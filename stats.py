def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents

def count_words(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)

def count_chars(path):
    text = get_book_text(path).lower()
    counts_dict = {}
    for c in list(text):
        if c not in counts_dict:
            counts_dict[c] = 0
        counts_dict[c] += 1
    return counts_dict

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list