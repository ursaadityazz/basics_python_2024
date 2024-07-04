import os

# Replace "path/to/your/folder" with the actual path
folder_path = "D:\PycharmProjects\python 2024"

# Get list of items in the folder
items = os.listdir(folder_path)

# Print each item
for item in items:
  print(item)
