import difflib 
def spell_check(word, dictionary): 
    matches = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.7) 
    return matches[0] if matches else "No suggestion" 
# Example dictionary 
dictionary = ["hello", "world", "spell", "checker", "python", 
"programming"] 
# Misspelled word 
misspelled = "progaming" 
correction = spell_check(misspelled, dictionary) 
print(f"Correction for '{misspelled}': {correction}")