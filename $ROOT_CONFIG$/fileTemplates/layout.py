#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore

from functools import partial


class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        """
        addWidget(<Компонент>, <Строка>, <Столбец>[, alignment=0])
        addWidget(<Компонент>, <Строка>, <Столбец>, <Количество строк>,
        <Количество столбцов>[, alignment=0])

        """
        QtGui.QMainWindow.__init__(self)

        self.Centr = QtGui.QWidget()
        self.setCentralWidget(self.Centr)

        button1 = QtGui.QPushButton("1")
        button2 = QtGui.QPushButton("2")
        button3 = QtGui.QPushButton("3")

        grid = QtGui.QGridLayout()
        grid.addWidget(button1, 0, 0)
        grid.addWidget(button2, 0, 1, alignment=QtCore.Qt.AlignLeft)
        grid.addWidget(button3, 1, 0, 1, 2)


        grid.setMargin(0)
        grid.setSpacing(0)

        self.Centr.setLayout(grid)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())