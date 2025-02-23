import sys
from stats import get_number_of_words, get_character_counts, sort_character_counts

def get_book_text(path_to_file):
    try:
        with open(path_to_file, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path_to_file}' was not found.")
        return None
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{path_to_file}'. Try using a different encoding.")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    if text:
        print(f"Found {get_number_of_words(text)} total words")
        chars = sort_character_counts(get_character_counts(text))
        for char in chars:
            if char.isalpha():
                print(f"{char}: {chars[char]}")

main()