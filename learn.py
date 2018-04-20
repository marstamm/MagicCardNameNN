#!/usr/bin/python3

import numpy as np
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
  print(len(word))
  size = len(charToInt)
  intToChar = dict((v,k) for k,v in charToInt.items())
  chars = [word[i:i+size] for i  in range(0, len(word), size)]
  result = ''
  for char in chars:
    intChar = [i for i,x in enumerate(char) if x == True]
    if (len(intChar) == 0):
      #should nor happen
      intChar = len(intToChar) - 1
    else:
      intChar = intChar[0]
    result += intToChar[intChar]
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

list = getList('/home/granor/code/test')
longestWord=len(max(list, key=len))
charToInt = getAlphabet(list)
trainData = []

for line in list:
  trainData.append(stringToTrainData(line, charToInt, longestWord))



X = np.array(trainData)
model = BernoulliRBM(n_components=10,n_iter=10000)
model.fit(X)

lastModel = len(trainData[2])
for i in range(0,100):
  lastModel = model.gibbs(lastModel)


print(trainDataToString(lastModel, charToInt))
