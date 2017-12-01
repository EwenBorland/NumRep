

#Importing packages
import graphviz
import pickle
import numpy as np
## sklearn classification packages

from sklearn.tree import export_graphviz
from sklearn import tree
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split


from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
import time 
#Loading weather data created from FeatureExtraction.py
weather = pickle.load(open('data/mldata.p'))

# Confirm that the data has loaded correctly by inspecting the data attributes in the `weather` object.
print weather.getNrEntries()
print weather.getTargetNames()
print weather.getFeatures()

#separating the feature data from the weather type data
obs_types = []
print "total length all: {0}".format(len(weather.data))
for i in range(len(weather.data)):
	given_type  = weather.data[i][-1] 
	obs_types.append(given_type)
weather.delete('Weather Type')

#creating the test and train files
trainsize = 0.5
weather_train , weather_test, result_train, result_test= train_test_split(weather.data,obs_types,train_size=trainsize)


# list of the classification methods to use
classifiers = [DecisionTreeClassifier(max_depth=10),RandomForestClassifier(),MLPClassifier(hidden_layer_sizes=(100,100,100, ),solver='adam'),KNeighborsClassifier(n_neighbors=100,weights='distance'),GradientBoostingClassifier()]
names = ["Decision Tree Classifier","Random Forest Classifier","MLP Classifier (Neural Network)","K Nearest Neighbor Classifier","Gradient Boosting"]
predictions = []

#clf = DecisionTreeClassifier().fit(weather_train,result_train)
#dot_data = tree.export_graphviz(clf, out_file="dectree.dot",feature_names=weather.getFeatures(),class_names=["0","1","2"])


# creating predicted data sets for each classifier
# initialises a classifier, fits the classifier to the training set, then predicts a data set using the test data.
ntot = 15
runresults = []
nruns=0
while nruns < ntot:	 
	t1 = time.time()
	for classifier in classifiers:
		predictions.append(classifier.fit(weather_train,result_train).predict(weather_test))
	runresults.append(predictions)
	print "Run {0} complete, time = {1}s".format(nruns,(time.time()-t1))
	nruns +=1

## Step 6 - Prediction Evaluation

#printing classification_report() results to the console for each classifier in the first run
for i in range(len(classifiers)):
	print "---------------------------------------------"
	#print classifiers[i].__name__
	print names[i]
	print classification_report(result_test,runresults[5][i])

#creating a list of empty lists, each empty list represents a classifier
classifier_lists = [[] for _ in range(len(classifiers))]

#loop to get the accuracy information in each run and organise into the classifier lists
for j in range(len(classifier_lists)):
	for i in runresults:
		classifier_lists[j].append(precision_recall_fscore_support(result_test,i[j]))

classifier_avelist = []

for i in range(len(classifier_lists)):
	prec = []
	reca = []
	for j in classifier_lists[i]:
		prec.append(np.average(j[0]))
		reca.append(np.average(j[1]))
	classifier_avelist.append([np.average(prec),np.average(reca)])
	
print classifier_avelist


'''



