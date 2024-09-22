import os
import psutil
import time
import shutil

# Define the list of file names you're looking for and the destination path
files_to_find = ["hi.txt", "hellp.pnd"]
destination = r"C:\Users\NAME"

# Function to check if a pendrive is connected
def get_removable_drives():
    drives = []
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts:
            drives.append(partition.mountpoint)
    return drives

# Function to scan for the target files on the drive
def find_and_copy_files(drive):
    for root, dirs, files in os.walk(drive):
        for file_name in files_to_find:
            if file_name in files:
                file_path = os.path.join(root, file_name)
                shutil.copy(file_path, destination)
                print(f"File '{file_name}' found and copied to {destination}")

# Main loop to constantly check for the pendrive
while True:
    removable_drives = get_removable_drives()
    
    if removable_drives:
        for drive in removable_drives:
            print(f"Scanning drive {drive}...")
            find_and_copy_files(drive)
    
    # Wait for 5 seconds before checking again
    time.sleep(2)
