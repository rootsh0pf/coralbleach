#!/usr/bin/python

## README ##################################################################
# 1. Install the python library "opencv"
# 2. Paint your leaf photos using EXACTLY the following colours (R, G, B):
#       Scales:             Magenta (255, 000, 255)
#       Healthy leaf area:  Blue    (000, 000, 255)
#       Damaged area:       Red     (255, 000, 000)
# 3. Save them in PNG file format
# 4. Run this script in the folder containing the photos
# 5. It will create a CSV file called "leaf_damage.csv"
############################################################################


## SETTINGS ################################################################
# Set scale size.
# It's unit will also be the output unit (eg. cm2).
scale_size = 1

# Accuracy of output (decimal places)
accuracy = 4
############################################################################


# Import necessary libraries
import cv2
import os
import csv
import numpy as np

# List all PNG files in the current folder
files = [x for x in os.listdir() if x.lower().endswith('.png')]
# Sort filenames alphabetically
files.sort()
count = len(files)

# Stop if no photos are found
if count == 0: print('No photos found in current folder. Make sure they are in PNG format!')
else:
    # Create a CSV file to write the results
    with open('leaf_damage.csv', 'w',  newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write a header row to the CSV file
        writer.writerow(['Filename', 'TotalLeafArea', 'DamageArea', 'DamagePercent'])
        print('Filename TotalLeafArea DamageArea DamagePercent')
        
        # Initialise counter for warnings
        warn_count = 0

        for idx in range(count):
            img = cv2.imread(files[idx])
            fileName = os.path.splitext(files[idx])[0]

            #damage
            red_pixel_count = cv2.countNonZero(cv2.inRange(img, (0,0,254), (0,0,255)))
            #leaf
            blue_pixel_count = cv2.countNonZero(cv2.inRange(img, (254,0,0), (255,0,0)))
            #reference square
            magenta_pixel_count = cv2.countNonZero(cv2.inRange(img, (254,0,254), (255,0,255)))
            
            # Count number of scale squares to average them in case there are more than one
            # Define lower and upper bounds for the color of interest (magenta)
            lower_color = np.array([254,0,254])
            upper_color = np.array([255,0,255])

            # Create a mask based on the color threshold
            mask = cv2.inRange(img, lower_color, upper_color)

            # Find contours of objects in the mask
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Count the number of objects that match the color of interest
            num_scales = len(contours)
            
            # Deal with some possible errors
            if num_scales == 0 or magenta_pixel_count == 0:
                print(f"{idx+1}/{count}: {fileName} WARNING: No scales detected")
                warn_count += 1
            elif blue_pixel_count == 0:
                print(f"{idx+1}/{count}: {fileName} WARNING: No leaf detected")
                warn_count += 1
            else:
                # Calculate average of scale sizes
                magenta_pixel_count = magenta_pixel_count/num_scales
                # Calculate values from pixel counts
                total_leaf_area = round((red_pixel_count+blue_pixel_count)/(magenta_pixel_count/scale_size), accuracy)
                damage_area = round(red_pixel_count/(magenta_pixel_count/scale_size), accuracy)
                damage_percent = round(red_pixel_count/(blue_pixel_count+red_pixel_count)*100, accuracy)
                # Write row into CSV file
                writer.writerow([fileName, total_leaf_area, damage_area, damage_percent])
                # Print in console
                print(f"{idx+1}/{count}: {fileName} {total_leaf_area} {damage_area} {damage_percent}")
        
        # Report warnings
        if warn_count == 0: print("Success!")
        else: print(f"Done. But {warn_count} photos skipped with warnings.")
