"""
Using a loop, open all the files from your data/ directory and save all their contents in a variable. 
"""

# Get the absolute path of the data directory
data_dir = os.path.abspath("data")

# Initialize a variable to store the content of all files
all_content = ""

# Iterate over each file and construct file path
for file in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file)
    
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            all_content += file.read()

# print content of all the files
print(all_content)

# Write the concatenated contents to a new file
output_file_path = os.path.join(data_dir, "combined_contents.txt")
with open(output_file_path, "w") as output_file:
    output_file.write(all_contents)

print("Combined contents saved to:", output_file_path)