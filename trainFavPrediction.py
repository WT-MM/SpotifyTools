from cProfile import label
from sklearn import svm
from sklearn.model_selection import train_test_split
import pickle
from neuralnet import *
import numpy as np
import pandas as pd


X = []
Y = []

favDF = pd.read_csv('localdata/favorites.csv')
print(favDF)
favDF.drop('Artist', axis=1, inplace=True)
favDF.drop('Name', axis=1, inplace=True)
favDF.drop('Date', axis=1, inplace=True)
favDF.drop('ID', axis=1, inplace=True)

#dislikeDF = pd.read_csv('localdata/dislike.csv')

#Definitely not using pandas correctly
for i in range(len(favDF.index)):
    X.append(list(favDF.iloc[i,:]))
    Y.append(1)
    #Temporary until real data gathered
    X.append([0,0,0,0,0,0,0,0,0,0,0])
    Y.append(0)
    
X_train, X_test, y_train, y_test = train_test_split(X,Y,train_size=0.8, random_state=0)


def makeSVM():
    clf = svm.SVC(decision_function_shape='ovo', probability=True)
    clf.fit(X_train,y_train)
    mm = clf.predict(X_test)
    acc = clf.score(X_test, y_test)

    #Have to tweak once more data is gathered
    tm = svm.SVC(decision_function_shape='ovo', C=5)
    tm.fit(X_train,y_train)
    tacc=tm.score(X_test,y_test)

    correct = []
    for i in range(len(X_test)):
        if mm[i] == y_test[i]:
            correct.append("YES")
        else:
            correct.append("NO")

    print("Accuracy: " + str(acc))
    print("Other Acc: " + str(tacc))
    #print(mm)
    #print("Comparison: ")
    #print(correct)

    with open('models/favSVM.pkl', 'wb') as f:
        pickle.dump(clf,f)
        
        
makeSVM()
     
'''   
def nn():
    if typ == "static":
        model = buildStatic(getStaticClasses())
    else:
        pass
    yT= staticEncode(y_train)
    yV = staticEncode(y_test)

    model.fit(X_train, yT.tolist(), epochs=75, batch_size=10)
    _, accuracy = model.evaluate(X_test, yV.tolist())
    
    prediction = model.predict([X_test[3]])[0]
    #Find the index of the largest value (probability) and feed into decoder
    predVal = np.argmax(prediction)
    interpret = decodeStatic([predVal])
    
    print("Accuracy: " + str(accuracy))
    print("Prediction: " + str(interpret))
    print("Prediction probability: " + str(prediction[predVal]))
    print("Actual: " + y_test[3])
    model.save("models/staticnet")
'''


