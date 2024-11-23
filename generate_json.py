import os
import gzip
import base64
import json

# Assuming the 'flash' folder is in the current directory
flash_folder = 'flash'

# Initialize a list to collect the SWF data
swf_files_data = []

# Check if the directory exists
if os.path.exists(flash_folder):
    # Iterate over each .swf file in the directory
    for swf_filename in os.listdir(flash_folder):
        if swf_filename.endswith('.swf'):
            with open(os.path.join(flash_folder, swf_filename), 'rb') as swf_file:
                # Compress the .swf file using gzip
                gzipped_data = gzip.compress(swf_file.read())
                # Encode the gzipped data using base64
                base64_encoded_data = base64.b64encode(gzipped_data).decode('utf-8')
                swf_files_data.append({'name': swf_filename, 'data': base64_encoded_data})
    
    # Write the result to a JSON file
    with open('flash_games.json', 'w') as json_file:
        json.dump(swf_files_data, json_file, indent=4)