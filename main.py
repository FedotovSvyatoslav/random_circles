import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI import Ui_Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QMainWindow, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.do_paint = False

        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        x1, y1 = random.randint(10, 630), random.randint(10, 420)
        x2, y2 = random.randint(10, 630), random.randint(10, 420)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255),
                           random.randint(1, 255)))
        qp.drawEllipse(x1, y1, x2, y2)

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
