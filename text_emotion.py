from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def detect_text_emotion(text):
    result = sentiment_pipeline(text)
    label = result[0]['label'].lower()
    if label == "positive":
        return "happy"
    elif label == "negative":
        return "sad"
    return "neutral"
