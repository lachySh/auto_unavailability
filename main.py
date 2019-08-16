from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QVBoxLayout, QCalendarWidget, QLayout
import sys
from PyQt5 import QtGui, QtCore

app = QApplication([])

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "ESS VRL Unavailability Tool"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.Calendar()

        self.show()

    def Calendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setFirstDayOfWeek(QtCore.Qt.Thursday)
        date = self.calendar.selectedDate()
        self.lbl = QLabel()
        self.lbl.setText("Select a Thursday date to start week with")
        vbox.addWidget(self.lbl)
        print(date)

        vbox.addWidget(self.calendar)
        

        self.setLayout(vbox)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

