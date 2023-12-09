# Author: Daniel Ritter
# Date: October 30, 2023
# Purpose: Calculate minimum bounding rectangle

# Define a Point class with two elements
class Point:
    x = 0
    y = 0

# Define an array for 10 points
points = [Point() for i in range(10)]

# Define function to read (x, y) points from text file
def readFileXY(name):
    myFile = open(name, "r")
    numpoints = int(myFile.readline())
    print("Number of points: {}\nStudy features:".format(numpoints))
    for i in range(numpoints):
        points[i].x, points[i].y = [int(x) for x in myFile.readline().split()]
        print(points[i].x, points[i].y)
    myFile.close()
    return(numpoints)

# Define function to read (x, y, z) points from text file
def readFileXYZ(name):
    myFile = open(name, "r")
    numpoints = int(myFile.readline())
    print("Number of points: {}\nStudy features:".format(numpoints))
    for i in range(numpoints):
        points[i].x, points[i].y, points[i].z = [int(x) for x in myFile.readline().split()]
        print(points[i].x, points[i].y, points[i].z)
    myFile.close()
    return(numpoints)

# Define function to determine MBR
def MBR(f):
    minx = 999
    miny = 999
    maxx = 0
    maxy = 0
    for i in range(f):
        if points[i].x < minx:
            minx = points[i].x
        elif points[i].x > maxx:
            maxx = points[i].x
    for i in range(f):
        if points[i].y < miny:
            miny = points[i].y
        elif points[i].y > maxy:
            maxy = points[i].y
    print("MBR:")
    print("({}, {})".format(minx, miny))
    print("({}, {})".format(maxx, maxy))

# Define function to determine MBRP
def MBRP(f):
    minx = 100
    miny = 100
    minz = 100
    maxx = 0
    maxy = 0
    maxz = 0
    for i in range(f):
        if points[i].x < minx:
            minx = points[i].x
        elif points[i].x > maxx:
            maxx = points[i].x
    for i in range(f):
        if points[i].y < miny:
            miny = points[i].y
        elif points[i].y > maxy:
            maxy = points[i].y
    for i in range(f):
        if points[i].z < minz:
            minz = points[i].z
        elif points[i].z > maxz:
            maxz = points[i].z
    print("MBR:")
    print("({}, {}, {})".format(minx, miny, minz))
    print("({}, {}, {})".format(maxx, maxy, maxz))

# Define file paths for study areas
canvas1 = r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\MBR\points.txt"
canvas2 = r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\MBR\points2.txt"
p1s1 = r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\MBR\part1-study1.txt"
p1s2 = r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\MBR\part1-study2.txt"
p2s1 = r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\MBR\part2-study1.txt"
p2s2 = r"C:\Users\danie\OneDrive\Documents\Projects\GEOG6180\Assignments\MBR\part2-study2.txt"

# Define main functions to read text file and determine MBR or MBRP
def mainMBR(studyarea): 
    f = readFileXY(studyarea)
    MBR(f)

def mainMBRP(studyarea):
    f = readFileXYZ(studyarea)
    MBRP(f)

# Call the main function for all study areas
mainMBR(canvas1)
mainMBR(canvas2)
mainMBR(p1s1)
mainMBR(p1s2)
mainMBRP(p2s1)
mainMBRP(p2s2)

