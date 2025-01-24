import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from database import Database


class RecommendationSystem:
    def __init__(self):
        self.db = Database()
        self.user_video_matrix = self._create_user_video_matrix()

    def _create_user_video_matrix(self):
        interactions = self.db.get_interactions()
        user_video_matrix = interactions.pivot(index='user_id', columns='video_id', values='rating').fillna(0)
        return user_video_matrix

    def get_recommendations(self, user_id, top_n=5):
        if user_id not in self.user_video_matrix.index:
            raise ValueError(f"User ID {user_id} not found")

        user_vector = self.user_video_matrix.loc[user_id].values.reshape(1, -1)
        similarity_scores = cosine_similarity(self.user_video_matrix, user_vector).flatten()
        similarity_df = pd.DataFrame({'user_id': self.user_video_matrix.index, 'similarity': similarity_scores})
        similarity_df = similarity_df.sort_values(by='similarity', ascending=False)

        similar_users = similarity_df['user_id'].iloc[1:6].values
        recommendations = self._get_top_videos_from_similar_users(similar_users, user_id, top_n)
        return recommendations

    def _get_top_videos_from_similar_users(self, similar_users, user_id, top_n):
        watched_videos = set(self.db.get_user_interactions(user_id)['video_id'])
        all_videos = self.db.get_interactions()
        similar_user_videos = all_videos[all_videos['user_id'].isin(similar_users)]

        recommendations = similar_user_videos.groupby('video_id')['rating'].mean().sort_values(ascending=False)
        recommendations = recommendations.index.difference(watched_videos)[:top_n]
        video_titles = self.db.get_video_titles(recommendations)
        return video_titles

    def add_interaction(self, user_id, video_id, rating):
        self.db.add_interaction(user_id, video_id, rating)
        self.user_video_matrix = self._create_user_video_matrix()

    def list_videos(self):
        return self.db.get_all_videos()
