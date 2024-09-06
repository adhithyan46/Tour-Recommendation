import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def tour_recommend(user_profile, tour_data):
    # Convert user interests into a single string
    user_interests = ' '.join(user_profile['interests'])
    
    tour_data['Description'] = tour_data['type'].astype(str) + ' ' + tour_data['place'].astype(str)
    
    # Include the user interests in the dataset for TF-IDF calculation
    tour_data_with_profile = tour_data.copy()
    tour_data_with_profile = tour_data_with_profile.append(
        {'Description': user_interests},
        ignore_index=True
    )
    
    # Vectorize the descriptions including the user interests
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(tour_data_with_profile['Description'])
    
    # Calculate cosine similarity between the user's interests and all tours
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Get the indices of the top 5 most similar tours
    top_indices = cosine_sim.argsort()[0][-5:][::-1]
    
    # Select and return the top 5 recommendations
    recommendations = tour_data.iloc[top_indices]
    return recommendations