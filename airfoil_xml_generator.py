import re
import os
from xml.etree.ElementTree import Element, SubElement, ElementTree

def extract_reynolds_numbers(file_path):
    reynolds_numbers = set()  # Using a set to store unique Reynolds numbers
    with open(file_path, 'r') as file:
        for line in file:
            # Search for lines containing "is outside the flight envelope of polars"
            if "is outside the flight envelope of polars" in line:
                # Extract the Reynolds number using regex
                match = re.search(r'Re = ([\d.]+)', line)
                if match:
                    reynolds_number = float(match.group(1))
                    reynolds_numbers.add(reynolds_number)  # Add to set to ensure uniqueness
    return list(reynolds_numbers)  # Convert set back to list if needed

def create_xml(reynolds_number):
    root = Element('Analysis')
    fixed_reynolds = SubElement(root, 'Fixed_Reynolds')
    fixed_reynolds.text = str(reynolds_number)
    
    tree = ElementTree(root)
    file_name = f"reynolds_{int(reynolds_number)}.xml"
    tree.write(file_name)
    print(f"Generated XML file: {file_name}")

# Example usage:
log_file_path = 'XFLR5.log'
reynolds_numbers = extract_reynolds_numbers(log_file_path)

# Generate XML files for each unique Reynolds number
for reynolds_number in reynolds_numbers:
    create_xml(reynolds_number)
