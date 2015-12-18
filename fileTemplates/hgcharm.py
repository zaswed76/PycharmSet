#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

name = "two_windows_view"
adr = "http://vrabey:fasadAQ*@bitbucket.org/vrabey/{}".format(name)

commands = (['hg', 'add'],
            ["hg", "commit"],
            ["hg", "push", adr])

for cmd in commands:
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.wait()