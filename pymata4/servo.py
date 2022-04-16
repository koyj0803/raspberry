import sys
import time
from pymata4 import pymata4

"""
This example will set a servo to 0, 90 and 180 degree positions.
"""

def servo(my_board, pin):
    """
    Set a pin to servo mode and then adjust its position.
    :param my_board: pymata4
    :param pin: pin to be controlled
    """
    # set the pin mode
    my_board.set_pin_mode_servo(pin)
    # set the servo to 0 degrees
    my_board.servo_write(pin, 0)
    time.sleep(1)
    # set the servo to 90 degrees
    my_board.servo_write(pin, 90)
    time.sleep(1)
    # set the servo to 180 degrees
    my_board.servo_write(pin, 180)
    time.sleep(1)
    my_board.servo_write(pin,120)
    time.sleep(1)
    my_board.servo_write(pin,30)

board = pymata4.Pymata4()
try:
    servo(board, 11)
except KeyboardInterrupt:
    board.shutdown()
    sys.exit(0)
