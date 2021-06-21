import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# Импортируем наш интерфейс из файла
from my_gui.py import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # События нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.my_function)
    
    # Функция которая выполняется при нажатии на кнопку
    def my_function(self):


if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        myapp = MyWin()
        myapp.show()
        sys.exit(app.exec_())
