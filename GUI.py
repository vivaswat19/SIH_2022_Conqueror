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
        self.langs ={'T1':False, 'T2':False, 'T3':False, 'T4':False,'T5':False,'T6':False}
        self.setWindowTitle("Pumping test Model")

        layout = QGridLayout()
        self.page_1_heading = QLabel("<h1>Select Testing Model</h1>",self)
        layout.addWidget(self.page_1_heading, 0, 0, 1, 5)

        
        self.checkBox_t1 = QCheckBox(self)
        self.checkBox_t1.stateChanged.connect(self.checkedc)
        self.checkBox_t1.setText("T1")

        layout.addWidget(self.checkBox_t1, 1, 1, 1, -1)
        
        self.checkBox_t2 = QCheckBox(self)
        self.checkBox_t2.stateChanged.connect(self.checkedc)
        self.checkBox_t2.setText("T1")

        layout.addWidget(self.checkBox_t2, 2, 1, 1, -1)
        
        self.checkBox_t3 = QCheckBox(self)
        self.checkBox_t3.stateChanged.connect(self.checkedc)
        self.checkBox_t3.setText("T1")

        layout.addWidget(self.checkBox_t3, 3, 1, 1, -1)
        
        self.checkBox_t4 = QCheckBox(self)
        self.checkBox_t4.stateChanged.connect(self.checkedc)
        self.checkBox_t4.setText("T1")

        layout.addWidget(self.checkBox_t4, 4, 1, 1, -1)

        self.setLayout(layout)


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