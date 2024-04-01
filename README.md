# CoralBleach
This python script automatically counts pixels of certain colours from all photos in a folder and calculates coral bleaching, paling and mortality.
It is based on my old script [Folderleaf](https://github.com/rootsh0pf/folderleaf) for calculating leaf damage in the same way.
I used it for my research and hope it will be helpful for others too.

## How to use it
 1. Install the python library "opencv"
 2. Take photos of corals
 3. Open photos one by one in GIMP or a similar photo editor
 4. If you use a quadrant, crop photos to quadrant size
 5. Paint your photos using EXACTLY the following colours (R, G, B):
       
       Healthy Coral:   Green    (000, 255, 000)
       
       Paling Coral:    Yellow   (255, 255, 000)
       
       Bleached Coral:  Red      (255, 000, 000)
       
       Dead Coral:      Magenta  (255, 000, 255)
       
       (Hint: The "fuzzy select"/magic wand tool of GIMP is super helpful for selecting regions of similar colour.)
 6. Save images in PNG file format, all in one folder
 7. Download the script "coralbleach.py"
 8. Run the script in the folder containing the photos
 9. It will create a CSV file with the results called "coralbleach_results.csv"
 
 Results are given as percent of the whole image area.
