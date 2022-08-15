from cProfile import label
import sys

import csv
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

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

        
        label_stylesheet = """
            QWidget {
                font: italic 20px;
                padding-left: 0px;
                padding-right: 5px;
                padding-bottom: 10px;
            }
        """

        
        # Main Page Heading
        self.page_1_heading = QLabel("Select Testing Model",self)
        self.page_1_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_1_heading.setStyleSheet("""
            QWidget {
                color: red;
                font: bold 30px;
                padding: 20px;
            }
        """)
        layout.addWidget(self.page_1_heading, 0, 0, 3, 5)

        
        self.checkBox_t1 = QCheckBox(self)
        self.checkBox_t1.stateChanged.connect(self.checkedc)
        self.checkBox_t1.setText("Confined (Thesis)")
        self.checkBox_t1.setStyleSheet(label_stylesheet)

        layout.addWidget(self.checkBox_t1, 3, 0, 2, 5)
        
        self.checkBox_t2 = QCheckBox(self)
        self.checkBox_t2.stateChanged.connect(self.checkedc)
        self.checkBox_t2.setText("Confined (Wellborn storage; numerical)")
        self.checkBox_t2.setStyleSheet(label_stylesheet)
        layout.addWidget(self.checkBox_t2, 4, 0, 2, 5)
        
        self.checkBox_t3 = QCheckBox(self)
        self.checkBox_t3.stateChanged.connect(self.checkedc)
        self.checkBox_t3.setText("Leaky (Hantush and Jacob)")
        self.checkBox_t3.setStyleSheet(label_stylesheet)
        layout.addWidget(self.checkBox_t3, 5, 0, 2, 5)
        
        self.checkBox_t4 = QCheckBox(self)
        self.checkBox_t4.stateChanged.connect(self.checkedc)
        self.checkBox_t4.setText("Leaky (Hantush, 1960; short-term; aquitard storage)")
        self.checkBox_t4.setStyleSheet(label_stylesheet)
        layout.addWidget(self.checkBox_t4, 6, 0, 2, 5)
        
        self.checkBox_t5 = QCheckBox(self)
        self.checkBox_t5.stateChanged.connect(self.checkedc)
        self.checkBox_t5.setText("Unconfined (Thesis, using Sy)")
        self.checkBox_t5.setStyleSheet(label_stylesheet)
        layout.addWidget(self.checkBox_t5, 7, 0, 2, 5)
        
        self.checkBox_t6 = QCheckBox(self)
        self.checkBox_t6.stateChanged.connect(self.checkedc)
        self.checkBox_t6.setText("Unconfined (Dupuit; wellborn storage; numerical)")
        self.checkBox_t6.setStyleSheet(label_stylesheet)
        layout.addWidget(self.checkBox_t6, 8, 0, 2, 5)

        self.setLayout(layout)

        

        self.last = QPushButton(text="last page", parent=self)
        self.last.clicked.connect(self.lastpage)
        self.last.setStyleSheet("""
        """)
        layout.addWidget(self.last, 11, 0, 2, 2)

        self.next = QPushButton(text="next page", parent=self)
        self.next.clicked.connect(self.nextpage)
        self.next.setStyleSheet("""
        """)   
        layout.addWidget(self.next, 11, 3, 2, 2)

    def checkedc(self,checked):
        self.langs['c'] = checked
    def nextpage(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)  
    def lastpage(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)  


class Screen3(QWidget):
    def __init__(self, fileName, parent = None):
        super(Screen3, self).__init__(parent)
        self.setWindowTitle("Aquifer Test")
        

        self.page_1_heading = QLabel("<h1> Screen 3 </h1>",self)

        wellRadiusLayout = QHBoxLayout()
        self.well_radius = QLabel("<h3> Well Radius </h3>")
        wellRadiusLayout.addWidget(self.well_radius)
        self.well_radius_input = QLineEdit(self)
        wellRadiusLayout.addWidget(self.well_radius_input)

        pumpingRateLayout = QHBoxLayout()
        self.pumping_rate = QLabel("<h3> Pumping Rate </h3>")
        pumpingRateLayout.addWidget(self.pumping_rate)
        self.pumping_rate_input = QLineEdit(self)
        pumpingRateLayout.addWidget(self.pumping_rate_input)

        self.fileName = fileName
        self.model = QStandardItemModel(self)

        self.tableView = QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.pushButtonLoad = QPushButton(self)
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)

        self.pushButtonWrite = QPushButton(self)
        self.pushButtonWrite.setText("Write Csv File!")
        self.pushButtonWrite.clicked.connect(self.on_pushButtonWrite_clicked)

        self.layoutVertical = QVBoxLayout(self)
        self.layoutVertical.addWidget(self.page_1_heading)
        self.layoutVertical.addLayout(wellRadiusLayout)
        self.layoutVertical.addLayout(pumpingRateLayout)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)
        self.layoutVertical.addWidget(self.pushButtonWrite)
        

    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def writeCsv(self, fileName):
        with open(fileName, "w") as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber, columnNumber),
                        Qt.ItemDataRole.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)

    @pyqtSlot()
    def on_pushButtonWrite_clicked(self):
        self.writeCsv(self.fileName)

    @pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        self.loadCsv(self.fileName)


app = QApplication(sys.argv)

window = MainWindow()
screen2 = Screen2()
screen3 = Screen3("data.csv")

widget = QStackedWidget()
widget.addWidget(window)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.show()
app.exec()

