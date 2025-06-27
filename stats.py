def count_words_in_block(book_block):
    #takes a book_block string and counts the number of words by spliting it then ranging it
    words = book_block.split()
    word_count = len(words)
    return f"{word_count} words found in the document"

def count_char_in_block(book_block):
    #takes a book_block string and counts the number of chars in it
    char_count_dictionary = {}
    
    for char in book_block:
        c = char.lower()
        if c in char_count_dictionary:
            char_count_dictionary[c] += 1
        else:
            char_count_dictionary[c] = 1

    return char_count_dictionary