def read_book(book):
    with open(book) as f:
        return f.read()

def word_count(book_contents):
    wc = book_contents.split()
    
    return len(wc)

def char_count(book_contents):
    temp_char_dict = {}
    char_list = []
    for char in book_contents:
        if char.lower() not in temp_char_dict:
            temp_char_dict.update({char.lower(): 1})
        else:
            temp_char_dict[char.lower()] += 1
    
    return temp_char_dict

def sort_on(dict):
    return dict["count"]

def convert_to_list(dict):
    char_list = []

    for i in dict:
        if i.isalpha(): 
            char_list.append({"char": i, "count": dict[i]})
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

def generate_report(book_word_count, book_char_count):
    print(f"--- Begin report of books/frankenstein.txt ---\n"
          f"{book_word_count} words found in the document\n\n")

    for i in range(len(book_char_count)):
        print(f"The \'{book_char_count[i].get('char')}\' character was found {book_char_count[i].get('count')} times")
    
    print("\n--- End report ---\n")

def main():
    book = "books/frankenstein.txt"
    book_content = read_book(book)
    book_word_count = word_count(book_content)
    book_char_count = char_count(book_content)
    char_list = convert_to_list(book_char_count)
    generate_report(book_word_count, char_list)

main()
