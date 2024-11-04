# Filecopy

Copies file from pendrive in background
# Key Enhancements

- **User Input**: Users can now input the file names, destination, and scanning interval.
- **Menu Interface**: The program provides a menu to start or exit the scanning process.
- **Error Handling**: Checks for valid destination paths and handles non-integer scanning interval inputs.
- **Keyboard Interrupt Handling**: Users can stop the scanning with `Ctrl+C`.
- **Feedback Messages**: Improved feedback, showing whether files were found or not.

# Stealth Mode Enhancements

1. **Removed All `print` Statements**:
   - All `print` statements were removed to ensure no visible output is displayed, making the program fully silent.
   - All messages that were displayed with `print` are now logged to `file_copy_log.txt` using the `logging` module.

   ```python
   # Original Code Example:
   print("File '{file_name}' found and copied to {destination}")
   
   # Updated Stealth Code:
   logging.info(f"File '{file}' copied to {destination}")
Logging Only Mode:

Instead of printing information or errors to the terminal, the program logs all actions, such as file copy events and errors, exclusively in file_copy_log.txt.
The logging configuration is set up at the beginning of the script to format logs with timestamps and save all activity.
python
Copy code
# Set up logging at the top of the script
logging.basicConfig(filename='file_copy_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
Error Handling and Silent Exit:

If the destination folder does not exist, instead of printing an error, it now logs the error silently to file_copy_log.txt and exits.
Any other exceptions encountered during file copying are also logged silently without any terminal output.
python
Copy code
# Example Error Logging for Missing Destination
if not os.path.exists(destination):
    logging.error(f"The destination folder '{destination}' does not exist.")
    return
Silent Loop Execution:

The main function’s scanning loop operates without any terminal output or interaction. If the user stops the program manually, only a log entry is made.
python
Copy code
# Keyboard interrupt logging instead of terminal message
logging.info("Scanning stopped by user.")
