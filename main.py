from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QVBoxLayout, QCalendarWidget, QLayout
import sys
from PyQt5 import QtGui

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
       # self.calendar.setFirstDayOfWeek(self, )
        date = self.calendar.selectedDate()
        print(date)

        vbox.addWidget(self.calendar)
        

        self.setLayout(vbox)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

