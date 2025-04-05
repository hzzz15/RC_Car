# 🚲 전동킥보드 주행 보조 시스템

## 1. 프로젝트 개요
### 목표
전동킥보드의 **안전성 향상 및 사용 편의성 개선**를 위해, 특정 라인을 따른 주행을 가능하게 하는 **주행 보조 시스템 프로토키프**를 구축

### 해결하고자 하는 문제
- 전동킥보드 사용자의 급증(10배 이상)과 이에 따른 **운행 사고 증가**
- 안전한 주행을 위한 **라인 트레이싱 시스템 필요성 증가**
- 주행 데이터를 수집 및 분석하여 **자동 보조 주행 알고리즘 개발**

### 주요 기능
- **RC카 기반 라인 트레이서 구현** (라즈베리파이 활용)
- **카메라(135°, 90°, 45°)를 이용한 데이터 수집 및 분석**
- **CNN 모델 학습 후 주행 보조 시스템 적용**
- **VNC Viewer를 이용한 원격 조작 기능**

---

## 2. 프로젝트 구조
```plaintext
├── src/                         # 주요 코드 파일 폴더
│   ├── bluetooth_serial.py      # 블루투스를 통한 차량 통신
│   ├── camera_test.py           # 카메라 테스트 코드
│   ├── image_processing.py      # 이미지 처리
│   ├── image_save.py            # 사용자 입력을 통해 이미지 데이터 저장
│   └── run_autodrive.py         # 저장된 CNN 모델 적용 및 실시간 보조 주행
└─ README.md                    # 프로젝트 개요 및 실행 방법
```

### 주요 파일 설명  
- **`bluetooth_serial.py`** → 블루투스를 이용한 RC카 제어 기능  
- **`camera_test.py`** → 카메라가 정산적으로 작동하는지 확인  
- **`image_save.py`** → 사용자의 입력에 따른 이미지 저장
- **`image_processing.py`** → 저장된 이미지를 전체 전처리하고 CNN 모델 학습 수행
- **`run_autodrive.py`** → 학습된 CNN 모델을 보내 다음 방향을 예측 및 표시

---

## 3. 설치 및 실행 방법
### 3.1 라즈베리파이 OS 설치
1. [라즈베리파이 공식 사이트](https://www.raspberrypi.org/software/)에서 **Raspberry Pi Imager** 다운로드
2. SD카드에 **Raspberry Pi OS** 설치
3. 라즈베리파이에 SD카드 삽입 후 불지

### 3.2 핫스팟과 VNC Viewer를 이용한 원격 접속
```bash
# SSH 활성화
sudo raspi-config
# 인터페이스 옵션에서 SSH 활성화 후 재부탁
```
1. `ifconfig`로 라즈베리파이 IP 조회
2. [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) 설치 후 IP로 원격 접속

### 3.3 이미지 수집 및 CNN 모델 학습
```bash
# 프로젝트 디렉토리 이동
cd ~/RC-CAR-ELECTRIC-SCOOTER/src

# 카메라 테스트 수행
python camera_test.py

# 사용자 입력을 통해 이미지 저장
python image_save.py

# 이미지 전처리 및 CNN 학습 수행
python image_processing.py
```

### 3.4 실시간 주행 보조 시스템 실행
```bash
# CNN 모델을 적용한 주행 보조 시스템 실행
python run_autodrive.py
```

---

## 4. 참고자료
```markdown
### 참고자리
- [라즈베리파이 공식 문서](https://www.raspberrypi.org/documentation/)
- [VNC Viewer 다운로드](https://www.realvnc.com/en/connect/download/viewer/)
```

---

> 결과적으로 RC카가 라인을 여부한 이미지를 보고 자동으로 다음 방향을 결정해 주혐하는 보조 시스템을 구현했습니다.
> 가장 가까운 보조 기능만 구현했고, GPIO 결합 제어는 최종 후로 계획입니다.