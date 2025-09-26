import spacy
from collections import Counter

# Load spaCy English NLP model at import time
try:
    nlp = spacy.load("en_core_web_sm")
except OSError as e:
    raise RuntimeError(
        "spaCy model 'en_core_web_sm' not found. "
        "Run: python -m spacy download en_core_web_sm"
    ) from e


def spacy_tokens(
    text: str, 
    *,
    remove_stop: bool = True,
    lemmatize: bool = True,
    pos_whitelist: set[str] | None = None,
    ) -> list[str]:
    """
    Tokenize text using spaCy with options for stopword removal, lemmatization and part-of-speech (POS) filtering.
    
    Args:
        text (str): The input text to tokenize.
        
        remove_stop (bool, optional): If True, exclude stopwords.
        
        lemmatiza (bool, optional): If True, return lemmas, otherwise return raw text.
        
        pos_whitelist(str[str] | None, optional): If provided, only include token whose POS tag is in this set (eg: Noun, Adj).
        
    Returns:
        list[str]: A list of processed tokens.
    """
    
    document = nlp(text)
    processed_tokens: list[str] = []
    
    for tok in document:
        if not tok.is_alpha: # Skip non-alphabetic tokens (punctuation, numbers, symbols)
            continue
        if remove_stop and tok.is_stop: # Skip stopwords if requested
            continue
        if pos_whitelist and tok.pos_ not in pos_whitelist: # Skip tokens not in the whitelist if requested
            continue
        processed_tokens.append(tok.lemma_.lower() if lemmatize else tok.text.lower()) # Append lemma or raw token (lowercased)
    
    return processed_tokens




def spacy_top_words(
    text: str, 
    n: int = 10, 
    **kwargs
    ) -> list[tuple[str, int]]:
    """
    Gets the top N most frequent words from text using spaCy processing.
    
    Args:
        text (str): Input text to analyze.
        
        n (int, optional): Number of top words to return. Defaults to 10.
        
        **kwargs: Extra keyword arguments passed to spacy_tokens function (eg: remove_stop, lemmatize, pos_whitelist).
        
    Returns:
        list[tuple[str, int]]: A list of (word, number_of_occurence) pair sorted from most to least frequent
    """
    processed_words = spacy_tokens(text, **kwargs)
    return Counter(processed_words).most_common(n)


def spacy_unique_words_and_diversity(
    text: str, 
    **kwargs
    ) -> tuple[int, float]:
    """
    Calculate the number of unique words and lexical diversity of input text.
    
    Lexical diversity is defined as (unique_words / total_words).
    
    Args:
        text (str): Input text to analyze.
        **kwargs: Extra keyword arguments passed to spacy_tokens function (eg: remove_stop, lemmatize, pos_whitelist).
    
    Returns:
        tuple[int, float]: A pair (unique_words, diversity_ratio).
    """
    processed_words = spacy_tokens(text, **kwargs)
    total_words = len(processed_words)
    unique_words = len(set(processed_words))
    diversity = (unique_words / total_words) if total_words else 0.0
  
    return unique_words, diversity