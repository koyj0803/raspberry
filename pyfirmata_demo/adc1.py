import pyfirmata as pf
import time

ard = pf.Arduino('COM6')
print('connected.')

# 아날로그핀을 사용하려면 반드시 아래와 같은 두 줄이 필요함.

pf.util.Iterator(ard).start()

ard.analog[0].enable_reporting()

while True:
	a0 = ard.analog[0].read() # [0,1]범위의 실수 반환
	print(a0)