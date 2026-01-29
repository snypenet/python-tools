# File Splitter Script  

This script splits a large, tab-delimited text file into smaller files based on a specified maximum file size (in bytes). Each output file contains whole lines to ensure data integrity.  

## Features  
- Splits files while preserving entire lines.  
- Takes a maximum size in bytes to determine split points.  
- Allows optional output file name customization.  

## Requirements  
- Python 3.x  

## Usage  

```sh
python3 split_file.py <input_file> <max_size_in_bytes> [output_base]
```

### Arguments:  
- `<input_file>`: Path to the input file.  
- `<max_size_in_bytes>`: Maximum file size (in bytes) for each split file.  
- `[output_base]` (optional): Base name for output files. If not provided, the script uses the input file name.  

## Example  

```sh
python3 split_file.py large_file.txt 1048576
```

This command splits `large_file.txt` into multiple 1MB-sized parts, named `large_file_part1.txt`, `large_file_part2.txt`, etc.  

To specify a custom output base name:  

```sh
python3 split_file.py large_file.txt 1048576 split_output
```

This will generate files like `split_output_part1.txt`, `split_output_part2.txt`, etc.  

## Notes  
- The script ensures that each line remains intact and is not split across multiple files.  
- If a single line exceeds the specified max size, it will still be written to a new file.  
