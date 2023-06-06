import time

from PyQt6.QtCore import QTimerEvent
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
import sys

from PyQt6.uic.uiparser import QtGui
from PyQt6.uic.properties import QtGui

# 문장 리스트
text = [
  '고양이는 야옹',
  '오렌지는 불주먹',
  '꿀주먹은 허니파워'
  ]

# 타이핑치는 효과
def typing_Ani(text, speed):
  string = text;
  for letter in string:
    time.sleep(speed)
    sys.stdout.write(letter)
    sys.stdout.flush()
  print("")


class window_class(QMainWindow):
    def __init__(self):
        from PyQt6.uic import loadUi
        super(window_class, self).__init__()
        loadUi('mini_game.ui', self)

    def mousePressEvent(self, e):

        position_x = e.position().x()
        position_y = e.position().y()
        print(position_x)
        print(position_y)

        wrong_check_x = 137
        wrong_check_y = 322

        label1 = QLabel('First Label', self)
        label1.move(int(position_x), int(position_y))

        if (wrong_check_x - 50) < position_x < (wrong_check_x + 50) \
                and (wrong_check_y - 10) < position_y < (wrong_check_y + 10):
            is_yn = "Y"
            label1.setPixmap(QPixmap("O.png"))
            # self.origin_photo = False
        else:

            # self.label.setPixmap(QtGui.QPixmap("x.png"))
            label1.setPixmap(QPixmap("x.png"))
            is_yn = "N"

        label1.setScaledContents(True)
        label1.show()
        print(is_yn)
        if is_yn=="N":

            self.timerEvent(QTimerEvent(1000))
            label1.hide()

app = QApplication(sys.argv)
window = window_class()
window.show()
app.exec()
