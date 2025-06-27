def get_book_text(file_path):
    #takes a file path and returns contents as string
    with open(file_path) as f:
        return f.read()
    
def count_words_in_block(book_block):
    #takes a book_block string and counts the number of words by spliting it then ranging it
    words = book_block.split()
    word_count = len(words)
    return f"{word_count} words found in the document"

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


