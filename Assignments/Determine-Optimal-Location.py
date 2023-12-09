# Author: Daniel Ritter
# Date: November 6, 2023
# Purpose: Determine optimal location based on minimum total weighted distance

# Create list of expected number of emergency calls from each neighborhood
call_list = [10, 20, 34, 21, 15, 6]

# Create array of distance between neighborhoods and potential fire station locations
dist_array = [[1.1, 1.9, 2.8, 2.4, 2.8, 3.4], 
           [1.4, 1.2, 1.8, 2.6, 2.5, 2.8], 
           [3.6, 2.4, 1.3, 3.7, 2.6, 1.6], 
           [2.3, 2.7, 3.4, 1.2, 1.6, 2.6], 
           [3.4, 2.6, 2.2, 2.7, 1.8, 1.0]]

# Define function to calculate total distance given a potential location (loc_index): 
def calTotalDistance(loc_index, dist_array, call_list):
    
    totalDistance = 0
    numNeighborhoods = len(call_list)

    for i in range(numNeighborhoods):
        totalDistance += call_list[i] * dist_array[loc_index][i]

    return totalDistance

# Create list to store distances
totalDist = []

# Iterate through potential locations and add distances to list
for i in range(len(dist_array)):
    D = round(calTotalDistance(i, dist_array, call_list), 2)
    # print("Distance for site {}: {}".format(i, D))
    totalDist.append(D)

# Find and report minimum distance and site index
minDist = min(totalDist)
siteIndex = totalDist.index(minDist)

print("The minimum total travel distance is {} miles.".format(minDist))
print("The best place to site the fire station will be at location: {}.".format(siteIndex))

