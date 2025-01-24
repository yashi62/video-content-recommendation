import pandas as pd


class Database:
    def __init__(self):
        self.users = pd.read_csv('data/users.csv')
        self.videos = pd.read_csv('data/videos.csv')
        self.interactions = pd.read_csv('data/interactions.csv')

    def get_interactions(self):
        return self.interactions

    def get_user_interactions(self, user_id):
        return self.interactions[self.interactions['user_id'] == user_id]

    def add_interaction(self, user_id, video_id, rating):
        new_interaction = {'user_id': user_id, 'video_id': video_id, 'rating': rating}
        self.interactions = self.interactions.append(new_interaction, ignore_index=True)
        self.interactions.to_csv('data/interactions.csv', index=False)

    def get_all_videos(self):
        return self.videos.to_dict(orient='records')

    def get_video_titles(self, video_ids):
        return self.videos[self.videos['video_id'].isin(video_ids)]['title'].tolist()
