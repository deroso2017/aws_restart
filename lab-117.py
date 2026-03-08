# Retrieve the protein sequence of human insulin from human preproinsulin

import os

# Get the folder where this Python file is located
# __file__ It contains the full path of the current Python file
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "files", "preproinsulin-seq.txt")
output_path_preproinsulin_seq_clean = os.path.join(
    base_dir, "files", "preproinsulin-seq-clean.txt"
)
output_path_lsinsulin_seq_clean = os.path.join(
    base_dir, "files", "lsinsulin-seq-clean.txt"
)
output_path_binsulin_seq_clean = os.path.join(
    base_dir, "files", "binsulin-seq-clean.txt"
)
output_path_cinsulin_seq_clean = os.path.join(
    base_dir, "files", "cinsulin-seq-clean.txt"
)
output_path_ainsulin_seq_clean = os.path.join(
    base_dir, "files", "ainsulin-seq-clean.txt"
)

# start 17
# Read the file
with open(input_path, "r") as file:
    content = file.read()

# Remove unwanted parts
content = content.replace("ORIGIN", "")
content = content.replace("//", "")
content = content.replace("61", "")
content = content.replace("1", "")
content = content.replace(" ", "")
content = content.replace("\n", "")  # Remove new lines

print(content)

# end 17

# start 18, 19, 21
with open(output_path_preproinsulin_seq_clean, "w") as file:
    file.write(content)

# end 18, 19, 21

# 20
print(len(content))
print("##########: ", len(content[0:24]))

# 22
with open(output_path_lsinsulin_seq_clean, "w") as file:
    file.write(content[0:24])

# 24
with open(output_path_binsulin_seq_clean, "w") as file:
    file.write(content[25:54])

# 26
with open(output_path_cinsulin_seq_clean, "w") as file:
    file.write(content[55:89])

# 28
with open(output_path_cinsulin_seq_clean, "w") as file:
    file.write(content[90:])

print("Cleaned file saved successfully.")
