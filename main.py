import sys
from PyQt5.QtWidgets import QApplication
from analyzer import *

app = QApplication(sys.argv)
analyzer = Analyzer_interface()
sys.exit(app.exec_())
