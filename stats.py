def get_word_count(filepath):
    

    with open(filepath) as f:
        book_content = f.read().lower()


    split_text = book_content.split()
    return len(split_text), book_content

def sort_on(items):
    return items['count']

def get_char_count(book_content):
    char_count = {}
    char_count_list = []
    for char in book_content:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    for char in char_count:
        char_count_list.append({"char":char,"count":char_count[char]})
    
    char_count_list.sort(reverse=True, key=sort_on)

    return char_count_list