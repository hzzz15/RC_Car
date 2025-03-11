import cv2
import numpy as np
from tensorflow.keras.models import load_model
import RPi.GPIO as GPIO
import time

# 상수 정의
MODEL_PATH = './model/model.h5'
LEFT_MOTOR_PIN = 17
RIGHT_MOTOR_PIN = 27
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
RESIZE_DIM = (64, 64)  
CONTROL_DELAY = 0.1    

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT_MOTOR_PIN, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_PIN, GPIO.OUT)

def cleanup_gpio():
    GPIO.cleanup()

def initialize_camera():
    cap = cv2.VideoCapture(0)
    cap.set(3, CAMERA_WIDTH)
    cap.set(4, CAMERA_HEIGHT)
    return cap

def preprocess_frame(frame):
    """
    카메라 프레임 전처리 :
      - 이미지를 RESIZE_DIM 크기로 리사이즈
      - 픽셀 값을 정규화 (0~1)
    """
    resized = cv2.resize(frame, RESIZE_DIM)
    normalized = resized.astype('float32') / 255.0
    return np.expand_dims(normalized, axis=0)

def control_vehicle(prediction):
    """
    모델 예측 결과에 따른 RC카 제어 함수:
      - prediction: softmax 출력
      - 가장 높은 확률의 인덱스에 따라 방향 결정
        0: 정지, 1: 좌회전, 2: 우회전
    """
    direction = np.argmax(prediction)
    if direction == 0:
        print("정지")
        GPIO.output(LEFT_MOTOR_PIN, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_PIN, GPIO.LOW)
    elif direction == 1:
        print("좌회전")
        # 좌회전: 오른쪽 모터 동작
        GPIO.output(LEFT_MOTOR_PIN, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_PIN, GPIO.HIGH)
    elif direction == 2:
        print("우회전")
        # 우회전: 왼쪽 모터 동작
        GPIO.output(LEFT_MOTOR_PIN, GPIO.HIGH)
        GPIO.output(RIGHT_MOTOR_PIN, GPIO.LOW)
    else:
        print("알 수 없는 명령")
        GPIO.output(LEFT_MOTOR_PIN, GPIO.LOW)
        GPIO.output(RIGHT_MOTOR_PIN, GPIO.LOW)

def main():
    initialize_gpio()
    cap = initialize_camera()
    model = load_model(MODEL_PATH)
    print("모델 로드 완료")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("프레임 캡처 실패")
                break

            processed_frame = preprocess_frame(frame)
            prediction = model.predict(processed_frame)
            control_vehicle(prediction)

            cv2.imshow("Camera Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(CONTROL_DELAY)
    except KeyboardInterrupt:
        print("사용자 인터럽트")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        cleanup_gpio()
        print("자원 해제 및 종료")

if __name__ == '__main__':
    main()