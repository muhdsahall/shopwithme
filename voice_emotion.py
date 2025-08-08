import numpy as np
import librosa

# Dummy emotion classifier – replace with real ML model later
def dummy_predict(features):
    return "happy"  # Static result for now

def detect_voice_emotion(audio_file):
    try:
        # Read the audio stream from Flask's FileStorage
        y, sr = librosa.load(audio_file, sr=None)
        
        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfccs_scaled = np.mean(mfccs.T, axis=0)

        # Predict emotion
        predicted_emotion = dummy_predict(mfccs_scaled)
        print("Detected Voice Emotion:", predicted_emotion)
        return predicted_emotion
    except Exception as e:
        print("Voice emotion detection failed:", e)
        return "unknown"
