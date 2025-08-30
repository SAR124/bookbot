def get_num_words(text):
    word_count = len(text.split())
    return word_count

def get_specific_character_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def get_sorted_chars(char_count):
    # Filter out non-alphabetic characters
    filtered_char_count = {char: num for char, num in char_count.items() if char.isalpha()}
    
    # Convert the filtered dictionary into a list of dictionaries
    sorted_list = [{"char": char, "num": num} for char, num in filtered_char_count.items()]
    
    # Sort the list in place by the "num" key in descending order
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    
    return sorted_list
