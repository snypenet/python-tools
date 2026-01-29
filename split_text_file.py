#!/usr/bin/env python3
import os
import sys

def split_file_by_size(input_file, max_size, output_base=None):
    """
    Splits a large, tab-delimited file into smaller files line by line, based on the passed max_size (in bytes).
    
    Args:
        input_file (str): Path to the input file.
        max_size (int): Maximum size (in bytes) for each split file.
        output_base (str): Base name for output files. If None, uses the input file name.
    """
    
    # If output_base is not specified, use the input_file's base name without extension.
    [name, extension] = os.path.splitext(os.path.basename(input_file))
    if output_base is None:
        base_name = name
    else:
        base_name = output_base
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        part_number = 1
        current_size = 0
        out_filename = f"{base_name}_part{part_number}.{extension}"
        with open(out_filename, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line_size = len(line.encode('utf-8'))  # Byte count of this line
                
                # If adding this line would exceed the max_size, start a new file
                if current_size + line_size > max_size:
                    # Close current file
                    outfile.close()
                    
                    # Start a new part file
                    part_number += 1
                    out_filename = f"{base_name}_part{part_number}.{extension}"
                    outfile = open(out_filename, 'w', encoding='utf-8')
                    current_size = 0
                
                # Write line to the current file
                outfile.write(line)
                current_size += line_size

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <input_file> <max_size_in_bytes> [output_base]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    try:
        max_size = int(sys.argv[2])
    except ValueError:
        print("Error: max_size_in_bytes must be an integer.")
        sys.exit(1)
    
    output_base = None
    if len(sys.argv) == 4:
        output_base = sys.argv[3]
    
    split_file_by_size(input_file, max_size, output_base)

if __name__ == "__main__":
    main()
