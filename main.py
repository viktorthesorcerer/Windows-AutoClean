import os
import shutil
import time

# List of folders to clean
folders_to_clean = [
    "%TEMP%",
    "%APPDATA%\Local\Temp",
    "C:\Windows\Temp",
    "C:\Windows\SoftwareDistribution\Download",
    "C:\Windows\Prefetch",
    "C:\Windows\Logs",
    "C:\Windows\Memory.dmp"
]

# Expand environment variables in the list of folders
folders_to_clean = [os.path.expandvars(folder) for folder in folders_to_clean]

# Iterate over the list of folders
for folder in folders_to_clean:
    # Check if the folder exists
    if os.path.exists(folder):
        # Delete the contents of the folder
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isdir(filepath):
                try:
                    shutil.rmtree(filepath)
                except PermissionError:
                    # Print a message if the folder cannot be deleted
                    print(f"Unable to delete folder {filepath} because it is in use.")
            else:
                # Try deleting the file
                try:
                    os.remove(filepath)
                except PermissionError:
                    # Skip the file if it is in use
                    continue

        # Print a message if the folder was cleaned
        print(f"{folder} was cleaned.")
    else:
        # Print a message if the folder does not exist
        print(f"{folder} does not exist.")

print("Done!")
