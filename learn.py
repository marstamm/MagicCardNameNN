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

def speak(model, charToInt):
  lastModel = stringToTrainData(createRandomWord(charToInt, longestWord), charToInt, longestWord)
  bestResult =  [lastModel, model.score_samples([lastModel])]
  #print(trainDataToString(lastModel, charToInt))
  for i in range(0,25):
    lastModel = model.gibbs(lastModel)
    score = model.score_samples([lastModel])
    if score > bestResult[1]:
      bestResult = [lastModel, score]
    print(trainDataToString(bestResult[0], charToInt) , bestResult[1])
  return trainDataToString(bestResult[0], charToInt)

def train(data, nComp, nIter):
  X = np.array(trainData)
  model = BernoulliRBM(n_components=nComp,n_iter=nIter,verbose=1)
  model.fit(X)
  return model

wordList = getList('/home/granor/code/magic/humans')
longestWord=len(max(wordList, key=len))
charToInt = getAlphabet(wordList)
trainData = []

for line in wordList:
  trainData.append(stringToTrainData(line, charToInt, longestWord))

train(trainData, 124, 100)

print(speak(model, charToInt))
