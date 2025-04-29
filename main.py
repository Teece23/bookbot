import sys
from stats import get_num_words, char_count, dict_sort

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = char_count(text)
    sorted_dict = dict_sort(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ---------- ")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print ("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
