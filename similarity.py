from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(min_df=1)
tfidf = vect.fit_transform(["I'd like an apple", "An apple a day keeps the doctor away", "Never compare an apple to an orange", "I prefer scikit-learn to Orange"])
print((tfidf * tfidf.T).A)