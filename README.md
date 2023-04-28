# Folderleaf
This python script automatically counts pixels of certain colours from all photos in a folder and calculates leaf area and leaf damage.
I used it for my research and hope it will be helpful for others too.

# how to use it
 1. Take photos of leaves and place a calibration object of known size in the image (e.g. a black 1 x 1 cm square, see example photos)
 1. Install the python library "opencv"
 2. Paint your leaf photos using EXACTLY the following colours (R, G, B):
 
       Scales:             Magenta (255, 000, 255)
       
       Healthy leaf area:  Blue    (000, 000, 255)
       
       Damaged area:       Red     (255, 000, 000)
       
       (The "fuzzy select"/magic wand tool of GIMP is super helpful for selecting regions of similar colour.)
       
 3. Save images in PNG file format
 4. Download the script "folderleaf.py" and run it in the folder containing the photos
 5. It will create a CSV file with the results called "leaf_damage.csv"
