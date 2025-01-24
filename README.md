# Video Content Recommendation System

A Python-based video recommendation system using collaborative filtering and Flask.

## Features
- Recommend videos based on user preferences.
- Add new user-video interactions.
- List available videos.

## Setup

### Prerequisites
- Python 3.8 or higher.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/video-content-recommendation.git
   cd video-content-recommendation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place data files in the `data/` folder.

4. Run the Flask server:
   ```bash
   python app.py
   ```

### API Endpoints
1. **Recommend Videos**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"user_id": 1}' http://127.0.0.1:5000/recommend
   ```

2. **Add Interaction**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"user_id": 1, "video_id": 3, "rating": 5}' http://127.0.0.1:5000/add_interaction
   ```

3. **List Videos**:
   ```bash
   curl http://127.0.0.1:5000/videos
   ```

## License
MIT
