""" 
Task 2: Put all the .txt files from the data/ directory into a variable. Then, copy the content of all the files from this variable into a file in data/ that you will name 'final.txt'
"""

import os

# Get the absolute path of the data directory
data_dir = os.path.abspath("data")
print(data_dir)

# List all files in the data directory ending with .txt
txt_files = [file for file in os.listdir(data_dir) if file.endswith(".txt")]
print(txt_files)

# Initialize a variable to store the content of all .txt files
combined_content = ""

# Iterate over each .txt file, read its content, and append it to combined_content
for txt_file in txt_files:
    file_path = os.path.join(data_dir, txt_file)
    with open(file_path, "r") as file:
        combined_content += file.read()

# Write the combined content to final.txt in the data directory
final_file_path = os.path.join(data_dir, "final.txt")
with open(final_file_path, "w") as final_file:
    final_file.write(combined_content)

print("Content of all .txt files copied to final.txt successfully!")

