import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import pydotplus
import matplotlib.image as pltimg
import graphviz
from sklearn.tree import export_graphviz
from subprocess import call
import collections
import pickle
import tkinter as tk
from tkinter import ttk
from PIL import Image as imagee
from PIL import *
from tkinter import *
from dtreeviz.trees import dtreeviz


obesity  = pd.read_csv("C:\\Users\\minel\\OneDrive\\Masaüstü\\hacettepe yl\\ObesityDataSet_raw_and_data_sinthetic.csv")

print(obesity.columns)

d = {'Female': 1, 'Male': 0}
obesity['Gender'] = obesity['Gender'].map(d)

d = {'yes': 1, 'no': 0}
obesity['family_history_with_overweight'] = obesity['family_history_with_overweight'].map(d)
obesity['FAVC'] = obesity['FAVC'].map(d)
obesity['SMOKE'] = obesity['SMOKE'].map(d)
obesity['SCC'] = obesity['SCC'].map(d)


d = {'no': 0, 'Sometimes': 1, 'Frequently': 2, 'Always':3}
obesity['CAEC'] = obesity['CAEC'].map(d)
obesity['CALC'] = obesity['CALC'].map(d)

d = {'Automobile': 0, 'Motorbike': 1, 'Public_Transportation': 2, 'Bike':3, 'Walking':4}
obesity['MTRANS'] = obesity['MTRANS'].map(d)

d = {'Insufficient_Weight': 0, 'Normal_Weight': 1, 'Obesity_Type_I': 2, 'Obesity_Type_II':3,
     'Obesity_Type_III':4, 'Overweight_Level_I':5, 'Overweight_Level_II':6}
obesity['NObeyesdad'] = obesity['NObeyesdad'].map(d)

features = ['Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight',
       'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 'TUE',
       'CALC', 'MTRANS']

cn = ['Insufficient_Weight', 'Normal_Weight', 'Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III',
       'Overweight_Level_I', 'Overweight_Level_II']

X = obesity[features]
y = obesity['NObeyesdad']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

classifier = DecisionTreeClassifier(max_depth = 5, 
                             random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
a = metrics.accuracy_score(y_test, y_pred)

#Model = pickle.dumps(model)


fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
tree.plot_tree(classifier,
               feature_names=features, 
               class_names=cn,
               filled = True);
fig.savefig('cls_individualtree.png')

text_representation = tree.export_text(classifier)
print(text_representation)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

viz = dtreeviz(classifier, X, y,
                target_name="target",
                feature_names=features,
                class_names=cn)

viz.save("decision_tree3.svg")





