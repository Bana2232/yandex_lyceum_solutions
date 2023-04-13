from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(555, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 160, 101, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 15px;\n"
                                      "    \n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(223, 223, 223);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 110, 201, 41))
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    border: 1px solid #ced4da;\n"
                                    "    border-radius: 15px;\n"
                                    "    padding-left: 10px;\n"
                                    "        background-color: rgb(255, 255, 255);\n"
                                    "    }\n"
                                    "    \n"
                                    "    QComboBox::drop-down {\n"
                                    "    border:0px;\n"
                                    "    }\n"
                                    "    \n"
                                    "    QComboBox::down-arrow {\n"
                                    "    image: url(/home/salih/Загрузки/arrow-down.png);\n"
                                    "    width: 24px;\n"
                                    "    height: 24px;\n"
                                    "    margin-right: 15px;\n"
                                    "    }\n"
                                    "    \n"
                                    "    QComboBox:on{\n"
                                    "        border: 2px solid rgb(87, 227, 137);\n"
                                    "    }\n"
                                    "    \n"
                                    "    QComboBox QListView {\n"
                                    "    border-radius: 15px;\n"
                                    "        font-size: 24px;\n"
                                    "        padding: 5px;\n"
                                    "        background-color: #fff;\n"
                                    "        outline: 0px;\n"
                                    "        \n"
                                    "        color: rgb(0, 0, 0);\n"
                                    "    }\n"
                                    "    \n"
                                    "    QComboBox QListView::item {\n"
                                    "    padding-left: 10px;\n"
                                    "        background-color: #00ff00;\n"
                                    "    }\n"
                                    "    \n"
                                    "    QComboBox QListView:item:hover {\n"
                                    "        background-color: rgb(87, 227, 137);\n"
                                    "    }\n"
                                    "    \n"
                                    "    QComboBox QListView:item:selected {\n"
                                    "        background-color: rgb(87, 227, 137);\n"
                                    "    }\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.pushButton.setText(_translate("MainWindow", "Начать игру"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Выберите город"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Каспийск"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Махачкала"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Дербент"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Москва"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Краснодар"))
        self.label.setText(_translate("MainWindow", "Угадай город"))
