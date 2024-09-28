import os
import sys
import shutil
from mutagen.easyid3 import EasyID3

def organize_music_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.mp3'):
            try:
                file_path = os.path.join(folder_path, filename)
                audio = EasyID3(file_path)

                # Extract artist and album information
                artist = audio.get('artist', ['Unknown Artist'])[0].replace(':', '').replace('!', '').replace('?', '').replace('/', '')
                album = audio.get('album', ['Unknown Album'])[0].replace(':', '').replace('!', '').replace('?', '').replace('/', '')

                # Create destination folder path
                artist_folder = os.path.join(folder_path, artist)
                album_folder = os.path.join(artist_folder, album)

                # Create directories if they don't exist
                if not os.path.exists(artist_folder):
                    os.makedirs(artist_folder)
                if not os.path.exists(album_folder):
                    os.makedirs(album_folder)

                # Move the MP3 file to the appropriate folder
                shutil.move(file_path, os.path.join(album_folder, filename))
                print(f"Moved: {filename} -> {artist}/{album}/")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

if __name__ == '__main__':
    # Check if the folder path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python organize_mp3s.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        organize_music_folder(folder_path)
