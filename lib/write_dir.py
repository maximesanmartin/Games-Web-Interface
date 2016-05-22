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
    import requests
    from xml.etree import ElementTree
    
    response = requests.get(url.format(game))
    tree = ElementTree.fromstring(response.content)
    try:
        id = tree[1][0].text
        file.write(id+"\n") # ID
        print "{}: {}".format(game,id) 
    except:
        pass

file.close()
