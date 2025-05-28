import unittest
import os
import csv
import json
from cleaner import clean_to_csv, clean_to_json

class TestCleanerIntegration(unittest.TestCase):
    def fileChecking(self):
        os.makedirs('./data', exist_ok=True)
        os.makedirs('./output', exist_ok=True)
        self.raw_csv_path = './data/raw_test_data.csv'
        self.output_csv_path = './output/clean_test_data.csv'
        self.output_json_path = './output/clean_test_data.json'

        # Create test input CSV file
        with open(self.raw_csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Email', 'Phone', 'DateOfBirth', 'Address', 'Occupation', 'Score', 'Status', 'Notes'])
            writer.writerow([' john doe ', ' John.Doe@EMAIL.COM ', ' 123-456-7890 ', ' 1990-01-01 ', ' 123 Elm St ',
                             ' software engineer ', ' 85 ', 'Active', 'excellent candidate '])

    def cleaningFileAfterTesting(self):
        # Clean up files after test
        for path in [self.raw_csv_path, self.output_csv_path, self.output_json_path]:
            if os.path.exists(path):
                os.remove(path)

    # CSV Cleaning Test 
    def test_clean_to_csv_creates_cleaned_file(self):
        clean_to_csv()
        with open(self.output_csv_path, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row['Name'], 'John Doe')
        self.assertEqual(row['Email'], 'john.doe@email.com')
        self.assertEqual(row['Phone'], '+1234567890')
        self.assertEqual(row['Address'], '123 ELM ST')
        self.assertEqual(row['Occupation'], 'Software Engineer')
        self.assertEqual(row['Status'], 'Active')
        self.assertEqual(row['Notes'], 'Excellent candidate')

    # JSON Cleaning Test 
    def test_clean_to_json_creates_cleaned_file(self):
        clean_to_json()
        with open(self.output_json_path, 'r') as f:
            data = json.load(f)

        self.assertEqual(len(data), 1)
        row = data[0]
        self.assertEqual(row['Name'], 'John Doe')
        self.assertEqual(row['Email'], 'john.doe@email.com')
        self.assertEqual(row['Phone'], '+1234567890')
        self.assertEqual(row['Address'], '123 ELM ST')
        self.assertEqual(row['Occupation'], 'Software Engineer')
        self.assertEqual(row['Status'], 'Active')
        self.assertEqual(row['Notes'], 'Excellent candidate')

if __name__ == '__main__':
    unittest.main()
