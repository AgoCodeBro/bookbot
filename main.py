from stats import word_count
from stats import char_count
from stats import sorted_list
import sys

# Takes a file path as an input and returns the content of the file as a string

def get_book_text_(path):

    # Open file

    with open(path) as f:

        # Read file

        text = f.read()

        return text


def print_report(path, word_count, char_count):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for x in char_count:
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")

    print("============= END ===============")

def main():

    if len(sys.argv) == 2:

        path = sys.argv[1]
        frankenstein = get_book_text_(path)
        count = word_count(frankenstein)
        chars = char_count(frankenstein)
        list = sorted_list(chars)

        print_report(path, count, list)

    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
