#!/usr/bin/python3

from numpy import array

def to_one_hot(list, alphabet):
  length=len(max(list, key=len))
  oneHotEncoded = []
  integerEncoded = []
  for line in list:
    currentLine=[]
    for char in line:
      letter = [0 for _ in range(len(alphabet))]
      letter[alphabet[char]] = 1
      currentLine.append(letter)
    while len(currentLine) < length:
      letter = [0 for _ in range(len(alphabet))]
      letter[alphabet['end']] = 1
      currentLine.append(letter)
    oneHotEncoded.append(currentLine)
  return oneHotEncoded

def getAlphabet(list):
  dict = {}
  index = 0
  for line in list:
    for char in line:
      if(char not in dict):
        dict[char] = index
        index += 1
  dict['end'] = index
  return dict

def getList(path):
  f=open(path)
  return [x.strip() for x in f.readlines()]

list = getList('input')
alph = getAlphabet(list)
oneHot = to_one_hot(list, alph)
