import numpy as np
import pandas as pd
from sklearn import *
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score
df = pd.read_csv('providerset.csv')
df["Comp_Fact1"] = df["Comp_Fact1"].map({'HardwareCompatiable':1,'HardwareInCompatiable':0})
df["Comp_Fact2"] = df["Comp_Fact2"].map({'HSCompatiable':1,'HSInCompatiable':0})
df["Comp_Fact3"] = df["Comp_Fact3"].map({'SoftwareCompatiable':1,'SoftwareInCompatiable':0})
df["Comp_Fact4"] = df["Comp_Fact4"].map({'DefinedCapabilities':1,'UnDefinedCapabilities':0})
df["Comp_Fact5"] = df["Comp_Fact5"].map({'DefinedRequirements':1,'UnDefinedRequirements':0})
df["SH_Fact6"] = df["SH_Fact6"].map({'Scalable':1,'NotScalable':0})
df["SH_Fact7"] = df["SH_Fact7"].map({'HighVariety':1,'LowVariety':0})
df["SH_Fact8"] = df["SH_Fact8"].map({'DefinedProtocols':1,'UnDefinedProtocols':0})
df["SH_Fact9"] = df["SH_Fact9"].map({'NoDeadLocks':1,'DeadLocks':0})
df["Qlty_Fact10"] = df["Qlty_Fact10"].map({'Autonomous':1,'NonAutonomous':0})
df["Qlty_Fact11"] = df["Qlty_Fact11"].map({'AutDivVal':1,'NoAutDivVal':0})
df["Qlty_Fact12"] = df["Qlty_Fact12"].map({'DefinedOwnership':1,'UnDefinedOwnership':0})
df["Qlty_Fact13"] = df["Qlty_Fact13"].map({'DefinedControls':1,'UnDefinedControls':0})
df["Reputation"] = df["Reputation"].map({'LowReputation':0,'GoodReputation':1,'VeryGoodReputation':2})
data = df[["Comp_Fact1","Comp_Fact2","Comp_Fact3","Comp_Fact4","Comp_Fact5","SH_Fact6","SH_Fact7","SH_Fact8","SH_Fact9","Qlty_Fact10","Qlty_Fact11","Qlty_Fact12","Qlty_Fact13","Reputation"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:400]
training_outputs = outputs[:400]
testing_inputs = inputs[400:]
testing_outputs = outputs[400:]
classifier = QuadraticDiscriminantAnalysis()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of QDAClassifier Classifier on testing data is: " + str(accuracy))
testSet = [[1,0,0,0,0,0,1,0,0,0,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDAClassifier Prediction on the first test set is:',predictions)
testSet = [[1,1,0,0,1,0,1,0,1,0,0,1,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDAClassifier Prediction on the second test set is:',predictions)
testSet = [[1,1,1,1,1,0,1,1,1,1,0,1,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('QDAClassifier Prediction on the third test set is:',predictions)