def main():
    # Variables declared and assigned values that will be returned
    # from the corresponding functions
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_dict(book_text)
    char_count_sorted = char_dict_to_sorted_list(char_count)
    
    print(f"There are {word_count} words in this book.")
    for letter in char_count_sorted:
        print(f"The letter '{letter['char']}' appears {letter['num']} times.")

# Opens the file and displays its contents
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Takes the text and splits each word into a string, then counts the number of strings
def get_word_count(text):
    words = text.split()
    return len(words)

# Lowers the case of all letters, determines which characters in the text are letters, 
# then adds them to a dictionary with a value that increases the number of times they appear  
def get_char_dict(text):
    case_adjust = text.lower()
    character_count = {}
    for character in case_adjust:
        if character.isalpha() == True:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return(character_count)

# Used in the following function to sort by the key "num"
def sort_by(char_dicts):
    return char_dicts["num"]

# Creates an empty list, then adds dictionaries with redundant keys and values used for the
# purpose of sorting
def char_dict_to_sorted_list(char_dicts):
    sorted_list = []
    for char in char_dicts:
        sorted_list.append({"char": char, "num": char_dicts[char]})
    sorted_list.sort(reverse=True, key=sort_by)
    return sorted_list
    
main()
