import cv2

class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def capture(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        _, buffer = cv2.imencode('.jpg', frame)
        return buffer.tobytes()

    def release(self):
        self.cap.release()
