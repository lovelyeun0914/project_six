import functools
import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QWidget
from PyQt6.uic import loadUi

text1 = '웅성웅성\n떠들떠들'
text2 = '어 저기 앉아야 겠다'

# class TypingEffect(QWidget):
#     def __init__(self, input_text):
#         super().__init__()
#         self.label = QLabel(self)
#         self.text = input_text
#         self.current_index = 0
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_text)
#         self.timer.start(400)  #
#         print("11111")
#         print(self.label)
#
#     def update_text(self):
#         if self.current_index >= len(self.text):
#             self.timer.stop()
#             return
#         self.label.setText(self.text[: self.current_index + 1])
#         self.current_index += 1

class WindowClass(QMainWindow):
    def typing_eppect(self, input_text):
        self.text = input_text
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_text)
        self.timer.start(400)  #
    def update_text(self):
        if self.current_index >= len(self.text):
            self.timer.stop()
            return True
        # self.label_text.setStyleSheet('padding: 15px')
        self.label_text.setText(self.text[: self.current_index + 1])
        self.label_text.setFont(QFont('Arial', 36))
        self.current_index += 1


    def __init__(self):
        super().__init__()
        loadUi('./img/sin1_2.ui', self)
        # self.typing_eppect(text1)  # 출력할 텍스트 입력

        self.next1.mousePressEvent = self.stage1 #next_btn에 클릭이벤트추가

    def stage1(self, event):
        loadUi('./img/sin1.ui', self)  # mini_game2.ui 파일의 UI 로드하여 현재 창에 설정
        self.typing_eppect(text1)  # 출력할 텍스트 입력
        self.next1.mousePressEvent = self.stage1_text #next_btn에 클릭이벤트추가
    def stage1_text(self, event):
        self.typing_eppect(text2)  # 출력할 텍스트 입력


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowClass()
    window.show()
    sys.exit(app.exec())
