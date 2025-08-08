from deepface import DeepFace
import cv2

def detect_face_emotion():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Cannot open webcam")
        return "unknown"
    
    detected_emotion = "unknown"
    print("Press 'q' to stop face capture")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            detected_emotion = result[0]['dominant_emotion']
            print("Detected Emotion:", detected_emotion)

        except Exception as e:
            print("Emotion detection failed:", e)

        # Display the frame
        cv2.imshow("Face Emotion Detection (Press q to quit)", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return detected_emotion
