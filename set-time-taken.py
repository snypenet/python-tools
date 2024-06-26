import os
import sys
from PIL import Image
import piexif
from datetime import datetime
import time

def modify_date_taken(directory, new_date):
    # Ensure the new_date is in the correct format
    try:
        new_date_dt = datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S")
        new_date_str = new_date_dt.strftime("%Y:%m:%d %H:%M:%S")
    except ValueError:
        print("Date format should be YYYY-MM-DD HH:MM:SS")
        return

    # List of supported image formats
    supported_formats = ('jpg', 'jpeg', 'tiff', 'bmp', 'png')

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(supported_formats):
                filepath = os.path.join(root, filename)
                try:
                    # Load the image
                    img = Image.open(filepath)
                    
                    if img.format.lower() in ['jpeg', 'tiff']:  # Only JPEG and TIFF support EXIF
                        # Load existing EXIF data
                        exif_dict = piexif.load(img.info.get('exif', b''))
                        
                        # Update the DateTimeOriginal and DateTimeDigitized tags
                        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date_str.encode()
                        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date_str.encode()

                        # Convert the modified EXIF data back to bytes
                        exif_bytes = piexif.dump(exif_dict)
                        
                        # Save the image with the new EXIF data
                        img.save(filepath, exif=exif_bytes)
                        print(f"Updated date taken for {filename}")
                    else:
                        # Set the file's last modified and created times
                        mod_time = time.mktime(new_date_dt.timetuple())
                        os.utime(filepath, (mod_time, mod_time))
                        print(f"Updated file times for {filename}")
                except Exception as e:
                    print(f"Error updating {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python modify_date_taken.py <directory_path> <new_date_taken>")
        print("Date format should be YYYY-MM-DD HH:MM:SS")
    else:
        directory_path = sys.argv[1]
        new_date_taken = sys.argv[2]
        modify_date_taken(directory_path, new_date_taken)
