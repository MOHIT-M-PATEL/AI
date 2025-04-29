from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
def compute_similarity(text1, text2): 
    vectorizer = TfidfVectorizer() 
    tfidf = vectorizer.fit_transform([text1, text2]) 
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2]) 
    return similarity[0][0] 
# Example 
text1 = "NLP is fun." 
text2 = "NLP is not fun" 
score = compute_similarity(text1, text2) 
print(f"Similarity Score: {score:.4f}") 