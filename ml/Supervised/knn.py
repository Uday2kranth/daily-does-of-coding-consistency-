import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#loading the data set 
iris =load_iris()
x=iris.data
y=iris.target
x_train , x_test,  y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# feature scaling (important for distance-based algorithms like KNN where we calculate Euclidean/Manhattan distance)
scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test) 

#initializing knn classifier model 
knn= KNeighborsClassifier(n_neighbors=3)
#train the model 
knn.fit(x_train,y_train)

#making the predictions use model with intialized on test data 
y_pred=knn.predict(x_test)

#evaluating the model accuracy
accuracy=accuracy_score(y_test,y_pred)
print(f"accuracy with k=3:- {accuracy:.4f}")
print(y[:5])   # prints the first 5 elements


print("Unique values in y:", np.unique(y))
print("Unique values in y_pred:", np.unique(y_pred))

