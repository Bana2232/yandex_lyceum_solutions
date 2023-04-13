import requests
import sys

from random import random, choice, randint

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from main_window import Ui_MainWindow
from second_window import Ui_Second_Window


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Main_window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.process()

    def process(self):
        self.comboBox.currentIndexChanged.connect(self.check_name_of_the_city)
        self.pushButton.clicked.connect(self.start_the_game)

    def check_name_of_the_city(self):
        if self.comboBox.currentIndex() == 0:
            self.pushButton.setEnabled(False)

        else:
            self.pushButton.setEnabled(True)

    def start_the_game(self):
        self.game_window = Second_Window(self.comboBox.currentText())
        self.game_window.show()
        self.close()


class Second_Window(Ui_Second_Window, QMainWindow):
    def __init__(self, name_of_the_city):
        super().__init__()

        self.name_of_the_city = name_of_the_city
        self.parameters_for_images = {"Каспийск": {'coors': (47.635665, 42.890853)},
                                      "Махачкала": {"coors": (47.504745, 42.9831)},
                                      "Дербент": {'coors': (48.288776, 42.057669)},
                                      "Москва": {"coors": (37.617698, 55.755864)},
                                      "Краснодар": {"coors": (38.975313, 45.03547)}
                                      }
        self.view = ["map", "sat"]

        self.setupUi(self)
        self.process()

    def process(self):
        self.next_image.clicked.connect(self.show_image)
        self.check_button.clicked.connect(self.checking_the_response)
        self.go_back_to_the_main_menu.clicked.connect(self.return_to_main_menu)

        self.answer_line.textEdited.connect(self.set_black_text_color)

        self.show_image()

    def set_black_text_color(self):
        self.answer_line.setStyleSheet("border-radius: 15px;\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "border: 1px solid #ced4da;\n"
                                       "padding-left: 5px;\n"
                                       "color: rgb(0, 0, 0);")

    def show_image(self):
        spn = random() / 20

        random_coors = [(random() / 80, -random() / 80), (random() / 80, -random() / 80)]

        response = requests.get(
            f"https://static-maps.yandex.ru/1.x/?ll={self.parameters_for_images[self.name_of_the_city]['coors'][0] - random_coors[0][randint(0, 1)]},{self.parameters_for_images[self.name_of_the_city]['coors'][1] - random_coors[0][randint(0, 1)]}&spn={spn},0.00619&l={choice(self.view)}")

        with open("image.jpeg", "wb") as file:
            file.write(response.content)

        self.image.setPixmap(QPixmap("image.jpeg"))

    def checking_the_response(self):
        if self.answer_line.text().lower() == self.name_of_the_city.lower():
            self.answer_line.setStyleSheet("border-radius: 15px;\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "border: 1px solid #ced4da;\n"
                                           "padding-left: 5px;\n"
                                           "color: rgb(179, 255, 0);")
            self.return_to_main_menu()

        else:
            self.answer_line.setStyleSheet("border-radius: 15px;\n"
                                           "background-color: rgb(255, 255, 255);\n"
                                           "border: 1px solid #ced4da;\n"
                                           "padding-left: 5px;\n"
                                           "color: rgb(249, 7, 31);")

    def return_to_main_menu(self):

        if self.sender() == self.go_back_to_the_main_menu:
            self.main_window = Main_window()
            self.main_window.show()
            self.close()

        else:
            message = QMessageBox.question(self, "Победа",
                                           "Вы вернётесь в главное меню",
                                           QMessageBox.Ok)

            if message == QMessageBox.Ok:
                self.main_window = Main_window()
                self.main_window.show()
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
