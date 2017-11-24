

## Step 1 - Import and Data loading

# Import the sklearn modules you intend to use as part of your Machine Learning analysis
# (e.g. classifiers, metrics, model selection)
import graphviz
import pickle
# ADD SKLEARN MODULES FOR YOUR CHOSEN CLASSIFICATION METHOD HERE
# e.g. to load the decision tree estimator use: from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
# Load the weather data you created by FeatureExtraction.py
weather = pickle.load(open('data/mldata.p'))
print weather.data[0]

# Confirm that the data has loaded correctly by inspecting the data attributes in the `weather` object.
print weather.getNrEntries()
print weather.getTargetNames()
print weather.getFeatures()
#print weather.data

## Step 2 - Define the training and testing sample
#
# Divide the weather data into a suitable training and testing sample.
# Start with a 50/50 split but make this easily adaptable for futher fitting evaluation.
#
# *Examples*:
# [`sklearn.model_selection.train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

# DEFINE TRAINING AND TESTING SAMPLES AND TARGETS HERE
classifications = []
print "total length all: {0}".format(len(weather.data))
for i in range(len(weather.data)):
	classification  = weather.data[i][-1] 
	classifications.append(classification)
weather.delete('Weather Type')
weather_train , weather_test, result_train, result_test= train_test_split(weather.data,classifications,test_size=0.5)
print "total length train: {0}".format(len(weather_train))
print "total length test: {0}".format(len(weather_test))
print "total length result train: {0}".format(len(result_train))
print "total length result test: {0}".format(len(result_test))

#print weather.data
#print classifications
## Step 3 - Define the classification method

# This can be any of the estimators provided by Sklearn.
# I suggest you start with a *white box* method
# to better understand the process before trying something more advanced.

# DEFINE CLASSIFIER HERE
# e.g for a Decision tree: clf = DecisionTreeClassifier()
clf = DecisionTreeClassifier()
clf1 = RandomForestClassifier()
pred2 = OneVsRestClassifier(LinearSVC(random_state=0)).fit(weather_train,result_train).predict(weather_test)

## Step 4 - Fit the training data

# Run the `fit` method of your chosen estimator using the training data (and corresponding targets) as input
clf.fit(weather_train,result_train)
clf1.fit(weather_train,result_train)

# RUN FIT METHOD HERE

## Step 5 - Define the expected and predicted datasets

# Define `expected` as your *test* target values (i.e. **not** your *training* target values)
# and run the `predict` method on your chosen estimator using your *test data*

# DEFINE EXPECTED AND PREDICTED VALUES HERE
pred = clf.predict(weather_test)
pred1 = clf1.predict(weather_test)
#dot_data = export_graphviz(clf, out_file="clf1.dot")
#pred2 = clf2.predict(weather_test)
print pred2
print "Decision Tree"
print classification_report(result_test,pred)
print "\nRandom Forest Class"
print classification_report(result_test,pred1)
print "\nOneVsRest Classifier"
print classification_report(result_test,pred2)

## Step 6 - Prediction Evaluation

# Use the `sklearn.metrics` module to compare the results using the expected and predicted datasets.

# Examples:
# - [Sklearn Model Evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html#)
# - [Handwritten Digits example](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py)

# RUN PREDICTION EVALUATION METHODS HERE
