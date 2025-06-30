# Matching logic using cosine similarity or keyword overlap

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_profiles():
    with open("data/user_profiles.json", "r") as f:
        return json.load(f)

def find_matches(target_name, top_n=3):
    profiles = load_profiles()
    names = [user["name"] for user in profiles]
    skillsets = [" ".join(user["skills"]) for user in profiles]

    if target_name not in names:
        return []

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(skillsets)
    target_index = names.index(target_name)

    similarity_scores = cosine_similarity(tfidf_matrix[target_index:target_index+1], tfidf_matrix).flatten()
    similarity_scores[target_index] = -1  # exclude self-match

    sorted_indices = similarity_scores.argsort()[::-1][:top_n]
    return [names[i] for i in sorted_indices]

