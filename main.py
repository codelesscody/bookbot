import sys
from stats import get_word_count
from stats import get_each_char_count
from stats import sort_dict

def get_book_text(filepath):
    """Reads the content of a book from a text file.

    Args:
        filepath (str): The path to the text file containing the book.

    Returns:
        str: The content of the book as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()



def main():
    book_path = None
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_each_char_count(book_text)
    sorted_char_count = sort_dict(char_count)
    #print(f'{word_count} words found in the document')
    #print(get_each_char_count(book_text))
    #    print(book_text)  # Print the text of the book

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()