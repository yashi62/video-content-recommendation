from flask import Flask, request, jsonify
from recommendation import RecommendationSystem

app = Flask(__name__)
rec_system = RecommendationSystem()

@app.route('/recommend', methods=['POST'])
def recommend_videos():
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        recommendations = rec_system.get_recommendations(user_id)
        return jsonify({'user_id': user_id, 'recommendations': recommendations}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/add_interaction', methods=['POST'])
def add_interaction():
    data = request.json
    user_id = data.get('user_id')
    video_id = data.get('video_id')
    rating = data.get('rating')

    if not all([user_id, video_id, rating]):
        return jsonify({'error': 'User ID, video ID, and rating are required'}), 400

    try:
        rec_system.add_interaction(user_id, video_id, rating)
        return jsonify({'message': 'Interaction added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/videos', methods=['GET'])
def list_videos():
    videos = rec_system.list_videos()
    return jsonify({'videos': videos}), 200


if __name__ == "__main__":
    app.run(debug=True)
