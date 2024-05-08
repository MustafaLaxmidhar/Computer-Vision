import os
#import cv2
import numpy as np
# import Filter1
import csv
# Sets the main folder to run throught
main_folder = "WeldGapImages"
# Sets up the output folder
processed_folder = 'Processed WeldGapImages'
# Sets up the output CSV file
results_csv_file = "Results.csv"
# checks if there is a folder existing and if there isnt it will create a new one
if not os.path.exists(processed_folder):
    os.makedirs(processed_folder)

# goes through and processes everything in the file
def iterate_files(folder_path, csv_writer):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            processed_file_path = os.path.join(processed_folder, file_name)
            file = os.path.join(root, file_name)
            print("File:", file)
            with open(file, 'r') as file:
                # Call the filter function here
                csv_result, processed_image = filter1. 
                # Writes the results into a csv file
                csv_writer.writerow([file, results]) 
                processed_image.save(processed_file_path)

# Opens csv file to write in
with open(results_csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(['file', 'result'])

    iterate_files(main_folder, csv_writer)

