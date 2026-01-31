import os
import time

# Lab Task 3: File Manager
print("--- File Manager Demo ---")

# 1. Show current directory
cwd = os.getcwd()
print("Current dir:", cwd)

folder = "lab_files"

# 2. Create folder
# always check if it exists first
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Created folder: {folder}")
else:
    print("Folder already exists")

# 3. Create 3 text files
filenames = ["file1.txt", "file2.txt", "file3.txt"]

for name in filenames:
    path = os.path.join(folder, name)
    # creating empty file using 'w' mode
    f = open(path, "w")
    f.close()
    print(f"Created {name}")

# 4. List files
print("Files in folder:")
files = os.listdir(folder)
for f in files:
    print(f" > {f}")

# 5. Rename a file
original = os.path.join(folder, "file1.txt")
new_name = os.path.join(folder, "renamed.txt")

if os.path.exists(original):
    os.rename(original, new_name)
    print("Renamed file1.txt to renamed.txt")

# 6. Cleanup
print("Cleaning up in 2 seconds...")
time.sleep(2) # just so I can see what happened before deleting

# delete files inside first
all_files = os.listdir(folder)
for f in all_files:
    full_path = os.path.join(folder, f)
    os.remove(full_path)
    print(f"Deleted {f}")

# delete the folder
os.rmdir(folder)
print("Deleted folder. Done.")