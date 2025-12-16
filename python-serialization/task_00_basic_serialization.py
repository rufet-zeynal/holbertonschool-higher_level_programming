import json

def serialize_and_save_to_file(data, filename):
    # Open the file in write mode ('w') to replace existing content
    with open(filename, 'w') as f:
        # Use json.dump to serialize the dictionary and save it to the file
        json.dump(data, f)

def load_and_deserialize(filename):
    # Open the file in read mode ('r')
    with open(filename, 'r') as f:
        # Use json.load to read the file and deserialize the JSON into a dictionary
        return json.load(f)

