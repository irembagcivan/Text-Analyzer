from PyQt5 import QtWidgets
from collections import Counter
from interface import Ui_MainWindow

class Analyzer_interface(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button interaction
        self.pushButton_analysis.clicked.connect(self.analyze_text)
        self.pushButton_search.clicked.connect(self.search_word)
    
    def analyze_text(self):
        text = self.textEdit.toPlainText()
        words = text.split() # returns list
        words_count = len(words)

        if words_count > 0:
            total_words = words_count
            self.label_words.setText(f"Total number of words in the text: {total_words}")

            most_repeated_word = Counter(words).most_common(1)[0]
            self.label_most.setText(f"The most repeated word in the text: {most_repeated_word[0]} ({most_repeated_word[1]} times)")

            least_repeated_word = Counter(words).most_common()[-1]
            self.label_least.setText(f"The least repeated word in the text: {least_repeated_word[0]} ({least_repeated_word[1]} times)")

        else:
            self.label_words.setText(f"Total number of words in the text: 0")
            self.label_least.setText(f"The most repeated word in the text: None")
            self.label_most.setText(f"The least repeated word in the text: None")

    def search_word(self):
        text = self.textEdit.toPlainText()
        search_word = self.lineEdit_search_word.text()
        words = text.split()
        word_count = words.count(search_word)
        self.label.setText(f"'{search_word}' found {word_count} times in the text")


