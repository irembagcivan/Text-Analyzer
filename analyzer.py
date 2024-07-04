from PyQt5 import QtWidgets
from collections import Counter
from interface import Ui_MainWindow
import re

class Analyzer_interface(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button interaction
        self.pushButton_analysis.clicked.connect(self.analyze_text)
        self.pushButton_search.clicked.connect(self.search_word)
    
    def analyze_text(self):
        text = self.textEdit.toPlainText()

        if not text.strip():
            self.label.setText("The text is empty. Please enter some text!!!")
            self.label_words.setText("Total number of words in the text: 0")
            self.label_most.setText("The most repeated word in the text: None")
            self.label_least.setText("The least repeated word in the text: None")
            return
        
        # Convert to lowercase and remove punctuation
        words = re.findall(r'\b\w+\b', text.lower())

        # Filter out common conjunctions
        common_conjunctions = {"and", "or", "but", "so", "yet", "for", "nor", "a", "an", "the", "in", "on", "at", "by", "with", "about",\
                                "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up",\
                                      "down", "out", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why",\
                                          "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only",\
                                              "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}
        
        filtered_words = []
        for word in words:
            if word not in common_conjunctions:
                filtered_words.append(word)
                
        words_count = len(filtered_words)

        if words_count > 0:
            total_words = words_count
            self.label_words.setText(f"Total number of words in the text: {total_words}")

            most_repeated_word = Counter(words).most_common(1)[0]
            self.label_most.setText(f"The most repeated word in the text: {most_repeated_word[0]} ({most_repeated_word[1]} times)")

            least_repeated_word = Counter(words).most_common()[-1]
            self.label_least.setText(f"The least repeated word in the text: {least_repeated_word[0]} ({least_repeated_word[1]} times)")


    def search_word(self):
        text = self.textEdit.toPlainText()

        if not text.strip():
            self.label.setText("The text is empty. Please enter some text!!!")
            return
        
        search_word = self.lineEdit_search_word.text().lower()
        words = re.findall(r'\b\w+\b', text.lower())
        word_count = words.count(search_word)
        self.label.setText(f"'{search_word}' found {word_count} times in the text")


