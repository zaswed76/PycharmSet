#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

widg_dict = {
    1: "Label",
    2: "FRAME",
    3: "StepButton"
}

RUN_WIDGET = widg_dict[1]


class Label(QtGui.QLabel):
    """
     __init__(self, QString, text,
              QWidget, parent = None,
              Qt.WindowFlags, flags = 0)
     """

    def __init__(self):
        QtGui.QLabel.__init__(self, parent=None,
                              flags=QtCore.Qt.Window)
        self.resize(300, 300)
        self.setText(u"Текст <b>полужирный</b>")
        self.setStyleSheet(
            'background-color: {0};'.format("lightblue"))


class FRAME(QtGui.QFrame):
    def __init__(self, parent=None):
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


class StepButton(QtGui.QPushButton):
    def __init__(self, text, parent=None):
        """

        @param text:
        @param parent:
        """
        QtGui.QPushButton.__init__(self, parent)
        self.setCheckable(True)
        self.setAutoExclusive(True)
        self.setText(text)
        # self.setMinimumWidth(cfg_step.width)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored,
                                       QtGui.QSizePolicy.Ignored)
        self.setSizePolicy(sizePolicy)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = eval(RUN_WIDGET + "()")
    main.show()
    sys.exit(app.exec_())