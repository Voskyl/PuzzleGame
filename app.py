from PySide2 import QtWidgets, QtCore, QtGui
from puzzle import Puzzle
from random import randint
import os
import constants


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_objects()
        self.setup_ui()
        self.setup_connections()
        self.shuffle()
        self.setup_timer()

    def setup_objects(self):
        self.setup_image()
        self.buttonMemory = []
        self.time = 0
        self.bestTime = self.load_data()

    def setup_image(self):
        self.qim_image = QtGui.QImage(constants.IMAGE_FILE)
        w, h = self.qim_image.size().width(), self.qim_image.size().height()
        if w % 3 == 1 :
            w -= 1
        if w % 3 == 2 :
            w += 1

        if h % 3 == 1 :
            h -= 1
        if h % 3 == 2 :
            h += 1
        self.qim_image = Puzzle(self.qim_image.scaled(w, h))
        self.qim_image_saved = self.qim_image.copy()

    def setup_ui(self):
        self.setWindowTitle("Puzzle game !")
        self.layout_base = QtWidgets.QVBoxLayout(self)
        self.layout_linetext = QtWidgets.QHBoxLayout()
        self.layout_line1 = QtWidgets.QHBoxLayout()
        self.layout_line2 = QtWidgets.QHBoxLayout()
        self.layout_line3 = QtWidgets.QHBoxLayout()

        self.pxm_image = QtGui.QPixmap(self.qim_image).scaled(constants.SIZE_IMAGE, constants.SIZE_IMAGE, QtCore.Qt.KeepAspectRatio)
        self.label_image = QtWidgets.QLabel("")
        self.label_image.setPixmap(self.pxm_image)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_text_1 = QtWidgets.QLabel("")
        self.label_text_1.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_text_2 = QtWidgets.QPushButton(f"Meilleur temps : {self.bestTime}s")

        self.btn_1 = QtWidgets.QPushButton("1")
        self.btn_2 = QtWidgets.QPushButton("2")
        self.btn_3 = QtWidgets.QPushButton("3")
        self.btn_4 = QtWidgets.QPushButton("4")
        self.btn_5 = QtWidgets.QPushButton("5")
        self.btn_6 = QtWidgets.QPushButton("6")
        self.btn_7 = QtWidgets.QPushButton("7")
        self.btn_8 = QtWidgets.QPushButton("8")
        self.btn_9 = QtWidgets.QPushButton("9")

        self.btn_1.setCheckable(True)
        self.btn_2.setCheckable(True)
        self.btn_3.setCheckable(True)
        self.btn_4.setCheckable(True)
        self.btn_5.setCheckable(True)
        self.btn_6.setCheckable(True)
        self.btn_7.setCheckable(True)
        self.btn_8.setCheckable(True)
        self.btn_9.setCheckable(True)

        self.btn_1.setMaximumWidth(100)
        self.btn_2.setMaximumWidth(100)
        self.btn_3.setMaximumWidth(100)
        self.btn_4.setMaximumWidth(100)
        self.btn_5.setMaximumWidth(100)
        self.btn_6.setMaximumWidth(100)
        self.btn_7.setMaximumWidth(100)
        self.btn_8.setMaximumWidth(100)
        self.btn_9.setMaximumWidth(100)

        self.layout_base.addWidget(self.label_image)
        self.layout_linetext.addWidget(self.label_text_1)
        self.layout_linetext.addWidget(self.btn_text_2)
        self.layout_line1.addWidget(self.btn_1)
        self.layout_line1.addWidget(self.btn_2)
        self.layout_line1.addWidget(self.btn_3)
        self.layout_line2.addWidget(self.btn_4)
        self.layout_line2.addWidget(self.btn_5)
        self.layout_line2.addWidget(self.btn_6)
        self.layout_line3.addWidget(self.btn_7)
        self.layout_line3.addWidget(self.btn_8)
        self.layout_line3.addWidget(self.btn_9)

        self.layout_base.addLayout(self.layout_linetext)
        self.layout_base.addLayout(self.layout_line1)
        self.layout_base.addLayout(self.layout_line2)
        self.layout_base.addLayout(self.layout_line3)

    def setup_connections(self):
        self.btn_text_2.clicked.connect(self.reset_data)
        self.btn_1.clicked.connect(self.button_input)
        self.btn_2.clicked.connect(self.button_input)
        self.btn_3.clicked.connect(self.button_input)
        self.btn_4.clicked.connect(self.button_input)
        self.btn_5.clicked.connect(self.button_input)
        self.btn_6.clicked.connect(self.button_input)
        self.btn_7.clicked.connect(self.button_input)
        self.btn_8.clicked.connect(self.button_input)
        self.btn_9.clicked.connect(self.button_input)
        
    def shuffle(self):
        """Mix the puzzle cells.
        """
        for _ in range(constants.SHUFFLE_NB):
            cellsNb = constants.POSSIBLE_CHOICES[randint(0, 11)]
            self.moving_cells(cellsNb)
        self.update_image()

    def button_input(self):
        button_nb = int(self.sender().text())
        self.buttonMemory.append(button_nb)
        self.buttonMemory.sort()
        if len(self.buttonMemory) == 2:
            if self.buttonMemory in (constants.POSSIBLE_CHOICES + constants.REDUNDANCY_CHOICES):
                self.moving_cells(self.buttonMemory)
                self.update_image()
            else:
                popup.text_update(f"{self.buttonMemory} n'est pas une combinaison possible !")
                popup.show()
            self.buttonMemory = []
            self.button_reset()
        self.victory_test()

    def button_reset(self):
        self.btn_1.setChecked(False)
        self.btn_2.setChecked(False)
        self.btn_3.setChecked(False)
        self.btn_4.setChecked(False)
        self.btn_5.setChecked(False)
        self.btn_6.setChecked(False)
        self.btn_7.setChecked(False)
        self.btn_8.setChecked(False)
        self.btn_9.setChecked(False)

    def moving_cells(self, cellsNb):
        cellsNb.sort()
        if cellsNb in constants.POSSIBLE_CHOICES:
            self.qim_image.moving_cells(cellsNb)
            return True
        else:
            return False
    
    def update_image(self):
        self.pxm_image = QtGui.QPixmap(self.qim_image).scaled(constants.SIZE_IMAGE, constants.SIZE_IMAGE, QtCore.Qt.KeepAspectRatio)
        self.label_image.setPixmap(self.pxm_image)

    def victory_test(self):
        if self.qim_image.__eq__(self.qim_image_saved):
            self.timer.stop()
            if self.time < self.bestTime:
                popup.text_update(f"Victoire en {self.time}s ! Un nouveau record !")
                self.save_data(self.time)
            else:
                popup.text_update(f"Victoire en {self.time}s !")
            popup.show()
            # self.close()

    def setup_timer(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.text_update)
        self.timer.setInterval(1000)
        self.timer.start()
        
    def text_update(self):
        self.time += 1
        self.label_text_1.setText(f"Temps : {self.time}s")

    def load_data(self):
        if not os.path.exists(constants.DATA_FILE):
            self.save_data(1000)
        with open(constants.DATA_FILE, "r") as f:
            data = f.read()
            if data.isdigit():
                return int(data)
            else:
                self.save_data(1000)
                return 1000

    def save_data(self, time):
        with open(constants.DATA_FILE, "w") as f:
            f.write(str(time))

    def reset_data(self):
        self.bestTime = 1000
        self.save_data(self.bestTime)
        self.btn_text_2.setText(f"Meilleur temps reset")
        



class AppPopup(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.resize(150, 50)
        
    def setup_ui(self):
        self.layout_base = QtWidgets.QHBoxLayout(self)
        self.label_text = QtWidgets.QLabel("")
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout_base.addWidget(self.label_text)

    def text_update(self, txt):
        self.label_text.setText(txt)



app = QtWidgets.QApplication([])

win = App()
popup = AppPopup()

win.show()
app.exec_()
