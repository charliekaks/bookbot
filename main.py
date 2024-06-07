def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    get_character_count(text)
    get_report(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    report_list = get_report(text)
    for alpha in report_list:
        print(f"The '{alpha['char']}' character was found {alpha['num']} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as f:
        return f.read()
    


def get_character_count(text):
    character_dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for character in alphabet:
        count = 0
        lower_text = text.lower()
        for char in lower_text:
            if(char == character):
                count+=1
                character_dict[character] = count
    return character_dict

def sort_on(dict):
    return dict["num"]

def get_report(text):
    character_dict =get_character_count(text)
    report_list=[]
    for char in character_dict:
        report_list.append({"char": char, "num":character_dict[char]})
    report_list.sort(reverse=True, key=sort_on)
    return report_list


main()