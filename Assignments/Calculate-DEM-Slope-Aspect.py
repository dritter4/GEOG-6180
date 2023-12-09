# Author: Daniel Ritter
# Date: October 23, 2023
# Purpose: Calculate slope and aspect from DEM

# Set up environment
from math import *
import numpy as np
import pandas as pd
import arcpy

filepath = r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\DEM\uofuDEM.txt"

# Create 2D array of 0's
n = 300
d = np.zeros((n, n))

# Define function to read DEM file
def ReadDEM():
    
    DEM_file = open(filepath, 'r')
    
    i = 0
    for line in DEM_file:
        l = line.split()         # Split line into list of strings
        for j in range(n):
            d[i,j] = float(l[j]) # Convert string numbers to float
        i = i + 1
    
    DEM_file.close()

# Read DEM file
ReadDEM()

print("\nStep 1. Read DEM file:\nThe DEM dimensions are", len(d), "by", len(d[0]))  # rows by cols
for i in range(3):
    for j in range(3):
        print(d[i][j])
    print

# Calculate and report the greatest difference in elevation
elevmin = np.min(d)
elevmax = np.max(d)
elevdiff = round(elevmax - elevmin, 1)

print("\nStep 2a. The greatest difference in elevation between any two cells is {} meters.".format(elevdiff))

# Categorize elevation cells into bins and report percentage in each bin
dflat = d.flatten()
bins = pd.cut(dflat, 5)
bincount = bins.value_counts()

print("\nStep 2b. Elevation Bins")

for i in range(5):
    percentage = round(bincount.iloc[i] / len(dflat) * 100, 1)
    binval = i + 1
    print("Bin {}: {}%".format(binval, percentage))

# Set DEM resolution and initialize slope
res = 10
s = 0.0

# Define slope and aspect arrays
slope = []
aspect = []

# Define slope and aspect function
def slopeaspect(i, j, d):
    b = float((d[i-1, j+1] + (2*d[i, j+1]) + d[i+1, j+1] - d[i-1, j-1] - (2*d[i, j-1]) - d[i+1, j-1]) / (8 * res))
    c = float((d[i+1, j-1] + (2*d[i+1, j]) + d[i+1, j+1] - d[i-1, j-1] - (2*d[i-1, j]) - d[i-1, j+1]) / (8 * res))
    
    s = degrees(atan(sqrt(pow(b, 2) + pow(c, 2))))
    
    a = 57.29578 * atan2(c, -b)
    a = round(a, 2)
    
    if a < 0:
        a = 90 - a
    elif a > 90.0:
        a = 360.0 - a + 90.0
    else:
        a = 90.0 - a
    
    slope.append(s)
    aspect.append(a)

# Calculate and store slope and aspect
for i in range(1, n - 1):
    for j in range (1, n - 1):
        slopeaspect(i, j, d)

print("\nStep 3. Calculation of slope and aspect is complete.")

# Convert list into 2D array
slope = np.array(slope).reshape(-1, 298)
aspect = np.array(aspect).reshape(-1, 298)

# Determine steepest and shallowest slopes
slopemin = round(np.min(slope), 2)
slopemax = round(np.max(slope), 2)
minloc = np.unravel_index(slope.argmin(), slope.shape)
maxloc = np.unravel_index(slope.argmax(), slope.shape)

print("\nStep 4a.")
print("The steepest slope is {} degrees and the cell is located at {}.".format(slopemax, maxloc))
print("The shallowest slope is {} degrees and the cell is located at {}.".format(slopemin, minloc))

# Categorize slope cells into bins and report percentage in each bin
sflat = slope.flatten()
binedge = [0, 10, 20, 30, 90]
bins = pd.cut(sflat, binedge)
bincount = bins.value_counts()

print("\nStep4b. Slope Bins")

for i in range(4):
    percentage = round(bincount.iloc[i] / len(dflat) * 100, 1)
    binval = i + 1
    binedge1 = binedge[i]
    binedge2 = binedge[i + 1]
    print("Bin {} ({}-{} degrees): {}%".format(binval, binedge1, binedge2, percentage))

# Categorize aspect cells into bins and report percentage in each bin
aflat = aspect.flatten()
binedge = np.linspace(0, 360, 17)
binlabels = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]
bins = pd.cut(aflat, binedge)
bincount = bins.value_counts()

print("\nStep4c. Aspect Bins")

for i in range(16):
    percentage = round(bincount.iloc[i] / len(dflat) * 100, 1)
    binval = i + 1
    binlabel = binlabels[i]
    print("Bin {} ({}): {}%".format(binval, binlabel, percentage))

# Export slope and aspect to text file
np.savetxt(r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\DEM\slope.txt", slope)
np.savetxt(r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\DEM\aspect.txt", aspect)

sraster = arcpy.NumPyArrayToRaster(slope)
araster = arcpy.NumPyArrayToRaster(aspect)

arcpy.CopyRaster_management(sraster, r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\DEM\slope.tif")
arcpy.CopyRaster_management(araster, r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\DEM\aspect.tif")
