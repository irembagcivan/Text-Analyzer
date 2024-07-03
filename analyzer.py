from PyQt5 import QtWidgets
from interface import Ui_MainWindow

class Analyzer_interface(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()