import zipfile
import os

ARCHIVE_PATH = r"path\archive.zip"
FILE_INSIDE = "large_file.txt"
OUTPUT_PATH = r"path\current_chunk.txt"

# on default 500mb
CHUNK_SIZE = 500 * 1024 * 1024  

def chunk_generator(archive_path, file_inside, chunk_size):
    with zipfile.ZipFile(archive_path, 'r') as z:
        with z.open(file_inside, 'r') as infile:
            while True:
                chunk = infile.read(chunk_size)
                if not chunk:
                    break
                yield chunk

def main():
    print("Init..")
    if not os.path.exists(ARCHIVE_PATH):
        print(f"Archive not found: {ARCHIVE_PATH}")
        return

    extractor = chunk_generator(ARCHIVE_PATH, FILE_INSIDE, CHUNK_SIZE)
    
    chunk_number = 1
    
    while True:
        print(f"\nChunk #{chunk_number}. Enter to extract, q for exit ", end="")
        user_input = input().strip().lower()
        
        if user_input == 'q':
            break
            
        try:
            print("Extract chunk...")
            current_chunk = next(extractor)
            with open(OUTPUT_PATH, 'wb') as outfile:
                outfile.write(current_chunk)
            print(f"Done! Chunk #{chunk_number} saved on: {OUTPUT_PATH}")
            print(f"File size: {os.path.getsize(OUTPUT_PATH) // (1024*1024)} mb")
            chunk_number += 1
            
        except StopIteration:
            print("\nEnd archive")
            break
        except Exception as e:
            print(f"\nError: {e}")
            break

if __name__ == "__main__":
    main()
