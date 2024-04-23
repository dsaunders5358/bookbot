def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"Found {num_words} in document")

def count_words(text):
    length_of_text = text.split()
    return len(length_of_text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()