import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic  # Импортируем uic git remote add user_a_at_b https://qwe-png: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/https://github.com/qwe-png/moskva-ksenofontov.git
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        r = 255
        g = 255
        b = 0
        tt = random.randint(1, 250)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(0, 0, tt, tt)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
