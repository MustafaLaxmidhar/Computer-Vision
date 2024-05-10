import os
import cv2
import numpy as np
import timefunc
import csv
# Sets the main folder to run throught
main_folder = "WeldGapImages"
# Sets up the output folder
processed_folder = 'Final Result'
interim_folder = 'InterimResults'
# Sets up the output CSV file
results_csv_file = "WeldGapPositions.csv"
# checks if there is a folder existing and if there isnt it will create a new one
if not os.path.exists(processed_folder):
    os.makedirs(processed_folder)
if not os.path.exists(interim_folder):
    os.makedirs(interim_folder)
# goes through and processes everything in the file
def iterate_files(folder_path, csv_writer):
    # Sets up the start so that it doesnt check with previous
    start = 1
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            processed_file_path = os.path.join(processed_folder, file_name)
            file = os.path.join(root, file_name)
            file_path = str(file)
            # This gets the Set that it is currently in
            parent_folder = file_path[:13]
            sub_folder = file_path[14:19]
            image_name = file_path[20:]
            interim_image = file_path[20:29]
            print("File:", interim_image)
            with open(file, 'r') as file:
                # Call the filter function here wit the three inputs parent_folder, sub folder and image name 
                csv_result, processed_image, interim1, interim2 = timefunc.process_image(parent_folder, sub_folder, image_name) 
                output1 = os.path.join(interim_folder, interim_image + "_A_WeldGapPosition.jpg")
                cv2.imwrite(output1, interim1)
                output2 = os.path.join(interim_folder, interim_image + "_B_InterimResultY.jpg")
                cv2.imwrite(output2, interim2)
                # Conditional statements to check the CSV Saves
                # Checks if its the start of the set and can save it directly and start checking
                if start == 1:
                    # This checks if the result is valid if its the first result in a set 
                    if csv_result == -1:
                        csv_writer.writerow([image_name, "-1", "0"])  
                        output = os.path.join(processed_folder, file_name)
                        cv2.imwrite(output, processed_image)
                    else:
                        csv_writer.writerow([image_name, csv_result, "1"]) 
                        output = os.path.join(processed_folder, file_name)
                        cv2.imwrite(output, processed_image)
                    # saves as previous 
                        prev_csv_result = csv_result
                    prev_sub_folder = sub_folder
                    start = 0
                # Checks if the set is the same as the previous set
                elif sub_folder == prev_sub_folder:
                    # Checks weldgap if it is 1mm, 
                    if csv_result <= 22 + prev_csv_result and csv_result >= prev_csv_result - 22:
                        csv_writer.writerow([image_name, csv_result, "1"]) 
                        output = os.path.join(processed_folder, file_name)
                        cv2.imwrite(output, processed_image)
                        # If it is valid is saves it as previous 
                        prev_csv_result = csv_result
                    else:
                        # This is for when its not valid and is not witin 1 mm of previous
                        csv_writer.writerow([image_name, "-1", "0"]) 
                        output = os.path.join(processed_folder, file_name)
                        cv2.imwrite(output, processed_image)
                        # if it is not valid it does not save as previous, IDK if it should save it 
                        # seems more resonable to not save it if it is not valid
                    prev_sub_folder = sub_folder
                # This is for when a new set happens 
                else:
                    print("File:", csv_result)
                    csv_writer.writerow([image_name, csv_result, "1"]) 
                    output = os.path.join(processed_folder, file_name)
                    cv2.imwrite(output, processed_image)
                    prev_csv_result = csv_result
                    prev_sub_folder = sub_folder
# Opens csv file to write in
with open(results_csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(['Image name', 'Weld Gap Position in pixel', 'Validity'])

    iterate_files(main_folder, csv_writer)

