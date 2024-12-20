import os

# Get the current working directory
current_directory = os.getcwd()

# Print the contents of the current directory
print("Contents of the directory:")
for item in os.listdir(current_directory):
    print(item)
