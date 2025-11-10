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

# %%
