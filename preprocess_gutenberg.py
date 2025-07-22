import os
import string

def preprocess_text(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    return text

def load_gutenberg_data(gutenberg_folder, output_file, chunk_size=1024*1024, max_size=1024*1024*1024*2):  # max_size is 2GB
    processed_size = 0
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for root, dirs, files in os.walk(gutenberg_folder):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        while True:
                            chunk = f.read(chunk_size)
                            if not chunk:
                                break
                            processed_chunk = preprocess_text(chunk)
                            out_f.write(processed_chunk)
                            processed_size += len(processed_chunk)
                            if processed_size >= max_size:
                                print(f"Reached the maximum size limit of {max_size} bytes.")
                                return

# Example usage
gutenberg_folder = "/Users/raunakraj/Documents/rapid_decrypt/gutenberg_en"
output_file = "/Users/raunakraj/Documents/rapid_decrypt/preprocessed_gutenberg.txt"
load_gutenberg_data(gutenberg_folder, output_file)
print(f"Preprocessed text data written to {output_file}")