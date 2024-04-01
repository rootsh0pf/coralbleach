#!/usr/bin/python

## SETTINGS ################################################################
# Accuracy of output (decimal places)
accuracy = 2
############################################################################


# Import necessary libraries
import cv2
import os
import csv
import numpy as np

# Define function for calculating total pixel count of an image
def count_total_pixels(img):
    height, width, _ = img.shape
    return height * width

# List all PNG files in the current folder
files = [x for x in os.listdir() if x.lower().endswith('.png')]
# Sort filenames alphabetically
files.sort()
count = len(files)

# Stop if no photos are found
if count == 0: print('No photos found in current folder. Make sure they are in PNG format!')
else:
    # Create a CSV file to write the results
    with open('coralbleach_results.csv', 'w',  newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write a header row to the CSV file
        writer.writerow(['Filename', 'HardCoralCover', 'Healthy', 'Paling', 'Bleached', 'Mortality'])
        # Also print header row in console
        print('Filename HardCoralCover Healthy Paling Bleached Mortality')
        
        # Initialise counter for warnings
        warn_count = 0

        for idx in range(count):
            img = cv2.imread(files[idx])
            fileName = os.path.splitext(files[idx])[0]

            #total
            total_pixel_count = count_total_pixels(img)
            #healthy
            green_pixel_count = cv2.countNonZero(cv2.inRange(img, (0,254,0), (0,255,0)))
            #paling
            yellow_pixel_count = cv2.countNonZero(cv2.inRange(img, (0,254,254), (0,255,255)))
            #bleached
            red_pixel_count = cv2.countNonZero(cv2.inRange(img, (0,0,254), (0,0,255)))
            #dead
            magenta_pixel_count = cv2.countNonZero(cv2.inRange(img, (254,0,254), (255,0,255)))
            
            
            # If there is no coral on the image
            if green_pixel_count + yellow_pixel_count + red_pixel_count + magenta_pixel_count == 0:
                # Write row into CSV file
                # Hard coral cover = 0 and all other values "NA"
                writer.writerow([fileName, 0, "NA", "NA", "NA", "NA"])
                # Print in console
                print(f"{idx+1}/{count}: {fileName}  0  NA  NA  NA  NA  (no coral)")
                warn_count += 1
            else:
                # Calculate values from pixel counts
                hard_coral_cover = round((green_pixel_count+yellow_pixel_count+red_pixel_count+magenta_pixel_count)/total_pixel_count*100, accuracy)
                healthy = round(green_pixel_count/total_pixel_count*100, accuracy)
                paling = round(yellow_pixel_count/total_pixel_count*100, accuracy)
                bleached = round(red_pixel_count/total_pixel_count*100, accuracy)
                mortality = round(magenta_pixel_count/total_pixel_count*100, accuracy)
                # Write row into CSV file
                writer.writerow([fileName, hard_coral_cover, healthy, paling, bleached, mortality])
                # Print in console
                print(f"{idx+1}/{count}: {fileName} {hard_coral_cover} {healthy} {paling}, {bleached}, {mortality}")
        
        # Report warnings
        if warn_count == 0: print("Success!")
        else: print(f"Done. But {warn_count} photos showed no coral. NAs introduced.")
