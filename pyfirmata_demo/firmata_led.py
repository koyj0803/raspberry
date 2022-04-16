
# 아래의 import pyfirmata를 수행하기 위해서는 conda에 의해 생성된 가상환경(control)의 site-packages에 pyfirmata 패키지
#가 설치되어야 함
#(control) > pip install pyfirmata 


import pyfirmata as pf
import time

ard = pf.Arduino('COM6') # windows의 장치관리자를 열어 aruduino가 연결된 com 포트를 확인하고 입력
# 상기의 코드는 pf(pyfirmata)에 있는 Arudino() 생성자를 통해 파라미터로 "COM6"를 사용하여 새로운 객체
# ard를 생성하는 것임
ard.get_pin('d:13:o') # ard 객체가 생성되면 get_pin() 메소드를 사용하여 디지털핀 13번을 출력으로 설정

while True:
    ard.digital[13].write(1)  #ard 객체에서 제공하는 digital[13].write()를 사용하여 선택된 13번 핀에 high(1)을 출력함
    time.sleep(2)
    ard.digital[13].write(0)
    time.sleep(2)

# 상기의 while True: 문은 arudino sketch에서 loop() 함수와 마찬가지로 예제에서와 같이 4개의 문장을 무한 반복 수행하는 기능임