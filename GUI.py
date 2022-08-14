from cProfile import label
import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        label_stylesheet = """
            QWidget {
                font: italic 20px;
                padding-left: 0px;
                padding-right: 5px;
                padding-bottom: 10px;
            }
        """

        self.setWindowTitle("Aquifer Test")

        # Main Page Heading
        self.page_1_heading = QLabel("Hydraulic Properties",self)
        self.page_1_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_1_heading.setStyleSheet("""
            QWidget {
                color: red;
                font: bold 30px;
                padding: 20px;
            }
        """)
        layout.addWidget(self.page_1_heading, 0, 0, 1, 5)

        # Aquifer Hydraulic Conductivity Widget
        self.aqfr_hydr_cond = QLabel("Aquifer Hydraulic Conductivity")
        self.aqfr_hydr_cond_input = QLineEdit(self)
        self.aqfr_hydr_cond.setStyleSheet(label_stylesheet)

        layout.addWidget(self.aqfr_hydr_cond, 1, 0, 1, 3)
        layout.addWidget(self.aqfr_hydr_cond_input, 1,3,1,2)

        self.aqfr_spec_storage = QLabel("Aquifer Specific Storage")
        self.aqfr_spec_storage_input = QLineEdit(self)
        self.aqfr_spec_storage.setStyleSheet(label_stylesheet)
        layout.addWidget(self.aqfr_spec_storage, 2, 0, 1, 3)
        layout.addWidget(self.aqfr_spec_storage_input, 2, 3, 1, 2)
        
        self.aqfr_spec_yield = QLabel("Aquifer Specific Yield")
        self.aqfr_spec_yield_input = QLineEdit(self)
        self.aqfr_spec_yield.setStyleSheet(label_stylesheet)
        layout.addWidget(self.aqfr_spec_yield, 3, 0, 1, 3)
        layout.addWidget(self.aqfr_spec_yield_input, 3, 3, 1, 2)
        
        self.aqfr_thickness = QLabel("Aquifer Thickness")
        self.aqfr_thickness_input = QLineEdit(self)
        self.aqfr_thickness.setStyleSheet(label_stylesheet)
        layout.addWidget(self.aqfr_thickness, 4, 0, 1, 3)
        layout.addWidget(self.aqfr_thickness_input, 4, 3, 1, 2)
        
        self.aqfrd_thickness = QLabel("Aquitard Thickness")
        self.aqfrd_thickness_input = QLineEdit(self)
        self.aqfrd_thickness.setStyleSheet(label_stylesheet)
        layout.addWidget(self.aqfrd_thickness, 5, 0, 1, 3)
        layout.addWidget(self.aqfrd_thickness_input, 5, 3, 1, 2)
        
        self.aqfrd_vert_cond= QLabel("Aquitard Vertical conductivity")
        self.aqfrd_vert_cond_input= QLineEdit(self)
        self.aqfrd_vert_cond.setStyleSheet(label_stylesheet)
        layout.addWidget(self.aqfrd_vert_cond, 6, 0, 1, 3)
        layout.addWidget(self.aqfrd_vert_cond_input, 6, 3, 1, 2)
        
        self.aqfrd_spec_storage = QLabel("Aquitard Specific storage")
        self.aqfrd_spec_storage_input = QLineEdit(self)
        self.aqfrd_spec_storage.setStyleSheet(label_stylesheet)
        layout.addWidget(self.aqfrd_spec_storage, 7, 0, 1, 3)
        layout.addWidget(self.aqfrd_spec_storage_input, 7, 3, 1, 2)

        self.update_btn = QPushButton(text="Update", parent=self)
        self.update_btn.setStyleSheet("""
        """)
        layout.addWidget(self.update_btn, 8, 0, 1, 2)

        self.save_btn = QPushButton(text="Save", parent=self)
        self.save_btn.clicked.connect(self.next)
        self.save_btn.setStyleSheet("""
        """)   
        layout.addWidget(self.save_btn, 8, 3, 1, 2)

        self.setLayout(layout)

    def next(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)       

class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.langs ={'T1':False, 'T2':False, 'T3':False, 'T4':False,'T5':False,'T6':False}
        self.setWindowTitle("Pumping test Model")

        layout = QGridLayout()
        self.page_1_heading = QLabel("<h1>Select Testing Model</h1>",self)
        layout.addWidget(self.page_1_heading, 0, 0, 1, 20)

        
        self.checkBox_t1 = QCheckBox(self)
        self.checkBox_t1.stateChanged.connect(self.checkedc)
        self.checkBox_t1.setText("Confined (Thesis)")
        self.checkBox_t1.setStyleSheet("""
            QWidget {
                font-size: 19px;
            }
        """)

        layout.addWidget(self.checkBox_t1, 1, 1, 1, 5)
        
        self.checkBox_t2 = QCheckBox(self)
        self.checkBox_t2.stateChanged.connect(self.checkedc)
        self.checkBox_t2.setText("Confined (Thesis)")
        self.checkBox_t2.setStyleSheet("""
            QWidget {
                font-size: 19px;
            }
        """)
        layout.addWidget(self.checkBox_t2, 2, 1, 1, 5)
        
        self.checkBox_t3 = QCheckBox(self)
        self.checkBox_t3.stateChanged.connect(self.checkedc)
        self.checkBox_t3.setText("Confined (Thesis)")
        self.checkBox_t3.setStyleSheet("""
            QWidget {
                font-size: 19px;
            }
        """)
        layout.addWidget(self.checkBox_t3, 3, 1, 1, 5)
        
        self.checkBox_t4 = QCheckBox(self)
        self.checkBox_t4.stateChanged.connect(self.checkedc)
        self.checkBox_t4.setText("Confined (Thesis)")
        self.checkBox_t4.setStyleSheet("""
            QWidget {
                font-size: 19px;
            }
        """)
        layout.addWidget(self.checkBox_t4, 4, 1, 1, 5)
        
        self.checkBox_t5 = QCheckBox(self)
        self.checkBox_t5.stateChanged.connect(self.checkedc)
        self.checkBox_t5.setText("Confined (Thesis)")
        self.checkBox_t5.setStyleSheet("""
            QWidget {
                font-size: 19px;
            }
        """)
        layout.addWidget(self.checkBox_t5, 5, 1, 1, 5)
        
        self.checkBox_t6 = QCheckBox(self)
        self.checkBox_t6.stateChanged.connect(self.checkedc)
        self.checkBox_t6.setText("Confined (Thesis)")
        self.checkBox_t6.setStyleSheet("""
            QWidget {
                font-size: 19px;
            }
        """)
        layout.addWidget(self.checkBox_t6, 6, 1, 1, 5)

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