import sys

import csv
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class Screen1(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
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
                font: bold 30px;
                padding: 20px;
                max-height: 50px;
            }
        """)
        layout.addWidget(self.page_1_heading)

        # Aquifer Hydraulic Conductivity Widget
        self.aqfr_hydr_cond = QLabel("Aquifer Hydraulic Conductivity")
        self.aqfr_hydr_cond_input = QLineEdit(self)
        self.aqfr_hydr_cond_input.setPlaceholderText("0")
        self.aqfr_hydr_cond.setStyleSheet(label_stylesheet)

        # placing Aquifer Hydraulic Conductivity Widget on Screen
        aqfr_hydr_cond_row = QHBoxLayout() 
        aqfr_hydr_cond_row.addWidget(self.aqfr_hydr_cond)
        aqfr_hydr_cond_row.addWidget(self.aqfr_hydr_cond_input)
        layout.addLayout(aqfr_hydr_cond_row)


        self.aqfr_spec_storage = QLabel("Aquifer Specific Storage")
        self.aqfr_spec_storage_input = QLineEdit(self)
        self.aqfr_spec_storage.setStyleSheet(label_stylesheet)
        aqfr_spec_storage_row= QHBoxLayout()
        aqfr_spec_storage_row.addWidget(self.aqfr_spec_storage)
        aqfr_spec_storage_row.addWidget(self.aqfr_spec_storage_input)
        layout.addLayout(aqfr_spec_storage_row)


        self.aqfr_spec_yield = QLabel("Aquifer Specific Yield")
        self.aqfr_spec_yield_input = QLineEdit(self)
        self.aqfr_spec_yield.setStyleSheet(label_stylesheet)
        
        aqfr_spec_yield_row = QHBoxLayout()
        aqfr_spec_yield_row.addWidget(self.aqfr_spec_yield)
        aqfr_spec_yield_row.addWidget(self.aqfr_spec_yield_input)
        layout.addLayout(aqfr_spec_yield_row)

        self.aqfr_thickness = QLabel("Aquifer Thickness")
        self.aqfr_thickness_input = QLineEdit(self)
        self.aqfr_thickness.setStyleSheet(label_stylesheet)

        aqfr_thickness_row = QHBoxLayout()
        aqfr_thickness_row.addWidget(self.aqfr_thickness)
        aqfr_thickness_row.addWidget(self.aqfr_thickness_input)
        layout.addLayout(aqfr_thickness_row)

        self.aqfrd_thickness = QLabel("Aquitard Thickness")
        self.aqfrd_thickness_input = QLineEdit(self)
        self.aqfrd_thickness.setStyleSheet(label_stylesheet)
        aqfrd_thickness_row = QHBoxLayout()
        aqfrd_thickness_row.addWidget(self.aqfrd_thickness)
        aqfrd_thickness_row.addWidget(self.aqfrd_thickness_input)
        layout.addLayout(aqfrd_thickness_row)
        
        self.aqfrd_vert_cond= QLabel("Aquitard Vertical conductivity")
        self.aqfrd_vert_cond_input= QLineEdit(self)
        self.aqfrd_vert_cond.setStyleSheet(label_stylesheet)

        aqfrd_vert_cond_row = QHBoxLayout()
        aqfrd_vert_cond_row.addWidget(self.aqfrd_vert_cond)
        aqfrd_vert_cond_row.addWidget(self.aqfrd_vert_cond_input)
        layout.addLayout(aqfrd_vert_cond_row)
        
        self.aqfrd_spec_storage = QLabel("Aquitard Specific storage")
        self.aqfrd_spec_storage_input = QLineEdit(self)
        self.aqfrd_spec_storage.setStyleSheet(label_stylesheet)

        aqfrd_spec_storage_row = QHBoxLayout()
        aqfrd_spec_storage_row.addWidget(self.aqfrd_spec_storage)
        aqfrd_spec_storage_row.addWidget(self.aqfrd_spec_storage_input)
        layout.addLayout(aqfrd_spec_storage_row)


        button_row_layout = QHBoxLayout()
        self.update_btn = QPushButton(text="Update", parent=self)
        self.update_btn.setStyleSheet("""
        """)
        button_row_layout.addWidget(self.update_btn)

        self.save_btn = QPushButton(text="Save", parent=self)
        self.save_btn.clicked.connect(self.next)
        self.save_btn.setStyleSheet("""
        """)   
        button_row_layout.addWidget(self.save_btn)
        layout.addLayout(button_row_layout)

        self.setLayout(layout)

    def next(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)       

class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.langs ={'T1':False, 'T2':False, 'T3':False, 'T4':False,'T5':False,'T6':False}
        self.setWindowTitle("Pumping test Model")

        layout = QVBoxLayout(self)

        
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
                font: bold 30px;
                padding: 20px;
                max-height: 50px;
            }
        """)
        layout.addWidget(self.page_1_heading)


        
        self.checkBox_t1 = QCheckBox(self)
        self.checkBox_t1.setText("Confined (Thesis)")
        self.checkBox_t1.setStyleSheet(label_stylesheet)

        
        checkbox_row1 = QHBoxLayout() 
        checkbox_row1.addWidget(self.checkBox_t1)
        layout.addLayout(checkbox_row1)
        
        self.checkBox_t2 = QCheckBox(self)
        self.checkBox_t2.setText("Confined (Wellborn storage; numerical)")
        self.checkBox_t2.setStyleSheet(label_stylesheet)
        checkbox_row2 = QHBoxLayout() 
        checkbox_row2.addWidget(self.checkBox_t2)
        layout.addLayout(checkbox_row2)
        
        self.checkBox_t3 = QCheckBox(self)
        self.checkBox_t3.setText("Leaky (Hantush and Jacob)")
        self.checkBox_t3.setStyleSheet(label_stylesheet)
        checkbox_row3 = QHBoxLayout() 
        checkbox_row3.addWidget(self.checkBox_t3)
        layout.addLayout(checkbox_row3)
        
        self.checkBox_t4 = QCheckBox(self)
        self.checkBox_t4.setText("Leaky (Hantush, 1960; short-term; aquitard storage)")
        self.checkBox_t4.setStyleSheet(label_stylesheet)
        checkbox_row4 = QHBoxLayout() 
        checkbox_row4.addWidget(self.checkBox_t4)
        layout.addLayout(checkbox_row4)
        
        self.checkBox_t5 = QCheckBox(self)
        self.checkBox_t5.setText("Unconfined (Thesis, using Sy)")
        self.checkBox_t5.setStyleSheet(label_stylesheet)
        checkbox_row5 = QHBoxLayout() 
        checkbox_row5.addWidget(self.checkBox_t5)
        layout.addLayout(checkbox_row5)
        
        self.checkBox_t6 = QCheckBox(self)
        self.checkBox_t6.setText("Unconfined (Dupuit; wellborn storage; numerical)")
        self.checkBox_t6.setStyleSheet(label_stylesheet)
        checkbox_row6 = QHBoxLayout() 
        checkbox_row6.addWidget(self.checkBox_t6)
        layout.addLayout(checkbox_row6)

        button_row_layout = QHBoxLayout()

        self.last = QPushButton(text="last page", parent=self)
        self.last.clicked.connect(self.lastpage)
        self.last.setStyleSheet("""
        """)

        button_row_layout.addWidget(self.last)

        self.next = QPushButton(text="next page", parent=self)
        self.next.clicked.connect(self.nextpage)
        self.next.setStyleSheet("""
        """)   
        
        button_row_layout.addWidget(self.next)
        layout.addLayout(button_row_layout)

        self.setLayout(layout)

    def nextpage(self):
        self.langs["T1"] = self.checkBox_t1.isChecked()
        self.langs["T2"] = self.checkBox_t2.isChecked()
        self.langs["T3"] = self.checkBox_t3.isChecked()
        self.langs["T4"] = self.checkBox_t4.isChecked()
        self.langs["T5"] = self.checkBox_t5.isChecked()
        self.langs["T6"] = self.checkBox_t6.isChecked()
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
screen1 = Screen1()
screen2 = Screen2()
screen3 = Screen3("data.csv")

widget = QStackedWidget()
widget.setStyleSheet("""
    background-color: white;
    color: black;
""")

widget.addWidget(screen1)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.show()
app.exec()

