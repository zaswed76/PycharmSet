#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from functools import partial


class Tool(QtGui.QToolBar):
    def __init__(self, parent, meth):
        QtGui.QToolBar.__init__(self)
        self.meth = meth
        self.setFixedHeight(30)
        self.parent = parent
        self.but_tool = {}
        self.names = range(3)

        self.add_but()

    def add_but(self):
        for name in self.names:
            self.but_tool[name] = QtGui.QPushButton(str(name))
            self.but_tool[name].pressed.connect(
                partial(self.meth, name))
            self.addWidget(self.but_tool[name])(self.but_tool[name])