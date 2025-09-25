from collections import Counter

def text_to_words(text_file):
    """
    Splits the text file and finds the total number of words present in the file
    """
    
    split_message = text_file.split()
    
    num_words = len(split_message)
    
    return num_words

def char_count(text):
    """
    Counts the number of times each character appears 
    """ 
    
    text = text.lower()
    
    string_to_int = {}
    
    for char in text:
        if char in string_to_int:
            string_to_int[char] += 1
        else:
            string_to_int[char] = 1
    
    return string_to_int


def sort_on(item):
    return item["num"]


def to_sorted_dict(char_dict):
    
    pairs = []
    
    for char, count in char_dict.items():
        pair = {"char": char, "num": count}
        pairs.append(pair)
    
    pairs.sort(reverse=True, key=sort_on)
    
    return pairs


def top_ten_words(text, n=10):
    """
    Accepts text (words) and applies counter to them and returns the the top 10 words
    """
    split_words = text.lower().split()
    counter = Counter(split_words) # Applies counter to the split words 
    top_ten_words = counter.most_common(n)
    
    return top_ten_words

def unique_words_and_diversity(text):
    """
    Returns counts of unique words and lexical diversity as percentage
    """
    all_words_from_text = text.lower().split()
    total_words = len(all_words_from_text) if all_words_from_text else 0
    unique_words = len(set(all_words_from_text))
    diversity = (unique_words / total_words) if total_words else 0.0
    
    return unique_words, diversity
    
    