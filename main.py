from stats import (
    count_words,
    count_chars,
    chars_dict_to_sorted_list
)
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print(f"Found {count_words(path)} total words in the document")
    
    chars_dict = count_chars(path)

    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

main()
