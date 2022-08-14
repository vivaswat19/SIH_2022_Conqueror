import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.page_1()
        


    def page_1(self):
        self.setWindowTitle("Aquifer Test")
        self.showMaximized()
        self.page_1_heading = QLabel("Hydraulic Properties", self)
        self.show()



app = QApplication(sys.argv)
window = MainWindow()
app.exec()