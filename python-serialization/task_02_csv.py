import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file, converts it to JSON format, and saves it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """

    try:
        data_list = []

        # 1. Open the CSV file and read using DictReader
        # DictReader treats the first row as headers and converts each subsequent row into a dictionary
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)

            # Convert the DictReader iterator into a list of dictionaries
            for row in csv_reader:
                data_list.append(row)

        # 2. Serialize the list of dictionaries and write to data.json
        json_output_file = "data.json"

        # Open the output file in write mode ('w')
        with open(json_output_file, mode='w', encoding='utf-8') as jsonfile:
            # json.dump serializes the list (data_list) and writes it to the file
            # indent=4 is optional but makes the output data.json readable
            json.dump(data_list, jsonfile, indent=4)

        # 3. Return True on success
        return True

    except FileNotFoundError:
        # Handle the case where the input CSV file does not exist
        return False
    except Exception:
        # Handle other potential errors during file reading/writing (e.g., malformed CSV, permission errors)
        return False


