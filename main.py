import sys
from stats import count_words_in_block 
from stats import count_char_in_block
from stats import char_count_sort

def get_book_text(file_path):
    #takes a file path and returns contents as string
    with open(file_path) as x:
        return x.read()
    
def main():
    #variable block
    book_block = ""
    
    if len(sys.argv) == 2:
        book_file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        raise sys.exit(1)
    
        

    #populate book_block by book_file_path
    book_block = get_book_text(book_file_path)
    print_report(book_file_path,book_block)
    return

def print_report(book_file_path,book_block):
    #prints book_block
    sorted_chars = []
    sorted_chars = char_count_sort(count_char_in_block(book_block))
    
    #prints report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}")
    print("----------- Word Count ----------")
    print(count_words_in_block(book_block))
    print("--------- Character Count -------")

    #prints the sorted_char list and filters non isalpha
    for i in sorted_chars:
        
        if i["char"].isalpha():
            c = i["char"]
            n = i["num"]
            line = f"{c}: {n}"
            print(line)
    print("============= END ===============")


    return

main()


