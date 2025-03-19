# 🚲 전동킥보드 주행 보조 시스템

## 1. 프로젝트 개요
### 목표
전동킥보드의 **안전성 향상 및 사용 편의성 개선**을 위해, 특정 라인을 따라 주행하는 **주행 보조 시스템 프로토타입**을 구축

### 해결하고자 하는 문제
- 전동킥보드 사용자의 급증(10배 이상)과 이에 따른 **운행 사고 증가**
- 안정적인 주행을 위한 **라인 트레이싱 시스템 필요성 증가**
- 주행 데이터를 수집 및 분석하여 **자동 보조 주행 알고리즘 개발**

### 주요 기능
- **RC카 기반 라인 트레이서 구현** (라즈베리파이 활용)  
- **카메라(135°, 90°, 45°)를 이용한 데이터 수집 및 분석**  
- **딥러닝 모델 학습 후 주행 보조 시스템 적용**  
- **VNC Viewer를 이용한 원격 조작 기능**  

---

## 2. 프로젝트 구조
```plaintext
├── src/                         # 주요 코드 파일 폴더
│   ├── bluetooth_serial.py      # 블루투스를 통한 차량 통신
│   ├── camera_test.py           # 카메라 테스트 코드
│   ├── image_processing.py      # 이미지 처리 및 데이터 분석
│   ├── image_save.py            # 촬영한 트랙 데이터 저장
│   ├── line_tracer.py           # 주행 보조 알고리즘 (라인 트레이싱)
├── README.md                    # 프로젝트 개요 및 실행 방법
```

### 주요 파일 설명  
- **`bluetooth_serial.py`** → 블루투스를 이용한 RC카 제어 기능  
- **`camera_test.py`** → 카메라가 정상적으로 작동하는지 확인하는 코드  
- **`image_processing.py`** → 수집된 트랙 데이터를 분석하고 전처리  
- **`image_save.py`** → 다양한 각도(135°, 90°, 45°)에서 촬영된 이미지 저장  
- **`line_tracer.py`** → 라인 트레이싱 알고리즘을 적용하여 주행 보조 기능 제공  

---

## 3. 설치 및 실행 방법
### 3.1 라즈베리파이 OS 설치
1. [라즈베리파이 공식 사이트](https://www.raspberrypi.org/software/)에서 **Raspberry Pi Imager** 다운로드
2. 마이크로 SD카드에 **라즈베리파이 OS** 설치
3. 라즈베리파이에 SD카드 삽입 후 부팅

### 3.2 핫스팟을 이용한 원격 접속
```bash
# SSH 활성화
sudo raspi-config
# 인터페이스 옵션에서 SSH 활성화 후 재부팅
```
- 1. 라즈베리파이의 IP 주소 확인 (ifconfig 명령어 사용)
- 2. VNC Viewer 다운로드 후 해당 IP로 원격 접속

### 3.3 코드 실행 및 데이터 수집
```bash
# 프로젝트 디렉토리 이동
cd ~/RC-CAR-ELECTRIC-SCOOTER/src

# 카메라 데이터 수집 실행
python camera_test.py

# 트랙 데이터 저장 실행
python image_save.py
```

### 3.4 모델 학습 및 주행 보조 적용
```bash
# 이미지 처리 및 전처리 수행
python image_processing.py

# 라인 트레이서 알고리즘 실행
python line_tracer.py
```

---

## 4. 라이선스 및 참고자료
```markdown
### 라이선스
본 프로젝트는 **MIT License** 하에 배포됩니다.

### 참고자료
- [라즈베리파이 공식 문서](https://www.raspberrypi.org/documentation/)
- [VNC Viewer 다운로드](https://www.realvnc.com/en/connect/download/viewer/)
```

---

> **참고**  
> 본 저장소에는 완성된 모델 학습 코드가 포함되어 있지 않습니다.  
> 실제 프로젝트에서는 CNN 모델을 별도로 학습 후, 임베디드 환경에 모델을 적용해 주행 보조 알고리즘을 구현했습니다.