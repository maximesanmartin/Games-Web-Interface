# -*- coding: utf-8 -*-
import os
import sys

""" ================= FOR SPYDER ==================== """
#sys.argv.append("../samples")

if len(sys.argv) < 2:
    sys.exit("Usage : python write_dir.py <directory>")
rep = sys.argv[1]
games = os.listdir(rep)

""" Request for Games API """
file = open("../data/ids.txt", "w")
url = "http://thegamesdb.net/api/GetGame.php?name={}&platform=PC"
for game in games:
    print game
    import requests
    from xml.etree import ElementTree
    
    response = requests.get(url.format(game))
    tree = ElementTree.fromstring(response.content)
    try:
        file.write(tree[1][0].text+"\n") # ID
    except:
        pass

file.close()
