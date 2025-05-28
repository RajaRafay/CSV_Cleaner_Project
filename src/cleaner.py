import json 
import csv
import os

# Cleaning raw data and storing it in new csv file
def clean_to_csv():
    # Raw and clean file location 
    raw_data_file_path = "./data/raw_test_data.csv"
    clean_data_file_path = "./output/clean_test_data.csv"
    if not os.path.exists(raw_data_file_path):
        folder = "./data"
        filename = "raw_test_data.csv"
        full_path = os.path.join(folder, filename)
        os.mkdir(folder)
        with open(full_path, "w") as f:
            f.write("")
        print(f"Path is formed and an empty {filename} is created.")
    else:
        # Reading from raw data file
        with open(raw_data_file_path, 'r') as csv_file:
            if(os.path.getsize("./data/raw_test_data.csv") == 0):
                print("File is empty.")
                return
            else:
                csv_reader = csv.DictReader(csv_file)
                # Writing in clean data file
                with open(clean_data_file_path, 'w', newline="") as new_file:
                    fieldnames = csv_reader.fieldnames
                    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    for row in csv_reader:
                        row['Name'] = "N/A" if(row['Name'].strip()=="") else row['Name'].strip().title()
                        row['Email'] = "N/A" if(row['Email'].strip()=="") else row['Email'].strip().lower()
                        row['Phone'] = "N/A" if(row['Phone'].strip()=="") else "+" + row['Phone'].strip().replace("+","").replace('.',"").replace('x',"").replace('-',"")
                        row['DateOfBirth'] ="N/A" if(row['DateOfBirth'].strip()=="") else row['DateOfBirth'].strip()
                        row['Address'] = "N/A" if(row['Address'].strip()=="") else row['Address'].strip().upper()
                        row['Occupation'] = "N/A" if(row['Occupation'].strip()=="") else row['Occupation'].strip().title()
                        row['Score'] = "N/A" if(row['Score'].strip()=="") else row['Score']
                        row['Status'] = "Inactive" if(row['Status'].strip()=="") else row['Status']
                        row['Notes'] = "N/A" if(row['Notes'].strip()=="") else row['Notes'].strip().capitalize()
                        csv_writer.writerow(row)
                print(f"File is cleaned and save to the path: {clean_data_file_path} in .csv format")


# Cleaning raw data and storing it in new json file
def clean_to_json():
    jsonArr = []
    # Raw and clean data file location 
    raw_data_file_path = "./data/raw_test_data.csv"
    clean_data_file_path = "./output/clean_test_data.json"
    if not os.path.exists(raw_data_file_path):
        folder = "./data"
        filename = "raw_test_data.csv"
        full_path = os.path.join(folder, filename)
        os.mkdir(folder)
        with open(full_path, "w") as f:
            f.write("")
        print(f"Path is formed and an empty {filename} is created.")
    else:
        # Reading from raw data file
        with open(raw_data_file_path, 'r') as csv_file:
            if(os.path.getsize("./data/raw_test_data.csv") == 0):
                print("File is empty.")
                return
            else:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    row['Name'] = "N/A" if(row['Name'].strip()=="") else row['Name'].strip().title()
                    row['Email'] = "N/A" if(row['Email'].strip()=="") else row['Email'].strip().lower()
                    row['Phone'] = "N/A" if(row['Phone'].strip()=="") else "+" + row['Phone'].strip().replace("+","").replace('.',"").replace('x',"").replace('-',"")
                    row['DateOfBirth'] ="N/A" if(row['DateOfBirth'].strip()=="") else row['DateOfBirth'].strip()
                    row['Address'] = "N/A" if(row['Address'].strip()=="") else row['Address'].strip().upper()
                    row['Occupation'] = "N/A" if(row['Occupation'].strip()=="") else row['Occupation'].strip().title()
                    row['Score'] = "N/A" if(row['Score'].strip()=="") else row['Score']
                    row['Status'] = "Inactive" if(row['Status'].strip()=="") else row['Status']
                    row['Notes'] = "N/A" if(row['Notes'].strip()=="") else row['Notes'].strip().capitalize()
                    jsonArr.append(row)
                # Writing in clean data file
                with open(clean_data_file_path, 'w') as new_file:
                    jsonfile = json.dumps(jsonArr, indent=4)
                    new_file.write(jsonfile)
                print(f"File is cleaned and save to the path: {clean_data_file_path} in .json format")
                

    