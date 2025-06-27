def count_words_in_block(book_block):
    #takes a book_block string and counts the number of words by spliting it then ranging it
    words = book_block.split()
    word_count = len(words)
    return f"Found {word_count} total words"

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

def sort_on(items):
    return items["num"]

def char_count_sort(char_count_dictionary):
    #sorts the char count dictionary into a sorted list of dictionaries
    library_chars = []
    
    for char in char_count_dictionary:
            char_dic = {"char":char,"num":char_count_dictionary[char]}
            library_chars.append(char_dic)
    library_chars.sort(reverse=True, key=sort_on)
    return library_chars 