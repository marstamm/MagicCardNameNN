#!/usr/bin/python3
import json

data = json.load(open('AllCards-x.json'))
string = ''
for i in data:
  if ('types' in data[i]) and ('subtypes' in data[i]) and ('Creature' in data[i]['types']) and ('Dragon' in data[i]['subtypes']):
    string += data[i]['name'] + '\n'

open('dragons', 'w').write(string)
