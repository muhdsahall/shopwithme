from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return "Server running!"

@app.route('/upload-image', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_data = data['image']
    image_bytes = base64.b64decode(image_data.split(',')[1])
    filename = datetime.now().strftime("image_%Y%m%d_%H%M%S.jpg")
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filepath, 'wb') as f:
        f.write(image_bytes)
    return jsonify({'message': 'Image saved successfully!', 'path': filepath})

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400
    audio_file = request.files['audio']
    filename = datetime.now().strftime("audio_%Y%m%d_%H%M%S.webm")
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    audio_file.save(filepath)
    return jsonify({'message': 'Audio saved successfully!', 'path': filepath})

@app.route('/upload-transcript', methods=['POST'])
def upload_transcript():
    data = request.get_json()
    transcript = data.get('transcript', '')
    filename = datetime.now().strftime("transcript_%Y%m%d_%H%M%S.txt")
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(transcript)
    return jsonify({'message': 'Transcript saved successfully!', 'path': filepath})

# ⬇️ Add product recommendation helper
def get_products(emotion):
    recommendations = {
        "happy": ["Colorful T-shirts", "Party Accessories", "Sunglasses", "Travel Backpacks"],
        "sad": ["Self-care Kit", "Motivational Books", "Aromatherapy Candles", "Comfort Snacks"],
        "angry": ["Stress Balls", "Boxing Gloves", "Meditation App Subscription", "Aromatherapy Oil"],
        "surprise": ["Mystery Boxes", "New Arrival Gadgets", "Limited Edition Items"],
        "fear": ["Home Safety Devices", "Night Lights", "Calming Tea Packs"],
        "disgust": ["Cleaning Supplies", "Deodorants", "Air Fresheners"],
        "neutral": ["Stationery", "Water Bottles", "Everyday Use Items"]
    }
    return recommendations.get(emotion.lower(), recommendations["neutral"])

# ⬇️ New /recommend route
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    emotion = data.get('emotion', 'neutral')

    product_names = get_products(emotion)
    recommendations = [
        {
            "name": name,
            "price": 299 + i * 50,
            "image": f"https://via.placeholder.com/150?text={name.replace(' ', '+')}"
        }
        for i, name in enumerate(product_names)
    ]

    return jsonify({"recommendations": recommendations})

# ⬇️ Start server
if __name__ == '__main__':
    app.run(debug=True)
