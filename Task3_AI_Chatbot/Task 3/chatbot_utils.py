import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_faq_data(file_path):
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        df = df[['Question', 'Answer']].dropna()
        df['Question_clean'] = df['Question'].str.lower().str.strip()
        return df
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return pd.DataFrame(columns=['Question', 'Answer', 'Question_clean'])

def get_answer(faq_data, user_query):
    if not isinstance(user_query, str):
        return "⚠️ Invalid input. Please ask a question."

    user_query = user_query.strip().lower()

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(faq_data['Question_clean'])
    user_tfidf = tfidf.transform([user_query])

    similarity_scores = cosine_similarity(user_tfidf, tfidf_matrix)
    max_score_idx = similarity_scores.argmax()
    max_score = similarity_scores[0, max_score_idx]

    matched_question = faq_data.iloc[max_score_idx]['Question']
    matched_answer = faq_data.iloc[max_score_idx]['Answer']

    print("🔍 User Query:", user_query)
    print("📊 Top Match Score:", max_score)
    print("📄 Matched Question:", matched_question)

    if max_score < 0.3:  # You can adjust this threshold
        return "🤖 Sorry, I couldn’t find a relevant answer. Please contact support."

    return matched_answer
