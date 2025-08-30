from stats import get_num_words
from stats import get_specific_character_count
from stats import get_sorted_chars
import sys

def get_book_text(file_path_input):
    with open(file_path_input) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    if len(sys.argv) != 2:
        print("Error: Please provide the path to the book file as a command-line argument.")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])

    num_words = get_num_words(book_text)

    print(f"Found {num_words} total words")

    char_count = get_specific_character_count(book_text)

    sorted_chars = get_sorted_chars(char_count)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()


    
