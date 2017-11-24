import numpy as np
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

class observation:
	def __init__(ID,Name,):
	
inputfile = open("data/basic.txt",'r')
data = []

input_type = inputfile.readline()
for line in inputfile:
	l = line.split()
	data.append(l)
print data[0]
