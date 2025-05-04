from stats import get_num_words
from stats import string_to_character
from stats import sorted_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_counts = string_to_character(text)
    sorted_chars = sorted_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars.items():
        print(f"{char}: {count}")
    print("============= END ===============")
main()