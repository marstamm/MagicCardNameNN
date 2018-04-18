#!/usr/bin/python3

import glob, os
from lxml import html 

os.chdir("./html")

string=''
for file in glob.glob("*"):
  xml = html.parse(file)
  for line in xml.xpath("//*/span[@class='cardTitle']/a/text()"):
    string += line + '\n'
open('../output', 'w').write(string)
