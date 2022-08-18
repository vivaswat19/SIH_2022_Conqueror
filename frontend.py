import imp
import sys

import csv
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from connector import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

payload = connector()

label_stylesheet = """
    QWidget {
        font: 20px;
        font-weight: 400;
        padding-left: 0px;
        padding-right: 5px;
        padding-bottom: 10px;
    }
"""

line_edit_stylesheet = """
    QLineEdit {
        text-align: center;
        font: italic 20px;
        min-width: 150px;
        max-width: 200px;
    }
"""

button_stylesheet = """
    QPushButton {
        font: bold 20px;
        min-width: 225;
        max-width: 250;
    }
"""

button_disabled_stylesheet = """
    QPushButton {
        font: bold 20px;
        min-width: 225;
        max-width: 250;
        background-color: rgb(69, 69, 69);
        color: white;
    }
"""

class Screen1(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pumping Test Desktop Application")
        layout = QVBoxLayout(self)

        # Main Page Heading
        self.page_1_heading = QLabel("Hydraulic Properties",self)
        self.page_1_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_1_heading.setStyleSheet("""
            QWidget {
                font: bold 40px;
                padding: 20px;
                max-height: 50px;
            }
        """)
        layout.addWidget(self.page_1_heading)

        # Aquifer Hydraulic Conductivity Widget
        self.aqfr_hydr_cond = QLabel("Aquifer Hydraulic Conductivity")
        self.aqfr_hydr_cond.setStyleSheet(label_stylesheet)

        # Aquifer Hydraulic Conductivity Input Widget
        self.aqfr_hydr_cond_input = QLineEdit(self)
        self.aqfr_hydr_cond_input.setPlaceholderText("0")
        self.aqfr_hydr_cond_input.setStyleSheet(line_edit_stylesheet)

        # placing Aquifer Hydraulic Conductivity Widget on Screen
        aqfr_hydr_cond_row = QHBoxLayout() 
        aqfr_hydr_cond_row.addWidget(self.aqfr_hydr_cond)
        aqfr_hydr_cond_row.addWidget(self.aqfr_hydr_cond_input)
        layout.addLayout(aqfr_hydr_cond_row)


        # Aquifer Specific Storage Widget
        self.aqfr_spec_storage = QLabel("Aquifer Specific Storage")
        self.aqfr_spec_storage.setStyleSheet(label_stylesheet)

        # Aquifer Specific Storage Input Widget
        self.aqfr_spec_storage_input = QLineEdit(self)
        self.aqfr_spec_storage_input.setPlaceholderText("0")
        self.aqfr_spec_storage_input.setStyleSheet(line_edit_stylesheet)

        # placing Aquifer Specific Storage Widget on Screen
        aqfr_spec_storage_row= QHBoxLayout()
        aqfr_spec_storage_row.addWidget(self.aqfr_spec_storage)
        aqfr_spec_storage_row.addWidget(self.aqfr_spec_storage_input)
        layout.addLayout(aqfr_spec_storage_row)


        # Aquifer Specific Yield Widget
        self.aqfr_spec_yield = QLabel("Aquifer Specific Yield")
        self.aqfr_spec_yield.setStyleSheet(label_stylesheet)

        # Aquifer Specific Yield Input Widget
        self.aqfr_spec_yield_input = QLineEdit(self)
        self.aqfr_spec_yield_input.setPlaceholderText("0")
        self.aqfr_spec_yield_input.setStyleSheet(line_edit_stylesheet)
        
        #Placing Aquifer Specific Yield Widget on Screen
        aqfr_spec_yield_row = QHBoxLayout()
        aqfr_spec_yield_row.addWidget(self.aqfr_spec_yield)
        aqfr_spec_yield_row.addWidget(self.aqfr_spec_yield_input)
        layout.addLayout(aqfr_spec_yield_row)


        # Aquifer Thickness Widget
        self.aqfr_thickness = QLabel("Aquifer Thickness")
        self.aqfr_thickness.setStyleSheet(label_stylesheet)
        
        # Aquifer Thickness Input Widget
        self.aqfr_thickness_input = QLineEdit(self)
        self.aqfr_thickness_input.setPlaceholderText("0")
        self.aqfr_thickness_input.setStyleSheet(line_edit_stylesheet)

        # Placing Aquifer thickenss widget on screen
        aqfr_thickness_row = QHBoxLayout()
        aqfr_thickness_row.addWidget(self.aqfr_thickness)
        aqfr_thickness_row.addWidget(self.aqfr_thickness_input)
        layout.addLayout(aqfr_thickness_row)


        # Aquitard Thickness Widget
        self.aqfrd_thickness = QLabel("Aquitard Thickness")
        self.aqfrd_thickness.setStyleSheet(label_stylesheet)
        
        # Aquitard Thickness Input Widget
        self.aqfrd_thickness_input = QLineEdit(self)
        self.aqfrd_thickness_input.setPlaceholderText("0")
        self.aqfrd_thickness_input.setStyleSheet(line_edit_stylesheet)

        # Placing Aquitard thickenss widget on screen
        aqfrd_thickness_row = QHBoxLayout()
        aqfrd_thickness_row.addWidget(self.aqfrd_thickness)
        aqfrd_thickness_row.addWidget(self.aqfrd_thickness_input)
        layout.addLayout(aqfrd_thickness_row)
        

        # Aquitard Thickness Widget
        self.aqfrd_vert_cond= QLabel("Aquitard Vertical conductivity")
        self.aqfrd_vert_cond.setStyleSheet(label_stylesheet)
        
        # Aquitard Thickness Input Widget
        self.aqfrd_vert_cond_input = QLineEdit(self)
        self.aqfrd_vert_cond_input.setPlaceholderText("0")
        self.aqfrd_vert_cond_input.setStyleSheet(line_edit_stylesheet)

        # Placing Aquitard thickenss widget on screen
        aqfrd_vert_cond_row = QHBoxLayout()
        aqfrd_vert_cond_row.addWidget(self.aqfrd_vert_cond)
        aqfrd_vert_cond_row.addWidget(self.aqfrd_vert_cond_input)
        layout.addLayout(aqfrd_vert_cond_row)
        

        # Aquitard Thickness Widget
        self.aqfrd_spec_storage = QLabel("Aquitard Specific storage")
        self.aqfrd_spec_storage.setStyleSheet(label_stylesheet)
        
        # Aquitard Thickness Input Widget
        self.aqfrd_spec_storage_input = QLineEdit(self)
        self.aqfrd_spec_storage_input.setPlaceholderText("0")
        self.aqfrd_spec_storage_input.setStyleSheet(line_edit_stylesheet)

        # Placing Aquitard thickenss widget on screen
        aqfrd_spec_storage_row = QHBoxLayout()
        aqfrd_spec_storage_row.addWidget(self.aqfrd_spec_storage)
        aqfrd_spec_storage_row.addWidget(self.aqfrd_spec_storage_input)
        layout.addLayout(aqfrd_spec_storage_row)

        # Update and Save Button Widget
        button_row_layout = QHBoxLayout()
        self.update_btn = QPushButton(text="Update", parent=self)
        self.update_btn.setStyleSheet(button_stylesheet)
        button_row_layout.addWidget(self.update_btn)

        self.save_btn = QPushButton(text="Save", parent=self)
        self.save_btn.setStyleSheet(button_stylesheet)
        self.save_btn.clicked.connect(self.next)
        button_row_layout.addWidget(self.save_btn)
        
        layout.addLayout(button_row_layout)
        self.setLayout(layout)

    def next(self):
        # collecting data from input box
        if(self.aqfr_hydr_cond_input.text() != ""):
            payload.K = self.aqfr_hydr_cond_input.text()
        if(self.aqfr_spec_storage_input.text() != ""):
            payload.Ss = self.aqfr_spec_storage_input.text()
        if(self.aqfr_spec_yield_input.text() != ""):
            payload.Sy = self.aqfr_spec_yield_input.text()
        if(self.aqfr_thickness_input.text() != ""):
            payload.b = self.aqfr_thickness_input.text()
        if(self.aqfrd_thickness_input.text() != ""):
            payload.bc = self.aqfrd_thickness_input.text()
        if(self.aqfrd_vert_cond_input.text() != ""):
            payload.Kc = self.aqfrd_vert_cond_input.text()
        if(self.aqfrd_spec_storage_input.text() != ""):
            payload.Ssc = self.aqfrd_spec_storage_input.text()

        widget.setCurrentIndex(widget.currentIndex() + 1)       

class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Pumping test Model")

        layout = QVBoxLayout(self)
        
        # Main Page Heading
        self.page_2_heading = QLabel("Select Testing Model",self)
        self.page_2_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_2_heading.setStyleSheet("""
            QWidget {
                font: bold 40px;
                padding: 20px;
                max-height: 50px;
            }
        """)
        layout.addWidget(self.page_2_heading)


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

        self.last = QPushButton(text="Previous Page", parent=self)
        self.last.clicked.connect(self.lastpage)
        self.last.setStyleSheet(button_stylesheet)

        button_row_layout.addWidget(self.last)

        self.next = QPushButton(text="Save", parent=self)
        self.next.clicked.connect(self.nextpage) 
        self.next.setStyleSheet(button_stylesheet)
        
        button_row_layout.addWidget(self.next)
        layout.addLayout(button_row_layout)

        self.setLayout(layout)

    def nextpage(self):
        payload.t1 = self.checkBox_t1.isChecked()
        payload.t2 = self.checkBox_t2.isChecked()
        payload.t3 = self.checkBox_t3.isChecked()
        payload.t4 = self.checkBox_t4.isChecked()
        payload.t5 = self.checkBox_t5.isChecked()
        payload.t6 = self.checkBox_t6.isChecked()
        widget.setCurrentIndex(widget.currentIndex() + 1)  
    def lastpage(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)  

class Screen3(QWidget):
    def __init__(self, parent = None):
        super(Screen3, self).__init__(parent)
        self.layoutVertical = QVBoxLayout()

        self.page_3_heading = QLabel("DrawDown Data")
        self.page_3_heading.setStyleSheet("""
            QWidget {
                font: bold 40px;
                padding: 20px;
                max-height: 50px;
            }
        """)
        self.page_3_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layoutVertical.addWidget(self.page_3_heading)


        wellRadiusLayout = QHBoxLayout()
        self.well_radius = QLabel("Well Radius")
        self.well_radius.setStyleSheet(label_stylesheet)
        wellRadiusLayout.addWidget(self.well_radius)
        self.well_radius_input = QLineEdit()
        self.well_radius_input.setStyleSheet(line_edit_stylesheet)
        wellRadiusLayout.addWidget(self.well_radius_input)

        
        pumpingRateLayout = QHBoxLayout()
        self.pumping_rate = QLabel("Pumping Rate")
        self.pumping_rate.setStyleSheet(label_stylesheet)
        pumpingRateLayout.addWidget(self.pumping_rate)
        self.pumping_rate_input = QLineEdit(self)
        self.pumping_rate_input.setStyleSheet(line_edit_stylesheet)
        pumpingRateLayout.addWidget(self.pumping_rate_input)

        
        self.model = QStandardItemModel()
        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        # self.tableView.horizontalHeader().setStretchLastSection(True)

        csvButtonLayout = QHBoxLayout()
        self.pushButtonLoad = QPushButton()
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.setStyleSheet(button_stylesheet)
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)
        
        self.pushButtonWrite = QPushButton()
        self.pushButtonWrite.setText("Update Csv File!")
        self.pushButtonWrite.setStyleSheet(button_disabled_stylesheet)
        self.pushButtonWrite.setDisabled(True)
        self.pushButtonWrite.clicked.connect(self.on_pushButtonWrite_clicked)
        csvButtonLayout.addWidget(self.pushButtonLoad)
        csvButtonLayout.addWidget(self.pushButtonWrite)

        page_change_ButtonLayout = QHBoxLayout()
        self.pushButtonPrev = QPushButton()
        self.pushButtonPrev.setText("Previous Page")
        self.pushButtonPrev.setStyleSheet(button_stylesheet)
        self.pushButtonPrev.clicked.connect(self.on_pushButtonlast_clicked)
        page_change_ButtonLayout.addWidget(self.pushButtonPrev)
        
        self.pushButtonEval = QPushButton()
        self.pushButtonEval.setText("Evaluate")
        self.pushButtonEval.setStyleSheet(button_stylesheet)
        self.pushButtonEval.clicked.connect(self.on_pushButtonnext_clicked)
        page_change_ButtonLayout.addWidget(self.pushButtonEval)

        self.layoutVertical.addLayout(wellRadiusLayout)
        self.layoutVertical.addLayout(pumpingRateLayout)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addLayout(csvButtonLayout)
        self.layoutVertical.addLayout(page_change_ButtonLayout)
        
        self.setLayout(self.layoutVertical)

    def getFile(self):
        try:
            fileName = QFileDialog.getOpenFileName(filter = "csv (*.csv)")[0]
            payload.filePath=fileName
            self.fileName = fileName
            self.loadCsv(fileName)
        except:
            print("Ok")

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

    def last(self):
        widget.setCurrentIndex(widget.currentIndex() - 1) 
    
    def next(self):
        if(self.well_radius_input.text() != ""):
            payload.r = self.well_radius_input.text()
        if(self.pumping_rate_input.text() != ""):
            payload.q = self.pumping_rate_input.text()
        payload.setValues()
        screen4.update_data_label()
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    @pyqtSlot()
    def on_pushButtonWrite_clicked(self):
        self.writeCsv(self.fileName)

    @pyqtSlot()
    def on_pushButtonLoad_clicked(self):
        self.getFile()
        self.pushButtonWrite.setDisabled(False)
        self.pushButtonWrite.setStyleSheet(button_stylesheet)

    @pyqtSlot()
    def on_pushButtonlast_clicked(self):
        self.last()

    @pyqtSlot()
    def on_pushButtonnext_clicked(self):
        self.next()


