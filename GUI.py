import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aquifer Test")
        layout = QGridLayout()

        self.page_1_heading = QLabel("<h1>Hydraulic Properties</h1>",self)
        layout.addWidget(self.page_1_heading, 0, 0, 1, 5)

        self.aqfr_hydr_cond = QLabel("<h3>Aquifer Hydraulic Conductivity</h3>")
        layout.addWidget(self.aqfr_hydr_cond, 1, 0, 1, 2)

        self.button = QPushButton(text="Click", parent=self)
        self.button.clicked.connect(self.gotopage2)   
        layout.addWidget(self.button, 3, 0, 1, 2)

        self.setLayout(layout)

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