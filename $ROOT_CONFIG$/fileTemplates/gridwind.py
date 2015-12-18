# coding=utf-8
import sys
from PyQt4 import QtGui, QtCore

from functools import partial


class FRAME(QtGui.QFrame):
    def __init__(self,parent=None):
        """
        рамка вокруг основных компонентов
        Plain — 16 — нет эффектов;
        Raised — 32 — панель отображается выпуклой;
        Sunken — 48 — панель отображается вогнутой;
        
        NoFrame — 0 — нет рамки;
        Box — 1 — прямоугольная рамка;
        Panel — 2 — панель, которая может быть выпуклой или вогнутой;
        WinPanel — 3 — панель со стилем, принятым в Windows. Ширина
        границы 2

        """
        QtGui.QFrame.__init__(self, parent)
        self.setFrameShape(QtGui.QFrame.Box)
        self.setFrameShadow(QtGui.QFrame.Plain)
        self.setLineWidth(1)
        self.setMidLineWidth(1)


        self.setStyleSheet('color: {0};'.format('#6E6E6E'))

class Grid:
    def __init__(self, parent=None, set=None):

        self.widget = FRAME()
        self.widget.setStyleSheet('background-color: {0};'
                                  .format("lightgrey"))
        self.parent = parent
        self.set = set
        x = self.set["geometry"]["base"]["width"]
        y = self.set["geometry"]["base"]["height"]
        # self.widget.setFixedSize(x, y)
        # grid = QtGui.QGridLayout(self.widget)
        # button1 = QtGui.QPushButton("1")
        # button2 = QtGui.QPushButton("1")
        # button3 = QtGui.QPushButton("1")
        # grid.addWidget(button1)
        # grid.addWidget(button2)
        # grid.addWidget(button3)


    def __call__(self, *args, **kwargs):
        return self.widget



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Grid()
    main.show()
    sys.exit(app.exec_())