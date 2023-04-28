# folderleaf
Python script to automatically calculate leaf sizes on photos by counting pixels of a certain colour

# Preparations:
 1. Take photos of leaves and place a calibration object of known size in the image (e.g. a black 1 x 1 cm square)
 1. Install the python library "opencv"
 2. Paint your leaf photos using EXACTLY the following colours (R, G, B):
 
       Scales:             Magenta (255, 000, 255)
       
       Healthy leaf area:  Blue    (000, 000, 255)
       
       Damaged area:       Red     (255, 000, 000)
       
       (The "fuzzy select"/magic wand tool of GIMP is super helpful for selecting regions of similar colour.)
       
 3. Save images in PNG file format
 4. Run this script in the folder containing the photos
 5. It will create a CSV file with the results called "leaf_damage.csv"
