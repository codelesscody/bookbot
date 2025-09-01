def get_word_count(text):
    """Counts the number of words in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def get_each_char_count(text):
    """Counts the occurrences of each character in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count