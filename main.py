def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    get_character_count(text)


def get_num_words(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as f:
        return f.read()
    

character_dict = {}
def get_character_count(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for character in alphabet:
        count = 0
        for char in text:
            if(char == character):
                count+=1
                character_dict[character] = count
                print(count)
    print(character_dict)



main()