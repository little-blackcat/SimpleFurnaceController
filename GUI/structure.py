import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QSizePolicy, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from DatabaseManager import DatabaseManager

db = DatabaseManager("../Common/database.db")
'''
class SimpleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()

        layout.setColumnStretch(1, 5)
        layout.setColumnStretch(2, 5)
        layout.setColumnStretch(3, 5)

        self.minTemperatureL = QLabel("Temperatura uruchamiania grzałki: ", self)
        self.minTemperatureL.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureL = QLabel("Temperatura wyłączania grzałki: ", self)
        self.maxTemperatureL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.temperatureReadingFrequencyL = QLabel("Częstotliwość sczytywania temperatury:", self)
        self.temperatureReadingFrequencyL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.minTemperatureE = QSpinBox(self)
        self.minTemperatureE.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.minTemperatureE.setValue(db.selectMinTempFromConf())

        self.maxTemperatureE = QSpinBox(self)
        self.maxTemperatureE.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureE.setValue(db.selectMaxTempFromConf())

        self.temperatureReadingFrequencyE = QSpinBox(self)
        self.temperatureReadingFrequencyE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.temperatureReadingFrequencyE.setValue(db.selectFrequencyFromConf())

        self.minTemperatureB = QPushButton("Zapisz", self)
        self.minTemperatureB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.minTemperatureB.clicked.connect(self.onSaveMinTemperature)

        self.maxTemperatureB = QPushButton("Zapisz", self)
        self.maxTemperatureB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureB.clicked.connect(self.onSaveMaxTemperature)

        self.temperatureReadingFrequencyB = QPushButton("Zapisz", self)
        self.temperatureReadingFrequencyB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.temperatureReadingFrequencyB.clicked.connect(self.onSaveTemperatureReadingFrequency)

        self.horizontalGroupBox.setLayout(layout)

        layout.addWidget(self.minTemperatureL, 1, 1)
        layout.addWidget(self.minTemperatureE, 1, 2)
        layout.addWidget(self.minTemperatureB, 1, 3)

        layout.addWidget(self.maxTemperatureL, 2, 1)
        layout.addWidget(self.maxTemperatureE, 2, 2)
        layout.addWidget(self.maxTemperatureB, 2, 3)

        layout.addWidget(self.temperatureReadingFrequencyL, 3, 1)
        layout.addWidget(self.temperatureReadingFrequencyE, 3, 2)
        layout.addWidget(self.temperatureReadingFrequencyB, 3, 3)

        self.setWindowTitle("Simple dialog")
        self.setFocus()
        self.showMaximized()

    def onSaveMinTemperature(self):
        minTemperatureValue = self.minTemperatureE.value()
        db.updateMinTemp(minTemperatureValue)
        print(minTemperatureValue)

    def onSaveMaxTemperature(self):
        maxTemperatureValue = self.maxTemperatureE.value()
        print(maxTemperatureValue)
        db.updateMaxTemp(maxTemperatureValue)

    def onSaveTemperatureReadingFrequency(self):
        temperatureReadingFrequency = self.temperatureReadingFrequencyE.value()
        db.updateFrequency(temperatureReadingFrequency)
        print(temperatureReadingFrequency)
'''

class SimpleDialog(QDialog):

    def __init__(self):
        super().__init__()

        oTabWidget = QTabWidget(self)
        self.createTable()

        oPage1 = QWidget()
        oVBox1 = QGridLayout()
        oPage1.setLayout(oVBox1)

        oPage2 = QWidget()
        oVBox2 = QVBoxLayout()
        oVBox2.addWidget(self.tableWidget)
        oPage2.setLayout(oVBox2)

        oPage3 = QWidget()

        oTabWidget.addTab(oPage1,"Page1")
        oTabWidget.addTab(oPage2,"Page2")
        oTabWidget.addTab(oPage3,"Page3")

        oTabWidget.setFixedSize(1920, 1080)

        oVBox1.setColumnStretch(1, 5)
        oVBox1.setColumnStretch(2, 5)
        oVBox1.setColumnStretch(3, 5)

        self.minTemperatureL = QLabel("Temperatura uruchamiania grzałki: ", self)
        self.minTemperatureL.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureL = QLabel("Temperatura wyłączania grzałki: ", self)
        self.maxTemperatureL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.temperatureReadingFrequencyL = QLabel("Częstotliwość sczytywania temperatury:", self)
        self.temperatureReadingFrequencyL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.minTemperatureE = QSpinBox(self)
        self.minTemperatureE.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.minTemperatureE.setValue(db.selectMinTempFromConf())

        self.maxTemperatureE = QSpinBox(self)
        self.maxTemperatureE.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureE.setValue(db.selectMaxTempFromConf())

        self.temperatureReadingFrequencyE = QSpinBox(self)
        self.temperatureReadingFrequencyE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.temperatureReadingFrequencyE.setValue(db.selectFrequencyFromConf())

        self.minTemperatureB = QPushButton("Zapisz", self)
        self.minTemperatureB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.minTemperatureB.clicked.connect(self.onSaveMinTemperature)

        self.maxTemperatureB = QPushButton("Zapisz", self)
        self.maxTemperatureB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureB.clicked.connect(self.onSaveMaxTemperature)

        self.temperatureReadingFrequencyB = QPushButton("Zapisz", self)
        self.temperatureReadingFrequencyB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.temperatureReadingFrequencyB.clicked.connect(self.onSaveTemperatureReadingFrequency)

        oVBox1.addWidget(self.minTemperatureL, 1, 1)
        oVBox1.addWidget(self.minTemperatureE, 1, 2)
        oVBox1.addWidget(self.minTemperatureB, 1, 3)

        oVBox1.addWidget(self.maxTemperatureL, 2, 1)
        oVBox1.addWidget(self.maxTemperatureE, 2, 2)
        oVBox1.addWidget(self.maxTemperatureB, 2, 3)

        oVBox1.addWidget(self.temperatureReadingFrequencyL, 3, 1)
        oVBox1.addWidget(self.temperatureReadingFrequencyE, 3, 2)
        oVBox1.addWidget(self.temperatureReadingFrequencyB, 3, 3)

        self.showMaximized()

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Date and time', 'Temperature'])
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)

    def onSaveMinTemperature(self):
        minTemperatureValue = self.minTemperatureE.value()
        db.updateMinTemp(minTemperatureValue)
        print(minTemperatureValue)

    def onSaveMaxTemperature(self):
        maxTemperatureValue = self.maxTemperatureE.value()
        print(maxTemperatureValue)
        db.updateMaxTemp(maxTemperatureValue)

    def onSaveTemperatureReadingFrequency(self):
        temperatureReadingFrequency = self.temperatureReadingFrequencyE.value()
        db.updateFrequency(temperatureReadingFrequency)
        print(temperatureReadingFrequency)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SimpleDialog()
    app.exec_()

