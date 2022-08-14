import sys

from PyQt6.QtCore import *
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

class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aquifer Test")
        layout = QGridLayout()

        self.page_1_heading = QLabel("<h1>Hydraulic Properties</h1>",self)
        layout.addWidget(self.page_1_heading, 0, 0, 1, 5)

        self.aqfr_hydr_cond = QLabel("<h3>Aquifer Hydraulic Conductivity</h3>")
        layout.addWidget(self.aqfr_hydr_cond, 1, 0, 1, 2)

        self.button = QPushButton(text="Click", parent=self)
        # self.button.clicked.connect(self.gotopage2)   
        layout.addWidget(self.button, 3, 0, 1, 2)

        self.setLayout(layout)



        # self.langs ={'c':False, 'cpp':False, 'java':False, 'python':False}
        # self.setWindowTitle("Pumping test Model")

        # layout = QGridLayout()
        # self.page_1_heading = QLabel("<h1>Select Testing Model</h1>",self)
        # layout.addWidget(self.page_1_heading, 0, 0, 1, 5)
        # self.page_1_heading.adjustSize()

        
        # self.checkBox_c = QCheckBox(self)
        # self.checkBox_c.stateChanged.connect(self.checkedc)
        # self.checkBox_c.setText("C")

        # layout.addWidget(self.page_1_heading, 1, 1, 1, 1)

        # self.setLayout(layout)


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