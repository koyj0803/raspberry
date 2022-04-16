import speech_recognition as sr  # 패키지 명은 SpeechRecogniton이지만 import 명은 speech_recognition임
import pyfirmata
from pymata4 import pymata4
import time, sys
DELAY = 1
MIN = 5
MAX = 175
MID = 90
board = pymata4.Pymata4()
#board = pyfirmata.Arduino('COM6')
servo = board.set_pin_mode_servo(11) # 11번핀을 서보모터 신호선으로 설정


def move_servo(v):                  # 파이선 함수 정의
    board.servo_write(11,0)
    time.sleep(1)
    board.servo_write(11, v)
    time.sleep(1) 
    
# Record Audio
r = sr.Recognizer()  # sr 패키지의 생성자 Recognizer()를 사용하여 음성인식을 위한 객체 r 을 생성함
with sr.Microphone() as source:     # with as 구문을 사용하여 sr의 Microphone() 메소드를 사용하여 source 객제를 생성
    print("Say something!")         # with as 구문을 사용하면 source를 사용한 후 별도로 close() 할 필요가 없음
    audio = r.listen(source)        # 생성된 음성인식 객체 r에서 제공하는 listen() 메소드에 마이크로 지정된 source(with as 구문)를 파라미터로 입력함
                                    # r.listen()은 audio라는 출력(r.recognize_google()에서 사용될 오디오파일을 생성함
# Speech recognition using Google Speech Recognition
# move_servo(0)
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
    print(text)
    if text.find("right") != -1:
        print("right is detected")
        move_servo(90)
        print("this right block is running\n")
        
        
    if text.find("left") != -1 or text.find('laughed') != -1:
        print("left is detected ")
        print("this left block is runnng\n")
        move_servo(180)
        #print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)    
    
    
