# -*- coding:utf-8 -*-
import pigpio
from time import sleep
import pygame.mixer
pi = pigpio.pi()
pygame.mixer.init()

pi.set_mode(14, pigpio.OUTPUT)
pi.set_mode(15, pigpio.OUTPUT)
pi.set_mode(18, pigpio.OUTPUT)
pi.set_mode(23, pigpio.OUTPUT)
pi.set_mode(24, pigpio.OUTPUT)
pi.set_mode(25, pigpio.OUTPUT)
pi.set_mode(8, pigpio.OUTPUT)
pi.set_mode(7, pigpio.OUTPUT)

pi.set_mode(16, pigpio.INPUT)
pi.set_mode(17, pigpio.INPUT)
pi.set_mode(27, pigpio.INPUT)
pi.set_mode(22, pigpio.INPUT)
pi.set_mode(10, pigpio.INPUT)
pi.set_mode(9, pigpio.INPUT)
pi.set_mode(11, pigpio.INPUT)
pi.set_mode(20, pigpio.INPUT)
pi.set_mode(21, pigpio.INPUT)
pi.set_mode(13, pigpio.INPUT)

OUTPIN = [7, 8, 25, 24, 23, 18, 15, 14]
INPIN = [13, 21, 20, 11, 9, 10, 22, 27, 17, 16]


class Bord():
    def checkPlace(self):
        for o in OUTPIN:
            pi.write(o, 1)
            for i in INPIN:
                if pi.read(i):
                    pi.write(o, 0)
                    self.place = o, i
                    return True
            pi.write(o, 0)
        return False

    def point(self):
        if self.checkPlace():
            outer, inner = self.place

            # 9~10
            if outer == OUTPIN[0]:
                place = 0
                magnification = 3
            elif outer == OUTPIN[1]:
                place = 0
                magnification = 2
            elif outer == OUTPIN[2]:
                place = 0
                magnification = 1
            # BULL
            elif outer == OUTPIN[3]:
                place = 2
                magnification = 1
            # 15~14
            elif outer == OUTPIN[4]:
                place = 1
                magnification = 1
            elif outer == OUTPIN[5]:
                place = 1
                magnification = 2
            else:
                place = 1
                magnification = 3

            if inner == INPIN[0]:
                point = [14, 9, 50]
            elif inner == INPIN[1]:
                point = [11, 12, 25]
            elif inner == INPIN[2]:
                point = [8, 5]
            elif inner == INPIN[3]:
                point = [16, 20]
            elif inner == INPIN[4]:
                point = [15, 10]
            elif inner == INPIN[5]:
                point = [2, 6]
            elif inner == INPIN[6]:
                point = [17, 13]
            elif inner == INPIN[7]:
                point = [3, 4]
            elif inner == INPIN[8]:
                point = [19, 18]
            elif inner == INPIN[9]:
                point = [7, 1]

            self.playSound(point[place], magnification)

            print(point[place] * magnification)
            self.point_nomal = point[place] * magnification
            self.point_pass = point[place] * 10 + magnification
            return True
        return None

    def playSound(self, _point, _magnification):
        if _point == 25:
            pygame.mixer.music.load("bull.mp3")
            pygame.mixer.music.play(1)
            sleep(1)
        elif _point == 50:
            pygame.mixer.music.load("D-bull.mp3")
            pygame.mixer.music.play(1)
            sleep(1)
        elif _magnification == 1:
            pygame.mixer.music.load("single.mp3")
            pygame.mixer.music.play(1)
            sleep(1)
        elif _magnification == 2:
            pygame.mixer.music.load("double.mp3")
            pygame.mixer.music.play(1)
            sleep(1)
        elif _magnification == 3:
            pygame.mixer.music.load("triple.mp3")
            pygame.mixer.music.play(1)
            sleep(1)


if __name__ == '__main__':
    b = Bord()
    while 1:
        if b.point():
            print(b.point_pass)
        sleep(0.1)
