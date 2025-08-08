def fuse_emotions(face, voice, text):
    weights = {"face": 0.4, "voice": 0.3, "text": 0.3}
    scores = {"happy": 0, "sad": 0, "angry": 0, "neutral": 0}

    if face in scores:
        scores[face] += weights["face"]
    if voice in scores:
        scores[voice] += weights["voice"]
    if text in scores:
        scores[text] += weights["text"]

    # Choose the emotion with the highest combined score
    return max(scores, key=scores.get)
