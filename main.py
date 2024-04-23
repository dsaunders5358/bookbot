def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_count = count_letter_appearance(text)
    print(f"Found {num_words} in document")
    print(letter_count)

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
        elif letter == " ":
            pass
        else:
            letter_count_dict[letter] = 1
    return letter_count_dict

main()