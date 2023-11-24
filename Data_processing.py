
import os
import csv
import shutil

input_directory = 'D:\Programming\Stock Selections\Stock-Selection-Using-ML\Collect_Stock_Financial_Data'
output_directory = 'D:\Programming\Stock Selections\Stock-Selection-Using-ML\Processing_Financial_Data'

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(input_directory):
    for csv_file in files:
        if csv_file.endswith('.csv'):
            input_file_path = os.path.join(root, csv_file)
            
            # Get the relative path to the input file
            relative_path = os.path.relpath(input_file_path, input_directory)
            
            # Create the corresponding subdirectory in the output directory
            output_subdirectory = os.path.join(output_directory, os.path.dirname(relative_path))
            os.makedirs(output_subdirectory, exist_ok=True)
            
            # Construct the output file path in the new directory structure
            output_file_path = os.path.join(output_subdirectory, f"{csv_file}")

            with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
                reader = csv.reader(input_file)
                writer = csv.writer(output_file)

                # Process header
                header = next(reader)
                writer.writerow(header)

                # Process each row in the CSV file
                for row in reader:
                    # Update specific columns
                    for i in range(len(row)):
                        if not row[i]:
                            row[i] = '0.0'
                        elif '.' in row[i]:
                            decimal_part = row[i].split('.')[1][:4]
                            row[i] = f"{row[i].split('.')[0]}.{decimal_part}"

                    # Write the updated row to the output file
                    writer.writerow(row)

print("Processing complete. Check the output directory for processed files.")
