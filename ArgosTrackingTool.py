#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Sara Sayed (sara.sayed@duke.edu)
# Date:   Fall 2020
#-------------------------------------------------------------

# Create a variable pointing to the file name
file_name = './data/raw/sara.txt'

# Create a file object from the file
file_object = open(file_name, 'r')

# Read contents of file into a list
line_list = file_object.readlines()

file_object.close()

#Iterate using a for loop
for lineString in line_list:
    if lineString[0] == "#" or lineString[0] == 'u': continue

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]             # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]                 # Observation Location Class
    obs_lat = lineData[6]               # Observation Latitude
    obs_lon = lineData[7]               # Observation Longitude
    
    # Print information to the use
    print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")
    

#Close the file
file_object.close()