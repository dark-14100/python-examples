# %% Pandas Series
import pandas as pd
data=[10,20,30,40] # Creating series using list
s=pd.Series(data)
print(s)
print(s[0]) # Accessing elements

s=pd.Series([10,20,30,40],index=['a','b','c','d']) # Adding index labels
print(s)
print(s['a']) # Accessing elements using index labels

data={"Maths":90,"Physics":80,"English":85} # Creating series using Dictionaries. Keys are the labels now
s=pd.Series(data)
print(s)
print(s['Maths']) # Accessing elements using index labels

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"]) # Accessing only a part of the series i.e. making a sub-series
print(myvar)
# %% Dataframes
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
 
# Locating rows in a Dataframe
print(df.loc[0]) # Returns the first row of the dataframe. Output is a series.
print(df.loc[0,1]) # Returns the first two rows of the dataframe. Output is a dataframe.

df=pd.DataFrame(data,index=["day1","day2","day3"]) # Adds custom labels instead of 0,1,2 etc
print(df)
# %% Reading from a csv file
import pandas as pd
df=pd.read_csv("data.csv")
print(df.to_string()) # to_string() is used to print the entire dataframe
print(df) # Prints only the first 5 rows and the last 5 rows
# %% Reading from a json file
import pandas as pd
df=pd.read_json("data.json")
print(df.to_string()) # to_string() is used to print the entire dataframe
print(df) # Prints only the first 5 rows and the last 5 rows
# %% Analysing Data
import pandas as pd
df=pd.read_csv("data.csv")
print(df.head(10)) # Returns the first 10 rows of the dataframe. Returns 5 by default
print(df.tail(10)) # Returns the last 10 rows of the dataframe. Returns 5 by default
print(df.info()) # Returns information about the dataframe
# %% Data Cleaning
import pandas as pd
# Cleaning Empty cells
df=pd.read_csv("workout_data_1.csv")
new_df=df.dropna() # Removes rows with missing values. Doesnt change the original dataframe
print(new_df.to_string())
new_df = df.dropna() # Removes rows with missing values. Doesnt change the original dataframe
print(new_df.to_string())

df=pd.read_csv("workout_data_2.csv")
new_df = df.fillna(130) # Fills missing values with 130. Doesnt change the original dataframe
print(new_df.to_string())
new_df = df.fillna({"Calories": 130}) # Fills missing values of only the Calories column with 130
print(new_df.to_string())

df = pd.read_csv('data.csv')
x = df["Calories"].mean() # Fill missing values with mean
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

df = pd.read_csv('data.csv')
x = df["Calories"].median() # Fill missing values with median
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

df = pd.read_csv('data.csv')
x = df["Calories"].mode() # Fill missing values with mode
new_df = df.fillna({"Calories": x})
print(new_df.to_string())

# Cleaning wrong formatting
df = pd.read_csv('data.csv') # Formatting the rows properly in the Date column 
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

df.dropna(subset=['Date'], inplace = True) # Removes rows with missing values in the Date column
print(df.to_string())

# Cleaning wrong data
df = pd.read_csv('data.csv')
df.loc[7,'Duration'] = 45 # Replaces the value in the Duration column of the 7th row with 45
print(df.to_string())

for x in df.index: # Applying a rule - usually used in large datasets
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120 # Replaces the value in the Duration column of the row where the value is greater than 120 with 120

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True) # Removes the row where the value is greater than 120
# %% Removing Duplicates
import pandas as pd

df = pd.read_csv('data.csv')
df.drop_duplicates(inplace = True) # Removes duplicate rows
print(df.to_string())

print(df.duplicated()) # Returns a boolean series
print(df.duplicated().sum()) # Returns the number of duplicate rows
# %% Correlation
df=pd.read_csv("data.csv")
print(df.corr()) # Returns the correlation of the dataframe
# Correlation only takes in non-string values
# %% Plotting
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
df.plot()
plt.show()

df.plot(kind="scatter",x="Duration",y="Calories") # Plots a scatterplot
plt.show()

df["Duration"].plot(kind="hist") # Plots a histogram. Histogram needs only one column
plt.show()