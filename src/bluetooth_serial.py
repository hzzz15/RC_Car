import threading
import serial
import time

# 블루투스 시리얼 설정
bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

gData = "" 

def serial_thread():
    global gData
    while True:
        data = bleSerial.readline().decode().strip()
        if data:
            gData = data

def main():
    """ 메인 루프: 받은 데이터 출력 """
    global gData
    try:
        while True:
            print("Serial Data:", gData)
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\n프로그램 종료")
    finally:
        bleSerial.close() 

if __name__ == '__main__':
    task1 = threading.Thread(target=serial_thread, daemon=True)
    task1.start()
    main()
