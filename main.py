import sys
from PyQt5.QtWidgets import QApplication
from analyzer import Analyzer_interface

app = QApplication(sys.argv)
analyzer = Analyzer_interface()
analyzer.show()
sys.exit(app.exec_())
