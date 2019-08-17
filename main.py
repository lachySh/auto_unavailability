from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QDialog, QVBoxLayout, QCalendarWidget, QLayout, QLineEdit,QGridLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from datetime import datetime  
from datetime import timedelta
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

        f = open("tdb.txt", "r")
        startdate = f.readline()
        starr = startdate.split(".")
        print(starr)

        #date = QDate.fromString()

        vbox = QVBoxLayout()
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        calendar.setFirstDayOfWeek(QtCore.Qt.Thursday)
        #calendar.setSelectedDate()
        
        lbl = QLabel()
        lbl.setText("Select a Thursday date to start week with")
        vbox.addWidget(lbl)

        vbox.addWidget(calendar)

        #self.setLayout(grid)
        f = open("tdb.txt", "r")
        startdate = f.readline()
        enddate = f.readline()
        times = []
        temp_times = []

        for n in range(0,7):
            temp_times = f.readline().split()
            times.append(temp_times)
        print(times)
        
        grid = QGridLayout()

        day = ["Thurs","Fri","Sat","Sun","Mon","Tues","Weds"]
        for i in range(1,8):
            daycount = QLabel()
            daycount.setText(day[i-1])
            grid.addWidget(daycount,i,0)
            for j in range(2,6):
                box = QLineEdit()
                box.setText(times[i-1][j-2])
                grid.addWidget(box,i,j)

        bbox = QVBoxLayout()
        button = QPushButton()
        button.setText("Set Unavailability")
        button.clicked.connect(handleButton)
        bbox.addWidget(button)

        

        vall = QVBoxLayout()
        vall.addLayout(vbox)
        vall.addLayout(grid)
        vall.addLayout(bbox)
        self.setLayout(vall)

        

        self.show()

        """def handleButton():
            date = calendar.selectedDate()
            strdate = QDate.toPyDate(date)
            enddate = strdate + timedelta(days=6)
            print(enddate)
            strdate = str(strdate)
            strdate = strdate.split("-")
            enddate = str(enddate)
            enddate = enddate.split("-")
            print(strdate)
            #FILE READING
            f = open("tdb.txt", "r")
            startdate = f.readline()
            enddate = f.readline()

            times = []
            temp_times = []

            for n in range(0,7):
                temp_times = f.readline().split()
                times.append(temp_times)
                #print(temp_times)
            msg = f.readline()
            #FILE WRITING
            f = open("tdb.txt", "w")
            f.write(strdate[2]+"."+strdate[1]+"."+strdate[0])
            f.write(enddate[2]+"."+enddate[1]+"."+enddate[0])"""

        

App = QApplication(sys.argv)
App.setStyle('Fusion')
window = Window()
sys.exit(App.exec())

