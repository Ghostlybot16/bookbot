import sys
from stats import (
    text_to_words, 
    char_count, 
    to_sorted_dict, 
    top_ten_words, 
    unique_words_and_diversity,
)

# To make sure script does not crash if spaCy model is unavailable
try:
    from nlp_stats import spacy_top_words, spacy_unique_words_and_diversity
    SPACY_AVAILABLE = True
except Exception:
    SPACY_AVAILABLE = False


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
    Main entry point: loads text, prints classic stats then spaCy processed stats
    """ 
    # ---------------------- args ----------------------------------
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>") # Message to user on proper usage format
        sys.exit(1)

    file_path = sys.argv[1] # Stores the user entered 2nd argument of sys.argv as file path


    # --------------------- load text -------------------------------
    contents_of_book = get_book_text(file_path)
    
    
    # ------------- Classic String Splitting Method -----------------
    total_words = text_to_words(contents_of_book) 
    unique_count, diversity = unique_words_and_diversity(contents_of_book)
    total_characters = char_count(contents_of_book)
    sorted_dict = to_sorted_dict(total_characters)
    
    
    
    
    
    # ----------------- Output Report Format -------------------------
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print(f"Unique words: {unique_count}")
    print(f"Lexical diversity: {diversity:.3f}") # Regex-tokenized, Diversity value has 3 decimal places
    
    
    
    print("--------- Character Count -------")
    
    for dict_item in sorted_dict:
        if not dict_item["char"].isalpha():
            continue
        print(f"{dict_item['char']}: {dict_item['num']}")
    
    print("--------- Top 10 Words ---------")
    for word, count in top_ten_words(contents_of_book, 10):
        print(f"{word}: {count}")
    
    
    
    # ------------------ spaCy-enhanced section -----------------
    if SPACY_AVAILABLE:
        print("----------- NLP (spaCy) - Cleaned Words -------------")
        
        # --------------- Features Lemmatization and Stop Word Removal --------------
        uniq_lem, div_nlp = spacy_unique_words_and_diversity(
            contents_of_book,
            # These values already exist in nlp_stats.py , passing for clarity
            remove_stop=True,
            lemmatize=True,
            pos_whitelist=None,
        )
        
        
        # -------------- Lemmatization WITHOUT Stop Word Removal -------------------
        uniq_all, div_all = spacy_unique_words_and_diversity(
            contents_of_book,
            remove_stop = False,
            lemmatize = True,
            pos_whitelist=None,
        )
        
        print(f"Unique Words(lemma, no stopwords): {uniq_lem}")
        print(f"Lexical Diversity (lemma, no stopwords): {div_nlp:.3f}")
        
        print(f"Unique Words(lemma, with stopwords): {uniq_all}")
        print(f"Lexical Diversity (lemma, with stopwords): {div_all:.3f}")
        
        
        print(f"--------- Top 10 Words (lemma, no stopwords) ---------")
        for word, count in spacy_top_words(
            contents_of_book,
            n = 10,
            remove_stop=True,
            lemmatize=True,
            pos_whitelist=None,
        ):
            print(f"{word}: {count}")
    
    else:
        print("------- NLP (spaCy) -------")
        print("spaCy not available, install model to enable")   
    
    print("============= END ===============")


if __name__ == "__main__":
    main()