import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QSizePolicy, QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, Qt
from DatabaseManager import DatabaseManager

db = DatabaseManager("/home/pi/sfc1/SimpleFurnaceController/Common/database.db")

# debug db
# db = DatabaseManager("../Common/database.db")

class SimpleDialog(QDialog):

    def __init__(self, width, height):
        super().__init__()

        self.width = width;
        self.height = height;

        oTabWidget = QTabWidget(self)
        oTabWidget.setMinimumHeight(height)
        oTabWidget.setMinimumWidth(width)
        oTabWidget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.createTable()

        spinBoxFont = QFont()
        spinBoxFont.setPointSize(60)

        labelFont = QFont()
        labelFont.setPointSize(30)

        oPage1 = QWidget()
        oVBox1 = QGridLayout()
        oPage1.setLayout(oVBox1)

        oPage2 = QWidget()
        oVBox2 = QVBoxLayout()
        oVBox2.addWidget(self.tableWidget)
        oPage2.setLayout(oVBox2)

        oTabWidget.addTab(oPage1,"Settings")
        oTabWidget.addTab(oPage2,"Last temperatures")

        oVBox1.setColumnStretch(1, 3)
        oVBox1.setColumnStretch(2, 3)
        oVBox1.setColumnStretch(3, 3)

        # ----- MIN -----
        self.minTemperatureL = QLabel("Min temperature: ", self)
        self.minTemperatureL.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.minTemperatureL.setFont(labelFont)

        self.minTemperatureE = QSpinBox(self)
        self.minTemperatureE.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.minTemperatureE.setAlignment(Qt.AlignCenter)
        self.minTemperatureE.setFont(spinBoxFont)
        self.minTemperatureE.setValue(db.selectMinTempFromConf())

        self.minTemperatureB = QPushButton("Save", self)
        self.minTemperatureB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.minTemperatureB.setFont(labelFont)
        self.minTemperatureB.clicked.connect(self.onSaveMinTemperature)

        # ----- MAX -----
        self.maxTemperatureL = QLabel("Max temperature: ", self)
        self.maxTemperatureL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.maxTemperatureL.setFont(labelFont)

        self.maxTemperatureE = QSpinBox(self)
        self.maxTemperatureE.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureE.setAlignment(Qt.AlignCenter)
        self.maxTemperatureE.setFont(spinBoxFont)
        self.maxTemperatureE.setValue(db.selectMaxTempFromConf())

        self.maxTemperatureB = QPushButton("Save", self)
        self.maxTemperatureB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.maxTemperatureB.setFont(labelFont)
        self.maxTemperatureB.clicked.connect(self.onSaveMaxTemperature)

        # ----- FREQ -----
        self.temperatureReadingFrequencyL = QLabel("Checking frequency:", self)
        self.temperatureReadingFrequencyL.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.temperatureReadingFrequencyL.setFont(labelFont)

        self.temperatureReadingFrequencyE = QSpinBox(self)
        self.temperatureReadingFrequencyE.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.temperatureReadingFrequencyE.setAlignment(Qt.AlignCenter)
        self.temperatureReadingFrequencyE.setFont(spinBoxFont)
        self.temperatureReadingFrequencyE.setValue(db.selectFrequencyFromConf())

        self.temperatureReadingFrequencyB = QPushButton("Save", self)
        self.temperatureReadingFrequencyB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.temperatureReadingFrequencyB.setFont(labelFont)
        self.temperatureReadingFrequencyB.clicked.connect(self.onSaveTemperatureReadingFrequency)

        # ----- REFRESH -----
        self.refreshTemperaturesB = QPushButton("Refresh", self)
        self.refreshTemperaturesB.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.refreshTemperaturesB.setMaximumHeight(self.height/5)
        self.refreshTemperaturesB.setFont(labelFont)
        self.refreshTemperaturesB.clicked.connect(self.onRefreshTemperatures)

        # ----- TAB 1 -----
        oVBox1.addWidget(self.minTemperatureL, 1, 1)
        oVBox1.addWidget(self.minTemperatureE, 1, 2)
        oVBox1.addWidget(self.minTemperatureB, 1, 3)

        oVBox1.addWidget(self.maxTemperatureL, 2, 1)
        oVBox1.addWidget(self.maxTemperatureE, 2, 2)
        oVBox1.addWidget(self.maxTemperatureB, 2, 3)

        oVBox1.addWidget(self.temperatureReadingFrequencyL, 3, 1)
        oVBox1.addWidget(self.temperatureReadingFrequencyE, 3, 2)
        oVBox1.addWidget(self.temperatureReadingFrequencyB, 3, 3)

        # ----- TAB 2 -----
        oVBox2.addWidget(self.refreshTemperaturesB)

        #self.showMaximized()
        self.showFullScreen()

    def createTable(self):
        tableFont = QFont()
        tableFont.setPointSize(20)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        for i in range(10):
            self.tableWidget.setRowHeight(i, 40)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setColumnWidth(0, self.width/2)
        self.tableWidget.setHorizontalHeaderLabels(['Date and time', 'Temperature'])
        self.tableWidget.setFont(tableFont)

        header = self.tableWidget.horizontalHeader()
        header.setStretchLastSection(True)

        self.updateTable()

    def updateTable(self):
        datetime_Data = []
        temperature_data = []
        datetime_Data, temperature_data = db.selectLastTenTemperatures()

        self.tableWidget.setItem(0,0, QTableWidgetItem(datetime_Data[0].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(1,0, QTableWidgetItem(datetime_Data[1].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(2,0, QTableWidgetItem(datetime_Data[2].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(3,0, QTableWidgetItem(datetime_Data[3].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(4,0, QTableWidgetItem(datetime_Data[4].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(5,0, QTableWidgetItem(datetime_Data[5].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(6,0, QTableWidgetItem(datetime_Data[6].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(7,0, QTableWidgetItem(datetime_Data[7].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(8,0, QTableWidgetItem(datetime_Data[8].strftime("%B %d, %Y, %H:%M:%S")))
        self.tableWidget.setItem(9,0, QTableWidgetItem(datetime_Data[9].strftime("%B %d, %Y, %H:%M:%S")))

        self.tableWidget.setItem(0,1, QTableWidgetItem(str(temperature_data[0])))
        self.tableWidget.setItem(1,1, QTableWidgetItem(str(temperature_data[1])))
        self.tableWidget.setItem(2,1, QTableWidgetItem(str(temperature_data[2])))
        self.tableWidget.setItem(3,1, QTableWidgetItem(str(temperature_data[3])))
        self.tableWidget.setItem(4,1, QTableWidgetItem(str(temperature_data[4])))
        self.tableWidget.setItem(5,1, QTableWidgetItem(str(temperature_data[5])))
        self.tableWidget.setItem(6,1, QTableWidgetItem(str(temperature_data[6])))
        self.tableWidget.setItem(7,1, QTableWidgetItem(str(temperature_data[7])))
        self.tableWidget.setItem(8,1, QTableWidgetItem(str(temperature_data[8])))
        self.tableWidget.setItem(9,1, QTableWidgetItem(str(temperature_data[9])))


    def onSaveMinTemperature(self):
        minTemperatureValue = self.minTemperatureE.value()
        db.updateMinTemp(minTemperatureValue)
        #print(minTemperatureValue)

    def onSaveMaxTemperature(self):
        maxTemperatureValue = self.maxTemperatureE.value()
        #print(maxTemperatureValue)
        db.updateMaxTemp(maxTemperatureValue)

    def onSaveTemperatureReadingFrequency(self):
        temperatureReadingFrequency = self.temperatureReadingFrequencyE.value()
        db.updateFrequency(temperatureReadingFrequency)
        #print(temperatureReadingFrequency)

    def onRefreshTemperatures(self):
        self.updateTable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    dialog = SimpleDialog(width, height)
    app.exec_()

