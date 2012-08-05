#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    import urllib
    import re
    stream = urllib.urlopen("http://usa.crazy-tronners.com/grid/onlineplayers.php").read()
    old_time = stream.split(';')[0]
    names = ''.join(stream.split(';')[1:]).split(', ')
    u_s = []
    p1 = re.compile('~\'U', re.IGNORECASE)
    p2 = re.compile('~`U', re.IGNORECASE)
    p3 = re.compile('~.\'U', re.IGNORECASE)
    p4 = re.compile('U~\'', re.IGNORECASE)
    p5 = re.compile('~\'.U', re.IGNORECASE)
    p6 = re.compile('\|EA$', re.IGNORECASE)
    length = int(len(names))
    for i in range(length):
        if p1.search(names[i]) or p2.search(names[i]) or p3.search(names[i]) or p4.search(names[i]) or p5.search(names[i]) or p6.search(names[i]):
            u_s.append("<p><font size=5px>"+names[i]+"</font></p>")
    if int(len(u_s)) != 0:
        return old_time + ":<br/>" + "<br/>".join(u_s)
    else:
        return "No one from ~'U is on tron"

if __name__ == "__main__":
    app.run('ix.lv-vl.net')
