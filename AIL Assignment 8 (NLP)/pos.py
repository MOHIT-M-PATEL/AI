import nltk
from nltk import word_tokenize, pos_tag
def pos_tag_sentence(sentence): 
    nltk.download('punkt_tab',quiet=True) 
    nltk.download('averaged_perceptron_tagger_eng',quiet=True) 
    tokens = word_tokenize(sentence) 
    tagged = pos_tag(tokens)    
    return tagged 
# Example 
sentence = "The quick brown fox jumps over the lazy dog." 
tags = pos_tag_sentence(sentence) 
print("POS Tags:", tags) 