from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests (React runs on different port)

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

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    emotion = data.get('emotion', 'neutral')

    product_names = get_products(emotion)

    # Simulated product data with image and price (static for now)
    recommendations = [
        {
            "name": name,
            "price": 299 + i * 50,
            "image": f"https://via.placeholder.com/150?text={name.replace(' ', '+')}"
        }
        for i, name in enumerate(product_names)
    ]

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
