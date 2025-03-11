import cv2
import numpy as np

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3, 160)  
    camera.set(4, 120)  

    if not camera.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            print("프레임을 가져올 수 없습니다.")
            break

        # 영상 뒤집기
        frame = cv2.flip(frame, -1)
        cv2.imshow('Normal', frame)

        # 관심 영역 추출
        crop_img = frame[60:120, 0:160]

        # 그레이스케일 변환
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

        # 가우시안 블러 적용
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # 반전
        ret_val, thresh1 = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow('Threshold', thresh1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
