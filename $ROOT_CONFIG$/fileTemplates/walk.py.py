#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

dir = "/home/serg/0SYNC/foto/foto"
for root, dirs, files in os.walk(dir):    # пройти по директории рекурсивно
    for name in files:
      fullname = os.path.join(root, name) # получаем полное имя файла
      print os.path.getctime(fullname)                      # делаем что-нибудь с ним
