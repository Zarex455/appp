# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 387)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 451, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.tab1)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 401, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 399, 319))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_6)
        self.textBrowser.setGeometry(QtCore.QRect(40, 20, 321, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_6)
        self.pushButton.setGeometry(QtCore.QRect(260, 250, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.splitter = QtWidgets.QSplitter(parent=self.scrollAreaWidgetContents_6)
        self.splitter.setGeometry(QtCore.QRect(110, 180, 141, 31))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(parent=self.splitter)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(parent=self.scrollAreaWidgetContents_6)
        self.progressBar.setGeometry(QtCore.QRect(20, 290, 371, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.tab2)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 421, 301))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 299))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(0, 190, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 139, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(0, 130, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(50, 70, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Далее"))
        self.label.setText(_translate("MainWindow", "Ответ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Вопрос"))
        self.label_6.setText(_translate("MainWindow", "Ваша оценка: 5"))
        self.label_5.setText(_translate("MainWindow", "Набрано балов 18 из 20 возможных.\n"
"Ваш результат 90%"))
        self.label_2.setText(_translate("MainWindow", "Всего заданий в тесте: /t afsd"))
        self.label_3.setText(_translate("MainWindow", "Всего заданий в тесте: /t afsd"))
        self.label_4.setText(_translate("MainWindow", "Всего заданий в тесте: /t afsd"))
        self.pushButton_2.setText(_translate("MainWindow", "ОК ✔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Результат"))