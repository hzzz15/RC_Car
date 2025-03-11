import cv2

def camera_test():
    camera = cv2.VideoCapture(-1)
    camera.set(3, 640)  # 가로 해상도 설정
    camera.set(4, 480)  # 세로 해상도 설정

    if not camera.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            print("프레임을 읽지 못했습니다.")
            break

        # 영상 출력
        cv2.imshow('Camera Test', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera_test()