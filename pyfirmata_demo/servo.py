import pyfirmata
# 상기와 같이 pyfirmata를 import하면 소스코드에서 pyfirmata 패키지 이름을 다 작성해야 함
# import pyfirmata as pf 로 하면 소스코드에서 pf로 간단히 패키지를 호출할 수 있음
DELAY = 1
MIN = 5
MAX = 175
MID = 90

board = pyfirmata.Arduino('COM6')
servo = board.get_pin('d:11:s') # 11번핀을 서보모터 신호선으로 설정

def move_servo(v):                  # 파이선 함수 정의
    servo.write(v)
    board.pass_time(DELAY)

move_servo(MIN)                     # 위에서 정의된 함수를 호출
move_servo(MAX)
move_servo(MID)
move_servo(MIN)
move_servo(MAX)

board.exit()                       # 수행종료