# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MiniWireshark.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import QRect
from scapy.all import *
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QDialog, QInputDialog, QLineEdit, QColorDialog, QPushButton
import threading

#sniff(prn=lambda x: x.summary(), lfilter=None, count=5, offline=None, store=0, L2socket=None, timeout=None)

list = get_windows_if_list()

s1 = list[0]['name']
s2 = list[1]['name']

stopFlag = False


pktsList = []
class mythread(threading.Thread):
    def run(self):
        if (self.name == 'StopThread'):
            print (self.name)
            #print('ana stop')
            #StopThread._is_stopped = False
            ui.DoStop()
            #StopThread._is_stopped = True
            #threading.currentThread = threading.main_thread()
        if (self.name == 'Worker'):
            print (self.name)
            #print("ana  worker")
            #worker._is_stopped = False
            #threading.currentThread = worker
            #print(worker.is_alive())
            ui.DoStart()
            #print(worker.is_alive())
            #worker._is_stopped = True
            #threading.current_thread = threading.main_thread()
            #worker.run()

GUI = mythread(name='GUI')
worker = mythread(name='Worker')
StopThread = mythread(name = 'StopThread')


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Save'
        self.left = 750
        self.top = 500
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        if (stopFlag == True):
            textboxValue = self.textbox.text()
            #QMessageBox.question(self, 'Message - pythonspot.com', "File Name not specified Or File Name Already Exists", QMessageBox.Ok,QMessageBox.Ok)
            try:
                wrpcap(textboxValue, pktsList)
                self.hide()
            except:
                QMessageBox.question(self, 'Message - pythonspot.com', "File Name not specified Or File Name Already Exists", QMessageBox.Ok,QMessageBox.Ok)
                app.exec_()
            self.textbox.setText("")

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Open'
        self.left = 750
        self.top = 500
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):


        textboxValue = self.textbox.text()
        #QMessageBox.question(self, 'Message - pythonspot.com', "File Does not Exist", QMessageBox.Ok,QMessageBox.Ok)
        global errorFlag
        errorFlag = False
        global pktsList
        pktsList = []
        try:
            pktsList = rdpcap(textboxValue)
            self.hide()
        except:
            QMessageBox.question(self, 'Warning', "File Does not Exist", QMessageBox.Ok, QMessageBox.Ok)
            errorFlag = True
        ui.write()
        self.textbox.setText("")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 712)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Capture.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButtonStart.sizePolicy().hasHeightForWidth())
        self.pushButtonStart.setSizePolicy(sizePolicy)
        self.pushButtonStart.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButtonStart.setBaseSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setMouseTracking(False)
        self.pushButtonStart.setAutoFillBackground(True)
        self.pushButtonStart.setText("")
        self.pushButtonStart.setIcon(icon)
        self.pushButtonStart.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonStart.setCheckable(False)
        self.pushButtonStart.setChecked(False)
        self.pushButtonStart.setAutoRepeat(True)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStart.clicked.connect(self.Lets_start)
        self.horizontalLayout.addWidget(self.pushButtonStart)
        self.pushButtonStop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButtonStop.sizePolicy().hasHeightForWidth())
        self.pushButtonStop.setSizePolicy(sizePolicy)
        self.pushButtonStop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Capturee.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStop.setIcon(icon1)
        self.pushButtonStop.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonStop.setAutoRepeat(True)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.pushButtonStop.clicked.connect(StopThread.start)
        self.horizontalLayout.addWidget(self.pushButtonStop)
        self.pushButtonRestart = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButtonRestart.sizePolicy().hasHeightForWidth())
        self.pushButtonRestart.setSizePolicy(sizePolicy)
        self.pushButtonRestart.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Captureee.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRestart.setText("Filter")
        self.pushButtonRestart.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonRestart.setAutoRepeat(True)
        self.pushButtonRestart.setObjectName("pushButtonRestart")
        self.pushButtonRestart.clicked.connect(self.DoRestart)
        self.horizontalLayout.addWidget(self.pushButtonRestart)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBoxFilter = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxFilter.setObjectName("comboBoxFilter")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.comboBoxFilter.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxFilter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBoxCapture = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCapture.setObjectName("comboBoxCapture")
        self.comboBoxCapture.addItem("")
        self.comboBoxCapture.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBoxCapture)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.tableWidget2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(1)
        self.tableWidget2.setRowCount(3)
        self.verticalLayout_3.addWidget(self.tableWidget2)
        self.Text = QtWidgets.QTextEdit(self.centralwidget)
        self.Text.setObjectName("Text")
        self.verticalLayout_3.addWidget(self.Text)
        self.Text.show()
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuCapture = QtWidgets.QMenu(self.menubar)
        self.menuCapture.setObjectName("menuCapture")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionRefresh)
        self.menuCapture.addAction(self.actionStart)
        self.menuCapture.addAction(self.actionStop)
        self.menuCapture.addAction(self.actionRestart)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuCapture.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini Wireshark"))
        self.label_2.setText(_translate("MainWindow", "   Filter   "))
        self.comboBoxFilter.setItemText(0, _translate("MainWindow", ""))
        self.comboBoxFilter.setItemText(1, _translate("MainWindow", "ARP"))
        self.comboBoxFilter.setItemText(2, _translate("MainWindow", "DHCP"))
        self.comboBoxFilter.setItemText(3, _translate("MainWindow", "DHCP6"))
        self.comboBoxFilter.setItemText(4, _translate("MainWindow", "DNS"))
        self.comboBoxFilter.setItemText(5, _translate("MainWindow", "ICMP"))
        self.comboBoxFilter.setItemText(6, _translate("MainWindow", "ICMPv6"))
        self.comboBoxFilter.setItemText(7, _translate("MainWindow", "IP"))
        self.comboBoxFilter.setItemText(8, _translate("MainWindow", "IPv6"))
        self.comboBoxFilter.setItemText(9, _translate("MainWindow", "TCP"))
        self.comboBoxFilter.setItemText(10, _translate("MainWindow", "UDP"))
        self.comboBoxFilter.activated.connect(self.filter_choice)
        self.label.setText(_translate("MainWindow", " Capture"))
        self.comboBoxCapture.setItemText(0, _translate("MainWindow", s1))
        self.comboBoxCapture.setItemText(1, _translate("MainWindow", s2))
        self.comboBoxCapture.activated.connect(self.capture_choice)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protocol"))

        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Length"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Info"))
        self.tableWidget.doubleClicked.connect(self.packetClickedFunction)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuCapture.setTitle(_translate("MainWindow", "Capture"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.triggered.connect(self.close_application)
        self.actionRestart.triggered.connect(self.DoRestart)
        self.actionStart.triggered.connect(self.Lets_start)
        self.actionStop.triggered.connect(StopThread.start)
        self.actionOpen.triggered.connect(self.Open)
        self.actionSave.triggered.connect(self.Save)
        self.actionStart.setText(_translate("MainWindow", "Start Captue"))
        self.actionStop.setText(_translate("MainWindow", "Stop Captue"))
        self.actionRestart.setText(_translate("MainWindow", "Restart Captue"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
    def close_application(self):
        sys.exit()
    def capture_choice(self):
        print("selection changed " + self.comboBoxCapture.currentText())
        if (self.comboBoxCapture.currentText() == s1):
            global s
            s = s1
            print("Ethernet")
        elif (self.comboBoxCapture.currentText() == s2):
            s = s2
            print("Wi-Fi")
    def filter_choice(self):
        print("selection changed " + self.comboBoxFilter.currentText())
        global filteringChoice
        filteringChoice = self.comboBoxFilter.currentText()
        self.EmptyTable()
    def filterDisplay(self, protocoll):
        global pktsList
        oldList = pktsList
        pktsList = []
        if(protocoll != ""):
            for p in oldList:
                if p.haslayer(protocoll):
                    pktsList.append(p)
            j = 0
            for p in pktsList:
                global Time
                Time = p.sprintf("%.time%")
                global SourceIP
                SourceIP = p.sprintf("{ARP:%-15s,ARP.psrc%}{IP:%-15s,IP.src%}{IPv6:%-15s,IPv6.src%}")
                global DstIP
                DstIP = p.sprintf("{ARP:%-15s,ARP.pdst%}{IP:%-15s,IP.dst%}{IPv6:%-15s,IPv6.dst%}")
                global protocol
                protocol = p.sprintf("{TCP:TCP}{UDP:UDP}{ICMP:ICMP}")
                global length
                length = p.sprintf("{ARP:%ARP.plen%}{IP:%IP.len%}{IPv6:%IPv6.plen%}")
                global Info
                Info = p.sprintf(
                    "{UDP:%UDP.sport%  ->  %UDP.dport% , chksum=%UDP.chksum%} {TCP:%TCP.sport%  ->  %TCP.dport% , seq=%TCP.seq% , ack=%TCP.ack% , win=%TCP.window%}")
                self.fillTable(j)
                j += 1
    def Lets_start(self):
        worker.daemon = True
        worker.start()
    def DoStop(self):
        print (threading.currentThread().getName())
        global stopFlag
        stopFlag = True
        worker._is_stopped = True
        #print ("hello")
    def fillTable(self, i):
        self.tableWidget.setItem(i, 0, QTableWidgetItem(Time))
        self.tableWidget.setItem(i, 1, QTableWidgetItem(SourceIP))
        self.tableWidget.setItem(i, 2, QTableWidgetItem(DstIP))
        self.tableWidget.setItem(i, 3, QTableWidgetItem(protocol))
        self.tableWidget.setItem(i, 4, QTableWidgetItem(length))
        self.tableWidget.setItem(i, 5, QTableWidgetItem(Info))
        self.tableWidget.resizeColumnsToContents()
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
    def EmptyTable(self):
        self.tableWidget.clear()
    def DoStart(self):
        #print("Hello")

        #print (threading.currentThread().getName())
        y = 0
        count = 0
        global stopFlag
        while not stopFlag:
            p = sniff(iface=s, count=1, timeout=10, store=1)
            print("check")
            if len(p) == 0:
                continue
            pktsList.append(p[0])
            global Time
            Time = p[0].sprintf("%.time%")
            global SourceIP
            SourceIP = p[0].sprintf("{ARP:%-15s,ARP.psrc%}{IP:%-15s,IP.src%}{IPv6:%-15s,IPv6.src%}")
            global DstIP
            DstIP = p[0].sprintf("{ARP:%-15s,ARP.pdst%}{IP:%-15s,IP.dst%}{IPv6:%-15s,IPv6.dst%}")
            global protocol
            protocol = p[0].sprintf("{TCP:TCP}{UDP:UDP}{ICMP:ICMP}")
            global length
            length = p[0].sprintf("{ARP:%ARP.plen%}{IP:%IP.len%}{IPv6:%IPv6.plen%}")
            global Info

            Info = p[0].sprintf(
                "{UDP:%UDP.sport%  ->  %UDP.dport% , chksum=%UDP.chksum%} {TCP:%TCP.sport%  ->  %TCP.dport% , seq=%TCP.seq% , ack=%TCP.ack% , win=%TCP.window%}")

            ui.fillTable(y)
            y += 1
            count += 1
            if (count == 50):
                stopFlag = True
                print("yalla b2a")
                y = 0
        print(":D")
    def DoRestart(self):
        global filteringChoice
        self.filterDisplay(filteringChoice)
    def packetClickedFunction(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
            pktNum = currentQTableWidgetItem.row()
            S1 = pktsList[pktNum].sprintf("Ethernet, Src:%r,Ether.src%, Dst:%r,Ether.dst%, type:%r,Ether.type%")
            S2 = pktsList[pktNum].sprintf(
                "Internet Protocol Version {IP:4, Src:%IP.src%, Dst:%IP.dst% }{IPv6:6, Src:%IPv6.src%, Dst:%IPv6.dst%}")
            S3 = pktsList[pktNum].sprintf(
                "{UDP:User Datagram Protocol, Src Port:%UDP.sport%, Dst Port:%UDP.dport%, len:%UDP.len%, chksum:%UDP.chksum%}{TCP:Transmission Control Protocol, Src Port:%TCP.sport%, Dst Port:%TCP.dport%, seq:%TCP.seq%, ack:%TCP.ack%, win:%TCP.window%, chksum:%TCP.chksum%}")
            hexviewS = hexdump(pktsList[pktNum], dump=True)
            self.add(S1, S2, S3, hexviewS)
    def Open(self):
        print("let's Open!")
        self.window = QtWidgets.QMainWindow()
        self.ui = AppWindow()
        print("Opened!")
    def Save(self):
        print("Let's Save!")
        self.window = QtWidgets.QMainWindow()
        self.ui = App()
        print("Saved!")
    def add(self, x, y, z, k):
        self.tableWidget2.setItem(0, 0, QTableWidgetItem(x))
        self.tableWidget2.setItem(0, 1, QTableWidgetItem(y))
        self.tableWidget2.setItem(0, 2, QTableWidgetItem(z))
        self.tableWidget2.resizeColumnsToContents()
        self.Text.setText(k)
    def write(self):
        i = 0
        if errorFlag == False:
            global pktsList
            for p in pktsList:
                global Time
                Time = p.sprintf("%.time%")
                global SourceIP
                SourceIP = p.sprintf("{ARP:%-15s,ARP.psrc%}{IP:%-15s,IP.src%}{IPv6:%-15s,IPv6.src%}")
                global DstIP
                DstIP = p.sprintf("{ARP:%-15s,ARP.pdst%}{IP:%-15s,IP.dst%}{IPv6:%-15s,IPv6.dst%}")
                global protocol
                protocol = p.sprintf("{TCP:TCP}{UDP:UDP}{ICMP:ICMP}")
                global length
                length = p.sprintf("{ARP:%ARP.plen%}{IP:%IP.len%}{IPv6:%IPv6.plen%}")
                global Info
                Info = p.sprintf(
                    "{UDP:%UDP.sport%  ->  %UDP.dport% , chksum=%UDP.chksum%} {TCP:%TCP.sport%  ->  %TCP.dport% , seq=%TCP.seq% , ack=%TCP.ack% , win=%TCP.window%}")
                self.fillTable(i)
                i += 1

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
