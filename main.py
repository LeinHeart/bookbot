from stats import get_word_count,get_char_count
import sys

def main():
    if len(sys.argv) != 2 :
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    word_count,book_content = get_word_count(book_path)
    char_count = get_char_count(book_content)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char in char_count:
        print(f'{char['char']}: {char['count']}')


main()