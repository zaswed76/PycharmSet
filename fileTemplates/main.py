#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class BaseWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.center = QtGui.QWidget()
        self.setCentralWidget(self.center)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = BaseWindow()
    main.show()
    sys.exit(app.exec_())