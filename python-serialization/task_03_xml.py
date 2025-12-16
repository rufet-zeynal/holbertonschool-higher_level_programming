import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML format and saves it to a file.

    Args:
        dictionary (dict): The Python dictionary to serialize.
        filename (str): The name of the XML file to save the data to.
    """

    # 1. Create the root element
    root = ET.Element("data")

    # 2. Iterate through the dictionary items and add them as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # Convert value to string to ensure it can be written as element text
        child.text = str(value)

        # 3. Write the XML tree to the file
    tree = ET.ElementTree(root)

    try:
        # Use 'wb' mode for ElementTree.write to correctly handle encoding/formatting
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error during XML serialization: {e}")
        # Does not explicitly return a value, but handles errors gracefully
        return None


def deserialize_from_xml(filename):
    """
    Reads XML data from a file, deserializes it, and returns a Python dictionary.

    Args:
        filename (str): The name of the XML file to read from.

    Returns:
        dict or None: The deserialized Python dictionary, or None if an error occurs.
    """

    try:
        # 1. Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        reconstructed_dict = {}

        # 2. Navigate through elements to reconstruct the dictionary
        # The structure is assumed to be: <data> <key1>value1</key1> ... </data>
        for child in root:
            # The tag is the dictionary key, and the text is the dictionary value
            # NOTE on Data Types: XML element text is always a string.
            # The instructions show the output as {'age': '28'}, so we return strings.
            reconstructed_dict[child.tag] = child.text

        # 3. Return the constructed dictionary
        return reconstructed_dict

    except FileNotFoundError:
        print(f"Error: File not found at {filename}")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# --- Testing Block (Place this in a separate test file or remove before final submission) ---
if __name__ == "__main__":
    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',  # Values are strings, matching the required output format
            'city': 'New York'
        }

        xml_file = "data.xml"
        serialize_to_xml(sample_dict, xml_file)
        print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)

        # Verify the content is correct
        assert deserialized_data == sample_dict
        print("Verification successful: Deserialized data matches original.")


    main()