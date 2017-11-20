

## Step 1 - Import and Data loading

# Import the sklearn modules you intend to use as part of your Machine Learning analysis
# (e.g. classifiers, metrics, model selection)

import pickle
# ADD SKLEARN MODULES FOR YOUR CHOSEN CLASSIFICATION METHOD HERE
# e.g. to load the decision tree estimator use: from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Load the weather data you created by FeatureExtraction.py
weather = pickle.load(open('data/mldata.p'))

# Confirm that the data has loaded correctly by inspecting the data attributes in the `weather` object.

# ADD PRINT STATEMENTS HERE (SEE FeatureExtract.py FOR EXAMPLES)

## Step 2 - Define the training and testing sample
#
# Divide the weather data into a suitable training and testing sample.
# Start with a 50/50 split but make this easily adaptable for futher fitting evaluation.
#
# *Examples*:
# [`sklearn.model_selection.train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

# DEFINE TRAINING AND TESTING SAMPLES AND TARGETS HERE

## Step 3 - Define the classification method

# This can be any of the estimators provided by Sklearn.
# I suggest you start with a *white box* method
# to better understand the process before trying something more advanced.

# DEFINE CLASSIFIER HERE
# e.g for a Decision tree: clf = DecisionTreeClassifier()

## Step 4 - Fit the training data

# Run the `fit` method of your chosen estimator using the training data (and corresponding targets) as input

# RUN FIT METHOD HERE

## Step 5 - Define the expected and predicted datasets

# Define `expected` as your *test* target values (i.e. **not** your *training* target values)
# and run the `predict` method on your chosen estimator using your *test data*

# DEFINE EXPECTED AND PREDICTED VALUES HERE

## Step 6 - Prediction Evaluation

# Use the `sklearn.metrics` module to compare the results using the expected and predicted datasets.

# Examples:
# - [Sklearn Model Evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html#)
# - [Handwritten Digits example](http://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-auto-examples-classification-plot-digits-classification-py)

# RUN PREDICTION EVALUATION METHODS HERE
