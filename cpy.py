import os
import psutil
import time
import shutil

def get_removable_drives():
    drives = []
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts:
            drives.append(partition.mountpoint)
    return drives

def find_and_copy_files(drive, files_to_find, destination):
    found_any = False
    for root, dirs, files in os.walk(drive):
        for file_name in files_to_find:
            if file_name in files:
                file_path = os.path.join(root, file_name)
                shutil.copy(file_path, destination)
                print(f"File '{file_name}' found and copied to {destination}")
                found_any = True
    if not found_any:
        print("No specified files found on the drive.")

def main():
    print("Welcome to the File Finder and Copier Program!")
    
    # Get input for the files to find
    files_to_find = input("Enter the file names to search for (comma-separated): ").split(',')
    files_to_find = [file.strip() for file in files_to_find]

    # Get input for the destination path
    destination = input("Enter the destination folder path: ").strip()
    if not os.path.exists(destination):
        print(f"The destination folder '{destination}' does not exist.")
        return

    # Get input for the scanning interval
    try:
        interval = int(input("Enter the scanning interval in seconds (default is 2): ").strip())
    except ValueError:
        interval = 2  # default value

    print("\nProgram is ready. Choose an option:")
    print("1. Start scanning for files")
    print("2. Exit the program")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == '1':
            print("\nStarting the scanning process. Press Ctrl+C to stop.\n")
            try:
                while True:
                    removable_drives = get_removable_drives()
                    
                    if removable_drives:
                        for drive in removable_drives:
                            print(f"Scanning drive {drive}...")
                            find_and_copy_files(drive, files_to_find, destination)
                    else:
                        print("No removable drives detected.")
                    
                    # Wait before the next scan
                    time.sleep(interval)
            
            except KeyboardInterrupt:
                print("\nScanning stopped by user.")
            break
        
        elif choice == '2':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
