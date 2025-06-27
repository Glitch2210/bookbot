from stats import count_words_in_block

def get_book_text(file_path):
    #takes a file path and returns contents as string
    with open(file_path) as f:
        return f.read()
    
def main():
    #variable block
    book_block = ""
    book_file_path = "books/frankenstein.txt"

    #populate book_block by book_file_path
    book_block = get_book_text(book_file_path)

    #prints book_block
    print(count_words_in_block(book_block))
    return

main()


