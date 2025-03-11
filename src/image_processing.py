import cv2
import numpy as np
import os

def process_lane_image(image):
    """
    주어진 이미지에서 라인만 보이도록 보정
    단계:
      1. 관심 영역(ROI) 추출
      2. 그레이스케일 변환
      3. 가우시안 블러 적용
      4. 임계값 처리로 이진화 (라인 강조)
    """
    height, width = image.shape[:2]
    
    # 관심 영역
    roi = image[int(height * 0.5):height, 0:width]
    
    # 그레이스케일
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # 가우시안 블러
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 임계값 처리
    ret, thresh = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY_INV)
    
    return thresh

def main():
    input_folder = '/home/pi/AI_CAR/video/test_image'
    output_folder = '/home/pi/AI_CAR/video/image'
    
    os.makedirs(output_folder, exist_ok=True)
    
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("입력 폴더에 이미지 파일이 없습니다:", input_folder)
        return
    
    for file_name in image_files:
        input_path = os.path.join(input_folder, file_name)
        image = cv2.imread(input_path)
        
        if image is None:
            print("이미지를 불러올 수 없습니다:", input_path)
            continue
        
        processed = process_lane_image(image)
        
        base_name, ext = os.path.splitext(file_name)
        output_file = f"{base_name}_processed.png"
        output_path = os.path.join(output_folder, output_file)
        
        cv2.imwrite(output_path, processed)
        print("저장됨:", output_path)

if __name__ == '__main__':
    main()
