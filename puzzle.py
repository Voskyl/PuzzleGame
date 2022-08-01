from Projet_Image import *
from PySide2 import QtGui, QtCore


class Puzzle(QtGui.QImage):
    def __init__(self, path_image):
        super().__init__(path_image)
        self.w, self.h = self.size().width(), self.size().height()
        self.w_, self.h_ = int(self.w/3)+1, int(self.h/3)+1
        self.grid()

    def grid(self):
        for j in range(0, self.h):  # Barres verticales
            for i in range(int(self.w/3)-2, int(self.w/3)+1):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))

            for i in range(int(2*self.w/3)-1, int(2*self.w/3)+2):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))
        
        for i in range(0, self.w):  # Barres horizontales
            for j in range(int(self.h/3)-2, int(self.h/3)+1):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))
            for j in range(int(2*self.h/3)-1, int(2*self.h/3)+2):
                self.setPixel(i, j, QtGui.qRgb(255, 255, 255))

    def moving_cells(self, cellNb):
        for i in range(int(self.w/3)+1, int(2*self.w/3)-1):
            for j in range(int(self.h/3)+1, int(2*self.h/3)-1):

                if cellNb == [1, 2]:
                    rgb_1 = self.pixel(i-self.w_, j-self.h_)
                    rgb_2 = self.pixel(i, j-self.h_)
                    self.setPixel(i, j-self.h_, rgb_1) 
                    self.setPixel(i-self.w_, j-self.h_, rgb_2)  

                if cellNb == [2, 3]:
                    rgb_1 = self.pixel(i, j-self.h_)
                    rgb_2 = self.pixel(i+self.w_, j-self.h_)
                    self.setPixel(i+self.w_, j-self.h_, rgb_1)
                    self.setPixel(i, j-self.h_, rgb_2)
                
                if cellNb == [4, 5]:
                    rgb_1 = self.pixel(i-self.w_, j)
                    rgb_2 = self.pixel(i, j)
                    self.setPixel(i, j, rgb_1)
                    self.setPixel(i-self.w_, j, rgb_2)
                
                if cellNb == [5, 6]:
                    rgb_1 = self.pixel(i, j)
                    rgb_2 = self.pixel(i+self.w_, j)
                    self.setPixel(i+self.w_, j, rgb_1)
                    self.setPixel(i, j, rgb_2)

                if cellNb == [7, 8]:
                    rgb_1 = self.pixel(i, j+self.h_)
                    rgb_2 = self.pixel(i-self.w_, j+self.h_)
                    self.setPixel(i-self.w_, j+self.h_, rgb_1)
                    self.setPixel(i, j+self.h_, rgb_2)

                if cellNb == [8, 9]:
                    rgb_1 = self.pixel(i, j+self.h_)
                    rgb_2 = self.pixel(i+self.w_, j+self.h_)
                    self.setPixel(i+self.w_, j+self.h_, rgb_1)
                    self.setPixel(i, j+self.h_, rgb_2)
                
                if cellNb == [1, 4]:
                    rgb_1 = self.pixel(i-self.w_, j)
                    rgb_2 = self.pixel(i-self.w_, j-self.h_)
                    self.setPixel(i-self.w_, j-self.h_, rgb_1)
                    self.setPixel(i-self.w_, j, rgb_2)
                
                if cellNb == [2, 5]:
                    rgb_1 = self.pixel(i, j)
                    rgb_2 = self.pixel(i, j-self.h_)
                    self.setPixel(i, j-self.h_, rgb_1)
                    self.setPixel(i, j, rgb_2)

                if cellNb == [3, 6]:
                    rgb_1 = self.pixel(i+self.w_, j)
                    rgb_2 = self.pixel(i+self.w_, j-self.h_)
                    self.setPixel(i+self.w_, j-self.h_, rgb_1)
                    self.setPixel(i+self.w_, j, rgb_2)

                if cellNb == [4, 7]:
                    rgb_1 = self.pixel(i-self.w_, j)
                    rgb_2 = self.pixel(i-self.w_, j+self.h_)
                    self.setPixel(i-self.w_, j+self.h_, rgb_1)
                    self.setPixel(i-self.w_, j, rgb_2)

                if cellNb == [5, 8]:
                    rgb_1 = self.pixel(i, j)
                    rgb_2 = self.pixel(i, j+self.h_)
                    self.setPixel(i, j+self.h_, rgb_1)
                    self.setPixel(i, j, rgb_2)

                if cellNb == [6, 9]:
                    rgb_1 = self.pixel(i+self.w_, j)
                    rgb_2 = self.pixel(i+self.w_, j+self.h_)
                    self.setPixel(i+self.w_, j+self.h_, rgb_1)
                    self.setPixel(i+self.w_, j, rgb_2)


def init_image(path):
    image = QtGui.QImage(path)
    w, h = image.size().width(), image.size().height()
    if w % 3 == 1 :
        w -= 1
    if w % 3 == 2 :
        w += 1

    if h % 3 == 1 :
        h -= 1
    if h % 3 == 2 :
        h += 1

    return Puzzle(image.scaled(w, h))


if __name__ == "__main__":
    A = init_image("test2.jpg")
    print(A)
    A.save("h.jpg")