class Screen4(QWidget):
    def __init__(self, parent = None):
        super(Screen4, self).__init__(parent)

        layout = QHBoxLayout()
        data_container = QVBoxLayout()

        self.cb = QComboBox()
        self.cb.addItems(['a','b','c','d'])
        self.cb.currentIndexChanged.connect(self.selectionChange)
        data_container.addWidget(self.cb)

        self.s_output = QLabel()
        self.t_output = QLabel()
        data_container.addWidget(self.s_output)
        data_container.addWidget(self.t_output)


        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        layout.addWidget(self.canvas)
        layout.addLayout(data_container)

        self.setLayout(layout)

    def plot(self):
        data = [random.random() for i in range(10)]
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(data, '*-')
        self.canvas.draw()

    def update_data_label(self):
        (s,t) = payload.getValues()
        self.s_output.setText(str(s))
        self.t_output.setText(str(t))

    def selectionChange(self, index):
        print(index)



app = QApplication(sys.argv)
screen1 = Screen1()
screen2 = Screen2()
screen3 = Screen3()
screen4 = Screen4()

widget = QStackedWidget()
widget.setStyleSheet("""
    background-color: white;
    color: black;
""")
widget.setFixedSize(600,600)
widget.setWindowFlags(Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMinimizeButtonHint)

widget.addWidget(screen1)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.addWidget(screen4)
widget.show()
app.exec()
