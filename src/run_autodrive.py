import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("/home/pi/AI_CAR/cnn_model.h5")
IMG_SIZE = 64
label_map = {0: "left", 1: "right", 2: "straight"}

def preprocess(frame):
    roi = frame[60:120, 0:160]  # 관심 영역
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY_INV)
    resized = cv2.resize(binary, (IMG_SIZE, IMG_SIZE))
    return resized.reshape(1, IMG_SIZE, IMG_SIZE, 1) / 255.0

def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 160)
    cam.set(4, 120)

    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            break

        frame = cv2.flip(frame, -1)
        input_img = preprocess(frame)
        pred = model.predict(input_img)
        direction = label_map[np.argmax(pred)]

        print("예측 방향:", direction)

        # 화면에 예측 결과 출력
        cv2.putText(frame, direction, (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("AutoDrive", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
