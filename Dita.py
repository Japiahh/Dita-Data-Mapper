import json
import re

def extract_vocab(file_paths, output_path):
    """Data mapping from multiple Json files"""
    words = set()
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                text = json.dumps(data)
                words.update(re.findall(r'\b[a-zA-Z]+\b', text.lower()))
        except FileNotFoundError:
            print(f"file is not here; {file_path}")
        except json.JSONDecodeError:
            print(f"wrong format; {file_path}")
    
    vocab_data = {"vocab": {word: idx + 1 for idx, word in enumerate(sorted(words))}}
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        json.dump(vocab_data, outfile, indent=4, ensure_ascii=False)
    
    print(f"done; {output_path}")

input_files = [
    r"", 
    r"", 
    r""
    ]
output_file = r""
extract_vocab(input_files, output_file)
