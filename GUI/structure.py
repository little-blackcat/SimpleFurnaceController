import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLineEdit, QLabel, QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from DatabaseManager import DatabaseManager

db = DatabaseManager("/home/pi/sfc/Common/database.db")

class SimpleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        #self.show()
        self.showFullScreen()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()

        layout.setColumnStretch(1, 5)
        layout.setColumnStretch(2, 5)
        layout.setColumnStretch(3, 5)

        self.minTemperatureL = QLabel("Temperatura uruchamiania grzałki: ", self)
        self.minTemperatureL.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        '''
        font = QFont()
        font.setPointSize(24)
        minTemperatureL.setFont(font)
        '''
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SimpleDialog()
    app.exec_()

