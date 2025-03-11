import cv2
import RPi.GPIO as GPIO
import time
import os

def save_single_image():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)  
    camera.set(4, 480)  

    if not camera.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    save_dir = "/home/pi/AI_CAR/video/test_image"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "test.png")

    while camera.isOpened():
        key = cv2.waitKey(10)
        if key == ord('q'):
            break

        ret, image = camera.read()
        if not ret:
            print("프레임을 가져올 수 없습니다.")
            break

        # 이미지 뒤집기
        image = cv2.flip(image, -1)
        cv2.imshow('Original', image)
        cv2.imwrite(filepath, image)
        time.sleep(1.0)

    camera.release()
    cv2.destroyAllWindows()

def save_image_sequence():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)
    camera.set(4, 480)

    if not camera.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    save_dir = "/home/pi/AI_CAR/video/test_image"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "test")
    i = 0

    while camera.isOpened():
        key = cv2.waitKey(10)
        if key == ord('q'):
            break

        ret, image = camera.read()
        if not ret:
            print("프레임을 가져올 수 없습니다.")
            break

        image = cv2.flip(image, -1)
        cv2.imshow('Original', image)
        
        # 파일명(test_00000.png...)
        filename = "{}_{:05d}.png".format(filepath, i)
        cv2.imwrite(filename, image)
        i += 1

        time.sleep(1.0)

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    save_image_sequence()
    GPIO.cleanup()
