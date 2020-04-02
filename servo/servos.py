from machine import Timer,PWM
from board import board_info
from fpioa_manager import fm
import time

class Servos:
    Servo_Open_Degree = -90
    Servo_Close_Degree = 0
    def __init__(self,channel, pin, id=Timer.TIMER0):
        self.tim = Timer(id, channel, mode=Timer.MODE_PWM)
        self.ch  = PWM(self.tim, freq=50, duty=0, pin=pin)

    def setting_degree(self, func ,angle):
        if func == True :
            self.Servo_Open_Degree = angle
        else :
            self.Servo_Close_Degree = angle

    # 舵机转动范围：-90 ~ 90
    def set(self,angle):
        self.ch.duty((angle+90)/180*10+2.5)
        time.sleep(1)

    # 舵机打开角度，垃圾桶打开
    def open(self):
        self.set(self.Servo_Open_Degree)
        time.sleep(1)

    # 舵机关闭角度，垃圾桶关闭
    def close(self):
        self.set(self.Servo_Close_Degree)
        time.sleep(1)
