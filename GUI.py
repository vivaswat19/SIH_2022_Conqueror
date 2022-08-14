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
        self.aqfr_hydr_cond_input = QLineEdit(self)
        layout.addWidget(self.aqfr_hydr_cond, 1, 0, 1, 3)
        layout.addWidget(self.aqfr_hydr_cond_input, 1,3,1,2)

        self.aqfr_spec_storage = QLabel("<h3>Aquifer Specific Storage</h3>")
        self.aqfr_spec_storage_input = QLineEdit(self)
        layout.addWidget(self.aqfr_spec_storage, 2, 0, 1, 3)
        layout.addWidget(self.aqfr_spec_storage_input, 2, 3, 1, 2)
        
        self.aqfr_spec_yield = QLabel("<h3>Aquifer Specific Yield</h3>")
        self.aqfr_spec_yield_input = QLineEdit(self)
        layout.addWidget(self.aqfr_spec_yield, 3, 0, 1, 3)
        layout.addWidget(self.aqfr_spec_yield_input, 3, 3, 1, 2)
        
        self.aqfr_thickness = QLabel("<h3>Aquifer Thickness</h3>")
        self.aqfr_thickness_input = QLineEdit(self)
        layout.addWidget(self.aqfr_thickness, 4, 0, 1, 3)
        layout.addWidget(self.aqfr_thickness_input, 4, 3, 1, 2)
        
        self.aqfrd_thickness = QLabel("<h3>Aquitard Thickness</h3>")
        self.aqfrd_thickness_input = QLineEdit(self)
        layout.addWidget(self.aqfrd_thickness, 5, 0, 1, 3)
        layout.addWidget(self.aqfrd_thickness_input, 5, 3, 1, 2)
        
        self.aqfrd_vert_cond= QLabel("<h3>Aquitard Vertical conductivity</h3>")
        self.aqfrd_vert_cond_input= QLineEdit(self)
        layout.addWidget(self.aqfrd_vert_cond, 6, 0, 1, 3)
        layout.addWidget(self.aqfrd_vert_cond_input, 6, 3, 1, 2)
        
        self.aqfrd_spec_storage = QLabel("<h3>Aquitard Specific storage</h3>")
        self.aqfrd_spec_storage_input = QLineEdit(self)
        layout.addWidget(self.aqfrd_spec_storage, 7, 0, 1, 3)
        layout.addWidget(self.aqfrd_spec_storage_input, 7, 3, 1, 2)

        self.update_btn = QPushButton(text="Update", parent=self)
        layout.addWidget(self.update_btn, 8, 0, 1, 2)

        self.save_btn = QPushButton(text="Save", parent=self)
        self.save_btn.clicked.connect(self.next)   
        layout.addWidget(self.save_btn, 8, 3, 1, 2)

        self.setLayout(layout)

    def next(self):
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