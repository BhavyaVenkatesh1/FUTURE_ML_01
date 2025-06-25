import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_faq_data(file_path):
    df = pd.read_csv(file_path)
    df = df[['Question', 'Answer']].dropna()
    return df

def get_answer(faq_data, user_query):
    if not isinstance(user_query, str):
        return "⚠️ Invalid input. Please ask a question."
    user_query = user_query.strip().lower()
    faq_data['Question_clean'] = faq_data['Question'].str.lower().str.strip()

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(faq_data['Question_clean'])
    user_tfidf = tfidf.transform([user_query])

    similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix)
    max_score_idx = similarity_scores.argmax()
    max_score = similarity_scores[0, max_score_idx]

    if max_score < 0.5:
        return "🤖 Sorry, I couldn’t find a relevant answer. Please contact support."
    return faq_data.iloc[max_score_idx]['Answer']
