import os
import shutil
import sys

def organize_mp3_files(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an mp3 file
        if filename.endswith(".mp3"):
            # Split the filename on the "-" character
            parts = filename.split("-")
            
            if len(parts) > 1:
                # Use the first part as the folder name
                folder_name = parts[0].strip()
                folder_path = os.path.join(directory, folder_name)

                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the mp3 file into the folder
                source = os.path.join(directory, filename)
                destination = os.path.join(folder_path, filename)
                shutil.move(source, destination)
                print(f"Moved: {filename} -> {folder_path}")
            else:
                print(f"Skipping: {filename} (no '-' found)")

if __name__ == "__main__":
    # Check if directory path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python organize_mp3_files.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        organize_mp3_files(directory_path)
