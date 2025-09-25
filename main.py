import sys
from stats import text_to_words
from stats import char_count
from stats import to_sorted_dict
from stats import top_ten_words
from stats import unique_words_and_diversity

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>") # Message to user on proper usage format
    sys.exit(1)

def get_book_text(file_path):
    """
    The function accepts a file path to read all the content of the file.
    It places all the content of the file in a variable and returns the variable 
    """
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents
    
def main():
    """
    Main function / Entry point 
    
    Calls 3 other functions 
    
    get_book_text: reads the file and extracts all the content of the file 
    text_to_words: finds the total number of words from the entire content that was read 
    char_count: counts how many times each character appears in the entire file which was read
    """ 
    # file_path = "./books/frankenstein.txt"
    file_path = sys.argv[1] # Uses the user entered 2nd argument of sys.argv as file path
    contents_of_book = get_book_text(file_path)
    total_words = text_to_words(contents_of_book) 
    unique_count, diversity = unique_words_and_diversity(contents_of_book)
    total_characters = char_count(contents_of_book)
    sorted_dict = to_sorted_dict(total_characters)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print(f"Unique words: {unique_count}")
    print(f"Lexical diversity: {diversity:.3f}") # Diversity as a place value decimal
    print("--------- Character Count -------")
    
    for dict_item in sorted_dict:
        if not dict_item["char"].isalpha():
            continue
        print(f"{dict_item['char']}: {dict_item['num']}")
    
    print("--------- Top 10 Words ---------")
    for word, count in top_ten_words(contents_of_book, 10):
        print(f"{word}: {count}")
    
    print("============= END ===============")

main()