import sys

from PyQt6.QtCore import *
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
        self.setHeight(1000)
        self.setWidth(1000)
        self.langs ={'c':False, 'cpp':False, 'java':False, 'python':False}
        self.setWindowTitle("Pumping test Model")
        self.page_1_heading = QLabel(self)
        self.page_1_heading.setText("Select Testing Model")
        self.page_1_heading.adjustSize()

        self.checkBox_c = QCheckBox(self)
        self.checkBox_c.setGeometry(QRect(170, 120, 81, 20))
        self.checkBox_c.stateChanged.connect(self.checkedc)
        self.checkBox_c.setText("C")

        # self.next = QPushButton(text="Next Page", parent=self)
        # self.next.clicked.connect(self.nextpage)  
        
        # self.last = QPushButton(text="Last Page", parent=self)
        # self.last.clicked.connect(self.lastpage)        

    def checkedc(self,checked):
        self.langs['c'] = checked
    def nextpage(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)  
    def lastpage(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)  

app = QApplication(sys.argv)
window = MainWindow()
screen2 = Screen2()
widget = QStackedWidget()
widget.addWidget(window)
widget.addWidget(screen2)
widget.show()
app.exec()