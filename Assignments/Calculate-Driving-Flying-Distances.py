# Author: Daniel Ritter
# Date: October 16, 2023
# Purpose: Calculate driving and flying distances between cities

# Set up environment
from numpy import *
from math import *

# Define array representing network driving distances between cities
d = array([[     0, 999,  90, 999, 379, 999, 999, 303, 999, 999, 168, 999],
              [999,   0,  62, 999, 999, 999, 999, 999, 149, 999, 291, 999],
              [ 90,  62,   0, 999, 339, 999, 999, 999, 162, 999, 999, 999],
              [999, 999, 999,   0, 999, 999,  72, 999, 999, 999, 999, 999],
              [379, 999, 339, 999,   0,  87, 999, 999, 307, 999, 999, 366],
              [999, 999, 999, 999,  87,   0, 999, 352, 999, 999, 999, 999],
              [999, 999, 999,  72, 999, 999,   0, 999, 999,  62, 999, 999],
              [303, 999, 999, 999, 999, 352, 999,   0, 999, 999, 248, 999],
              [999, 149, 162, 999, 307, 999, 999, 999,   0,  73, 999, 247],
              [999, 999, 999, 999, 999, 999,  62, 999,  73,   0, 999, 278],
              [168, 291, 999, 999, 999, 999, 999, 248, 999, 999,   0, 999],
              [999, 999, 999, 999, 366, 999, 999, 999, 247, 278, 999,   0]])

##print(d)

# Define array of cities with UTM coordinates (Zone 12 easting/northing) and Lat/Long using WGS84 geodetic datum
f = [["Beaver",    356647, 4237752, 38.276389, -112.638889],
     ["Delta",     364415, 4357138, 39.353056, -112.573611],
     ["Fillmore",  384706, 4314043, 38.967778, -112.330833],
     ["Logan",     430910, 4620996, 41.737778, -111.830833],
     ["Moab",      626337, 4270335, 38.572500, -109.549722],
     ["Monticello",645836, 4192594, 37.869167, -109.341944],
     ["Ogden",     419447, 4564488, 41.227778, -111.961111],
     ["Page AZ",   459050, 4085449, 36.914167, -111.459722],
     ["Provo",     443795, 4455096, 40.244422, -111.660803],
     ["Salt Lake", 425430, 4511381, 40.750000, -111.883333],
     ["St George", 270880, 4108552, 37.095278, -113.578056],
     ["Vernal",    624174, 4479259, 40.454722, -109.535556]]

##print(f)

# Step 1: Calculate all-to-all flying distance in km

n = len(f)
flydist = zeros((n, n))
for i in range(n):
    for j in range(n):
        xc = pow(f[i][1] - f[j][1], 2)
        yc = pow(f[i][2] - f[j][2], 2)
        flydist[i, j] = round(sqrt(xc + yc) / 1000, 1)

print(f"Matrix of flying distance (km) between all cities: \n{flydist}")

# Step 2: Calculate all-to-all driving distance in km

def Floyd():
    n = len(d)
    # print(n)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i, j], d[i, k] + d[k, j])

Floyd()
drivedist = d
print(f"Matrix of driving distance (km) between all cities: \n{drivedist}")

# Step 3: Calculate a) ratio of driving to flying and b) difference between driving and flying

ratio = where(flydist == 0, 0, round_(divide(drivedist, flydist), 2)) # If dividing by zero, replace with 0 instead of nan
diff = round_(subtract(drivedist, flydist), 1)

print(f"Ratio of driving to flying distance: \n{ratio}")
print(f"Difference between driving and flying distance: \n{diff}")

# Step 4: Sort output from greatest to least ratio

output = []
n = len(f)
for o in range(n):
    for d in range(n):
        origin = f[o][0]
        destination = f[d][0] 
        driveval = drivedist[o, d]
        flyval = flydist[o, d]
        ratioval = ratio[o, d]
        diffval = diff[o, d]
        entry = [origin, destination, driveval, flyval, ratioval, diffval]
        output.append(entry)

output = list(filter(lambda pair:pair[2] != 0, output)) # Remove same city pairs
output.sort(key = lambda pair:pair[4], reverse = True) # Sort from greatest to least ratio
output.insert(0, ['From', 'To', 'Driving distance (km)', 'Flying distance (km)', 'Ratio', 'Difference']) # Add header row

for row in output:
    print(*row) # Print without formatting

# Optional: Print with formatting using tabulate library

##from tabulate import *
##print(tabulate(output, headers = ['From', 'To', 'Driving distance (km)', 'Flying distance (km)', 'Ratio', 'Difference']))

