

#Importing packages
import graphviz
import pickle

## sklearn classification packages
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier , RadiusNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
#Loading weather data created from FeatureExtraction.py
weather = pickle.load(open('data/mldata.p'))

# Confirm that the data has loaded correctly by inspecting the data attributes in the `weather` object.
print weather.getNrEntries()
print weather.getTargetNames()
print weather.getFeatures()


# DEFINE TRAINING AND TESTING SAMPLES AND TARGETS HERE

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
classifiers = [DecisionTreeClassifier(),RandomForestClassifier(),MLPClassifier(hidden_layer_sizes=(100,100,100, ),solver='adam'),KNeighborsClassifier(n_neighbors=100,weights='distance'),GradientBoostingClassifier()]
names = ["Decision Tree Classifier","Random Forest Classifier","MLP Classifier (Neural Network)","K Nearest Neighbor Classifier","Gradient Boosting"]
predictions = []

# creating predicted data sets for each classifier
# initialises a classifier, fits the classifier to the training set, then predicts a data set using the test data.
ntot = 10
runresults = []
nruns=0
while nruns < ntot:	 
	for classifier in classifiers:
		predictions.append(classifier.fit(weather_train,result_train).predict(weather_test))
	runresults.append(predictions)
	print "Run {0} complete".format(nruns)
	nruns +=1

## Step 6 - Prediction Evaluation

#printing classification_report() results to the console for each classifier in the first run
for i in range(len(classifiers)):
	print "---------------------------------------------"
	#print classifiers[i].__name__
	print names[i]
	print classification_report(result_test,runresults[0][i])

runsreport = []

for j in range(ntot):
	runreport = []
	for i in range(len(classifiers)):
		runreport.append([i,precision_recall_fscore_support(result_test,runresults[j][i])])
	runsreport.append(runreport)

classresultlists = []

for i in runsreport:
	precrecfsup = []
	for j in i:
		#i is a classifier, j is the precision, recall ...
		precrecfsup.append(j)
	classresultlists.append(precrecfsup)
print classresultlists
#classresultlist[q][r][s] corresponds to run


