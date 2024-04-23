def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_count = count_letter_appearance(text)
    sorted_count = sort_dict_alphabetically(letter_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"Found {num_words} in document")
    for ch in sorted_count:
        if ch["char"].isalpha() == True:
            print(f"The {ch["char"]} character was found {ch["num"]} times")
    print("--- End report ---")

def count_words(text):
    length_of_text = text.split()
    return len(length_of_text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letter_appearance(text):
    letter_count_dict = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in letter_count_dict:
            letter_count_dict[letter] += 1
        else:
            letter_count_dict[letter] = 1
    return letter_count_dict

def sort_on(dict):
    return dict["num"]

def sort_dict_alphabetically(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char" : ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()