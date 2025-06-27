def count_words_in_block(book_block):
    #takes a book_block string and counts the number of words by spliting it then ranging it
    words = book_block.split()
    word_count = len(words)
    return f"{word_count} words found in the document"
