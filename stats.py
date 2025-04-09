# Takes a string as an input and returns its word count as a int

def word_count(text):
    list = text.split()
    return len(list)


# Takes in a string and returns the number of times each character appears

def char_count(text):
    clean_text = text.lower()
    char_count = {}

    for char in clean_text:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(dict):
    return dict["num"]

def sorted_list(dict):
    list = []
    for key in dict:
        list.append({"char" : key, "num" : dict[key]})

    list.sort(reverse=True, key=sort_on)

    return list