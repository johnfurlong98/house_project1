import os

# Step 1: Get the current working directory
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# Step 2: Change to the parent directory
# os.path.dirname(current_dir) gives the parent directory
parent_dir = os.path.dirname(current_dir)

# Step 3: Change the current working directory to the parent directory
os.chdir(parent_dir)
print("New Working Directory:", os.getcwd())