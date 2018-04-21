#!/usr/bin/python3

import numpy as np
import random
from sklearn.neural_network import BernoulliRBM

def stringToTrainData(string, charToInt, maxWordLength):
  charLength = len(charToInt)
  result = [0] * maxWordLength * len(charToInt)
  for i in range(0, maxWordLength):
    if(i < len(string)):
      result[i*charLength + charToInt[string[i]]] = 1
    else:
      result[i*charLength + charToInt['#']] = 1
  return result


def trainDataToString(word, charToInt):
  size = len(charToInt)
  intToChar = dict((v,k) for k,v in charToInt.items())
  chars = [word[i:i+size] for i  in range(0, len(word), size)]
  result = ''
  for char in chars:
    intChar = [i for i,x in enumerate(char) if x == True]
    if (len(intChar) == 0):
      #should nor happen
      result += '?'
    else:
      result += intToChar[intChar[0]]
  return result


def getAlphabet(list):
  dict = {}
  index = 0
  for line in list:
    for char in line:
      if(char not in dict):
        dict[char] = index
        index += 1
  dict['#'] = index
  return dict


def getList(path):
  f=open(path)
  return [x.strip() for x in f.readlines()]


def createRandomWord(charToInt, length):
  result = ''
  for i in range(length):
    result += random.choice(list(charToInt.keys()))
  return result

wordList = getList('/home/granor/code/magic/input_short')
longestWord=len(max(wordList, key=len))
charToInt = getAlphabet(wordList)
trainData = []

for line in wordList:
  trainData.append(stringToTrainData(line, charToInt, longestWord))

X = np.array(trainData)
model = BernoulliRBM(n_components=128,n_iter=200,verbose=1)
model.fit(X)

lastModel = stringToTrainData(createRandomWord(charToInt, longestWord), charToInt, longestWord)
print(trainDataToString(lastModel, charToInt))
for i in range(0,25):
  lastModel = model.gibbs(lastModel)
  print(trainDataToString(lastModel, charToInt))


print(trainDataToString(lastModel, charToInt))
