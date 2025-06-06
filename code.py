import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load ratings data
ratings_data = pd.read_csv('ratings.csv')

# Load movies data
movies_data = pd.read_csv('movies.csv')

# Merge ratings and movies data
merged_data = pd.merge(ratings_data, movies_data, on='movieId')

# Drop unnecessary columns
merged_data = merged_data.drop(['timestamp', 'genres'], axis=1)

# Create user-item matrix
user_item_matrix = merged_data.pivot_table(index='userId', columns='movieId', values='rating')

# Split the data into training and testing sets
train_data, test_data = train_test_split(user_item_matrix, test_size=0.2, random_state=42)

# Calculate item-item similarity using cosine similarity
item_similarity = cosine_similarity(train_data.fillna(0))
np.fill_diagonal(item_similarity, 0)  # Set diagonal elements to 0 to avoid self-similarity

def get_recommendations(user_id, top_n=5):
    # Get the user's ratings and item similarity
    user_ratings = train_data.loc[user_id].values.reshape(1, -1)
    similarity_scores = item_similarity.dot(user_ratings.T).reshape(-1)

    # Sort the movies based on similarity scores
    sorted_indices = np.argsort(similarity_scores)[::-1]
    top_indices = sorted_indices[:top_n]

    # Get the recommended movie IDs
    recommended_movie_ids = user_item_matrix.columns[top_indices]

    # Get the movie titles
    recommended_movies = movies_data[movies_data['movieId'].isin(recommended_movie_ids)]

    return recommended_movies
