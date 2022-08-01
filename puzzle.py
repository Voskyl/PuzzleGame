from Projet_Image import *
from PySide2 import QtGui


class Puzzle(QtGui.QImage):
    def __init__(self, path_image):
        super().__init__(path_image)
        self.grid()
    
    def grid(self):
        for j in range(0, H):  # Barres verticales
            for i in range(91, 93+1):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))

            for i in range(185, 187+1):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))
        
        for i in range(0, W):  # Barres horizontales
            for j in range(67, 69+1):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))
            for j in range(137, 139+1):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))

    def moving_cells(self, cellNb):
        # Cases 1-2
        if cellNb == [1, 2]:
            self._move12() 

        # Cases 2-3
        if cellNb == [2, 3]:
            self._move23()

        # Cases 4-5
        if cellNb == [4, 5]:
            self._move45()

        # Cases 5-6
        if cellNb == [5, 6]:
            self._move56()

        # Cases 7-8
        if cellNb == [7, 8]:
            self._move78()

        # Cases 8-9
        if cellNb == [8, 9]:
            self._move89()

        # Cases 1-4
        if cellNb == [1, 4]:
            self._move14()

        # Cases 2-5
        if cellNb == [2, 5]:
            self._move25()

        # Cases 3-6
        if cellNb == [3, 6]:
            self._move36()

        # Cases 4-7
        if cellNb == [4, 7]:
            self._move47()

        # Cases 5-8
        if cellNb == [5, 8]:
            self._move58()

        # Cases 6-9
        if cellNb == [6, 9]:
            self._move69()

    def _move12(self):  # Déplacement des cases 1-2
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i-94, j-70)
                rgb_2 = self.pixel(i, j-70)
                self.setPixel(i, j-70, rgb_1) 
                self.setPixel(i-94, j-70, rgb_2) 

    def _move23(self):  # Déplacement des cases 2-3
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i, j-70)
                rgb_2 = self.pixel(i+94, j-70)
                self.setPixel(i+94, j-70, rgb_1)
                self.setPixel(i, j-70, rgb_2)
    
    def _move45(self):  # Déplacement des cases 4-5
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i-94, j)
                rgb_2 = self.pixel(i, j)
                self.setPixel(i, j, rgb_1)
                self.setPixel(i-94, j, rgb_2)
        
    def _move56(self):  # Déplacement des cases 5-6
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i, j)
                rgb_2 = self.pixel(i+94, j)
                self.setPixel(i+94, j, rgb_1)
                self.setPixel(i, j, rgb_2)
        
    def _move78(self):  # Déplacement des cases 7-8
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i, j+70)
                rgb_2 = self.pixel(i-94, j+70)
                self.setPixel(i-94, j+70, rgb_1)
                self.setPixel(i, j+70, rgb_2)

    def _move89(self):  # Déplacement des cases 8-9
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i, j+70)
                rgb_2 = self.pixel(i+94, j+70)
                self.setPixel(i+94, j+70, rgb_1)
                self.setPixel(i, j+70, rgb_2)

    def _move14(self):  # Déplacement des cases 1-4
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i-94, j)
                rgb_2 = self.pixel(i-94, j-70)
                self.setPixel(i-94, j-70, rgb_1)
                self.setPixel(i-94, j, rgb_2)

    def _move25(self):  # Déplacement des cases 2-5
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i, j)
                rgb_2 = self.pixel(i, j-70)
                self.setPixel(i, j-70, rgb_1)
                self.setPixel(i, j, rgb_2)

    def _move36(self):  # Déplacement des cases 3-6
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i+94, j)
                rgb_2 = self.pixel(i+94, j-70)
                self.setPixel(i+94, j-70, rgb_1)
                self.setPixel(i+94, j, rgb_2)

    def _move47(self):  # Déplacement des cases 4-7
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i-94, j)
                rgb_2 = self.pixel(i-94, j+70)
                self.setPixel(i-94, j+70, rgb_1)
                self.setPixel(i-94, j, rgb_2)

    def _move58(self):  # Déplacement des cases 5-8
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i, j)
                rgb_2 = self.pixel(i, j+70)
                self.setPixel(i, j+70, rgb_1)
                self.setPixel(i, j, rgb_2)

    def _move69(self):  # Déplacement des cases 6-9
        for j in range(70, 136+1):
            for i in range(94, 184+1):
                rgb_1 = self.pixel(i+94, j)
                rgb_2 = self.pixel(i+94, j+70)
                self.setPixel(i+94, j+70, rgb_1)
                self.setPixel(i+94, j, rgb_2)


if __name__ == "__main__":
    A = Puzzle("images/Citroen_2CV_3.jpg")
    A.moving_cells([1,2])
    A.save("h.jpg")