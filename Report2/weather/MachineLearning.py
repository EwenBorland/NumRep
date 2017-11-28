

#Importing packages
import graphviz
import pickle

## sklearn classification packages
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier , RadiusNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.neural_network import MLPClassifier
#Loading weather data created from FeatureExtraction.py
weather = pickle.load(open('data/mldata.p'))


# Confirm that the data has loaded correctly by inspecting the data attributes in the `weather` object.
print weather.getNrEntries()
print weather.getTargetNames()
print weather.getFeatures()


## Step 2 - Define the training and testing sample
#
# Divide the weather data into a suitable training and testing sample.
# Start with a 50/50 split but make this easily adaptable for futher fitting evaluation.
#
# *Examples*:
# [`sklearn.model_selection.train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)



# DEFINE TRAINING AND TESTING SAMPLES AND TARGETS HERE

#separating the feature data from the weather type data
obs_types = []
print "total length all: {0}".format(len(weather.data))
for i in range(len(weather.data)):
	given_type  = weather.data[i][-1] 
	obs_types.append(given_type)
weather.delete('Weather Type')

#creating the test and train files
weather_train , weather_test, result_train, result_test= train_test_split(weather.data,obs_types,test_size=0.3)


# list of the classification methods to use
allclassifiers = [DecisionTreeClassifier,RandomForestClassifier,OneVsRestClassifier,RadiusNeighborsClassifier(radius=10.0)]
classifiers = [DecisionTreeClassifier(),RandomForestClassifier(),KNeighborsClassifier(n_neighbors=10),BaggingClassifier(KNeighborsClassifier(),max_samples=0.5, max_features=0.5),MLPClassifier()]
names = ["Decision Tree Classifier","Random Forest Classifier","K Nearest Neighbor Classifier","Bagging Classifier","MLP Classifier (Neural Network)"]
predictions = []

# creating predicted data sets for each classifier
# initialises a classifier, fits the classifier to the training set, then predicts a data set using the test data.
 
for classifier in classifiers:
	predictions.append(classifier.fit(weather_train,result_train).predict(weather_test))



## Step 6 - Prediction Evaluation

# Use the `sklearn.metrics` module to compare the results using the expected and predicted datasets.

# Examples:
# - [Sklearn Model Evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html#)
# - [Handwritten Digits example](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py)
#dot_data = export_graphviz(clf, out_file="clf1.dot")
# RUN PREDICTION EVALUATION METHODS HERE

#printing classification_report() results to the console for each classifier
for i in range(len(classifiers)):
	print "---------------------------------------------"
	#print classifiers[i].__name__
	print names[i]
	print classification_report(result_test,predictions[i])









