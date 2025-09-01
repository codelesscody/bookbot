from stats import get_word_count

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
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    print(f'{word_count} words found in the document')    
#    print(book_text)  # Print the text of the book

main()