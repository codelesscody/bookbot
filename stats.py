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

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def sort_dict(items):
    """Sorts a dictionary into a list of dictionaries based on the value of each input key in descending order.

    Args:
        items (dictionary): A dictionary of key:value pairs where the value is a count of key occurrences.

    Returns:
        list: The sorted list of dictionaries -- each dictionary containing the previous key:value pair split into "char" (character) and "num" (count).
    """
    item_list = []
    for i in items:
        item_list.append({"char": i, "num": items[i]})
    item_list.sort(reverse=True, key=sort_on)
    return item_list