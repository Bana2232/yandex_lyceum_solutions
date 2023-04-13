from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Second_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 598)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "    background-color: rgb(247, 247, 247);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.horizontalFrame_2)
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.horizontalFrame.setStyleSheet("")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.go_back_to_the_main_menu = QtWidgets.QPushButton(self.horizontalFrame)
        self.go_back_to_the_main_menu.setMinimumSize(QtCore.QSize(110, 40))
        self.go_back_to_the_main_menu.setMaximumSize(QtCore.QSize(150, 40))
        self.go_back_to_the_main_menu.setStyleSheet("QPushButton {\n"
                                                    "    background-color: rgb(255, 255, 255);\n"
                                                    "    border-radius: 15px;\n"
                                                    "    \n"
                                                    "}\n"
                                                    "QPushButton:hover {\n"
                                                    "    background-color: rgb(223, 223, 223);\n"
                                                    "}\n"
                                                    "")
        self.go_back_to_the_main_menu.setObjectName("go_back_to_the_main_menu")
        self.horizontalLayout.addWidget(self.go_back_to_the_main_menu)

        self.answer_line = QtWidgets.QLineEdit(self.horizontalFrame)
        self.answer_line.setMinimumSize(QtCore.QSize(400, 40))
        self.answer_line.setMaximumSize(QtCore.QSize(500, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.answer_line.setFont(font)
        self.answer_line.setStyleSheet("border-radius: 15px;\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "border: 1px solid #ced4da;\n"
                                       "padding-left: 5px;")
        self.answer_line.setObjectName("answer_line")
        self.horizontalLayout.addWidget(self.answer_line)
        self.check_button = QtWidgets.QPushButton(self.horizontalFrame)
        self.check_button.setMinimumSize(QtCore.QSize(90, 40))
        self.check_button.setMaximumSize(QtCore.QSize(150, 40))
        self.check_button.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(255, 255, 255);\n"
                                        "    border-radius: 15px;\n"
                                        "    \n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(223, 223, 223);\n"
                                        "}\n"
                                        "")
        self.check_button.setObjectName("check_button")
        self.horizontalLayout.addWidget(self.check_button)

        self.verticalLayout.addWidget(self.horizontalFrame, 0, QtCore.Qt.AlignRight)

        self.next_image = QtWidgets.QPushButton(self.horizontalFrame)
        self.next_image.setMinimumSize(QtCore.QSize(90, 40))
        self.next_image.setMaximumSize(QtCore.QSize(150, 40))
        self.next_image.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 15px;\n"
                                      "    \n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(223, 223, 223);\n"
                                      "}\n"
                                      "")
        self.next_image.setObjectName("next_image")
        self.horizontalLayout.addWidget(self.next_image)

        MainWindow.setCentralWidget(self.centralwidget)

        self.image.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Угадай-ка город"))
        self.label_2.setText(_translate("MainWindow", "Какой это город?"))
        self.go_back_to_the_main_menu.setText(_translate("MainWindow", "Закончить игру"))
        self.next_image.setText(_translate("MainWindow", "Следующее"))
        self.answer_line.setPlaceholderText(_translate("MainWindow", "Ваш ответ"))
        self.check_button.setText(_translate("MainWindow", "Проверить"))
