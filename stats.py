def get_word_count(text):
    """Counts the number of words in a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)