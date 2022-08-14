import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aquifer Test")
        self.page_1_heading = QLabel(self)
        self.page_1_heading.setText("Hydraulic Properties")
        self.page_1_heading.adjustSize()
        self.button = QPushButton(text="Click", parent=self)
        self.button.clicked.connect(self.gotopage2)        

    def gotopage2(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)       

class Screen2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("page2")
        self.page_1_heading = QLabel(self)
        self.page_1_heading.setText("Page 2")
        self.page_1_heading.adjustSize()

app = QApplication(sys.argv)
window = MainWindow()
screen2 = Screen2()
widget = QStackedWidget()
widget.addWidget(window)
widget.addWidget(screen2)
widget.show()
app.exec()