# SUPERWISED DATA
# %% Creating a LINEAR REGRESSION model
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data=pd.read_csv("student-mat.csv",sep=";")
data=data[["G1","G2","G3","studytime","failures","absences"]] # All the different attributes from which we're going to predict a label

predict="G3" # Our label i.e. the thing we're trying to predict

x=np.array(data.drop([predict],axis=1))
y=np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# We're taking all the attributes, and we are splitting them into 4 different variables.
# We're splitting 10% of the data into a testing data and 90% into training data. (That's what the test_size variable does)

linear=linear_model.LinearRegression() # We create our model
linear.fit(x_train,y_train) # Creating the best line fit
accuracy=linear.score(x_test,y_test) # Returns the accuracy of the best fit line 
print(accuracy) # When we run this it gives us an accuracy of ~87%

print("Coefficient:",linear.coef_) # Returns slope for each dimension(attribute)
print("Intercept:",linear.intercept_) # Returns the y-intercept 

predictions = linear.predict(x_test) # This will return the predicted values for the test data


for i in range(len(predictions)):
    print(predictions[i],x_test[i],y_test[i]) # We're printing the prediction, all our attributes, and the actual value
# Saving our model and plotting data

'''with open("studentmodel.pickle","wb") as f: # Saving our model
    pickle.dump(linear,f)''' 
# Un-comment this to make the pickle file

# Checking and saving the best model
'''best=0
for i in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    linear=linear_model.LinearRegression() # We create our model
    linear.fit(x_train,y_train) # Creating the best line fit
    accuracy=linear.score(x_test,y_test)
    print(accuracy)
    if accuracy>best:
        best=accuracy
        with open("studentmodel.pickle","wb") as f: 
            pickle.dump(linear,f)''' # Un-comment this to get the most efficient model

model=pickle.load(open("studentmodel.pickle","rb")) # Loading our model into variable called 'model'
# 'model' currently contains the model with the best accuracy we can get in 30 runs which is ~94% in this example

# Plotting data
style.use("ggplot")
p="G1"
pyplot.scatter(data[p],data["G3"]) # X axis,Y axis
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()

# %% Classifications - KNN
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model,preprocessing
import pandas as pd
import numpy as np

data=pd.read_csv("car.data")

# Since most of our data is non-integer, we use preprocessing to assign numeric values to our data
le=preprocessing.LabelEncoder() # Creating the object

# Now we create lists for each attribute and convert them into appropriate integers
buying=le.fit_transform(list(data["buying"]))
maint=le.fit_transform(list(data["maint"]))
door=le.fit_transform(list(data["door"]))
persons=le.fit_transform(list(data["persons"]))
lug_boot=le.fit_transform(list(data["lug_boot"]))
safety=le.fit_transform(list(data["safety"]))
cls=le.fit_transform(list(data["class"]))

predict="class" # Our label i.e. the thing we're trying to predict

x=list(zip(buying,maint,door,persons,lug_boot,safety))
y=list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=5) # Created the model with k=5
model.fit(x_train,y_train) # Training the model
accuracy=model.score(x_test,y_test) # Returns the accuracy of the best fit line 
print(accuracy) 

predictions=model.predict(x_test)
names=["unacc","acc","good","vgood"]

for x in range(len(predictions)):
    print(names[predictions[x]],x_test[x],names[y_test[x]]) # Predicted data,all attributes,actual data
    n=model.kneighbors([x_test[x]],9,True) # We're putting double brackets cos the function doesn't know how to look data which is not 2D
    print("N:",n)

# Saving the model
'''with open("cardata.pickle","wb") as f: 
    pickle.dump(model,f)
model=pickle.load(open("cardata.pickle","rb")) # Loading the model into an object'''
# %% Classification - SVM
import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

cancer = datasets.load_breast_cancer() # Loading in a built in dataset

print(cancer.feature_names) # Feature names
print(cancer.target_names) # Target names i.e. the thing we'll predict

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

classes=["malignant","benign"]

clf=svm.SVC(kernel="linear") # We can use poly for more accurate results, but then it takes way too long to run. We can try changing the degree instead
clf_2=svm.SVC(kernel="poly",degree=4) # New model with a poly of degree 4
clf_3=svm.SVC(kernel="linear",C=2) # C is the soft margin param. Defaulted to 1. C=0 for hard margin.

clf.fit(x_train,y_train)
clf_2.fit(x_train,y_train)
clf_3.fit(x_train,y_train)

y_pred=clf.predict(x_test)
y_pred_2=clf_2.predict(x_test)
y_pred_3=clf_3.predict(x_test)

accuracy1=metrics.accuracy_score(y_test,y_pred)
accuracy2=metrics.accuracy_score(y_test,y_pred_2)
accuracy3=metrics.accuracy_score(y_test,y_pred_3)

print("Accuracy 1: ",accuracy1)
print("Accuracy 2: ",accuracy2) # Adding the degree param here adds more complexity. We have a dataset which can easily be divided by a linear hyperplane, that's why the accuracy drops.
print("Accuracy 3: ",accuracy3) # Again, data is evenly divided, hence the doubling the soft margin doesn't do much
 
# Does using KNearestNeighbors make a difference?
clf_k=KNeighborsClassifier(n_neighbors=9)
clf_k.fit(x_train,y_train)
y_pred_k=clf_k.predict(x_test)
accuracy_k=metrics.accuracy_score(y_test,y_pred_k)
print("Accuracy K: ",accuracy_k)

# %% UNSUPERWISED DATA
# K Means Clustering
import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits # Our builtin dataset
from sklearn.cluster import KMeans
from sklearn import metrics

digits=load_digits() # Loading the data
data=scale(digits.data) # We're scaling down our data so that all the values are between -1 and 1
y=digits.target # Our labels
k=len(np.unique(y)) # Dynamic way of finding the number of clusters

samples,features=data.shape # Samples = number of rows, Features = number of columns

# We could manually score and fit the data, but then sklearn's sourcecode already has a better way to do that so we'll just use that
def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))

clf=KMeans(n_clusters=k,init="k-means++",n_init=10) # Read about the params here: https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation
bench_k_means(clf,"1",data) # (classifier,name,data)

# %%
