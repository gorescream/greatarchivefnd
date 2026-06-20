import zipfile

ARCHIVE_PATH = r"path\archive"
FILE_INSIDE = "file.txt" 

SEARCH_STRING = "string"

ENCODING = 'utf-8'  

print(f"Find '{SEARCH_STRING}' in archive...")

line_count = 0
found = False

with zipfile.ZipFile(ARCHIVE_PATH, 'r') as z:
    with z.open(FILE_INSIDE, 'r') as infile:
        for raw_line in infile:
            line_count += 1
            line = raw_line.decode(ENCODING, errors='ignore')
            if SEARCH_STRING in line:
                print(f"\n\nFounded")
                print(f"String number: {line_count}")
                print(f"Full string: {line.strip()}")
                found = True
                break
        
            if line_count % 500000 == 0:
                print(f"\rChecked: {line_count:,}".replace(",", " "), end="")

if not found:
    print(f"\n\nSearch end. String '{SEARCH_STRING}' not found. checked lines: {line_count:,}".replace(",", " "))
