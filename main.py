def main():
    book = "books/frankenstein.txt"
    text = get_text(book)
    word_count = get_count(text)
    char_count = get_char(text)
    char_list = get_char_list(char_count)
    
    print(f"---Begin report of {book} ---")
    print(f"There are {word_count} words in this document")
    print()

    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
        
def get_count(text):
    words = text.split()
    return len(words)
    
def get_text(path):
    with open(path) as f:
        # opening the frankenstein file for reading
        return f.read()

def get_char(text):
    lowered_text = text.lower()
    text_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for letter in lowered_text:
        if letter in text_dict:
            text_dict[letter] += 1
    return text_dict

def sort_on(d):
    return d["num"]

def get_char_list(char_count):
    list = []
    for x in char_count:
        list.append({"char": x, "num": char_count[x]})
    list.sort(reverse=True, key=sort_on)
    return list


main()