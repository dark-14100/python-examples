# %% Displot - Shows how many times an element is occuring in an array
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],bins=20) # Creates 20 divisions
plt.show()

sns.displot([1,2,3,4,5,6],kind="kde") # Plots a probability density function
plt.show()

# %% Normal Distributions - Plots a normal distributtion
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x) # Returns a 2x3 array with elements from a normal distribution with mean(loc) 1 and standard deviation(scale) 2

# Plotting the normal distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Normal Distribution")
plt.show()
# %% Binomial Distributions - Plots a binomial distribution, discrete
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.binomial(n=10, p=0.5, size=100)
print(x) 
# Returns a 1D array. Each element represents, say number of heads in a coin toss of 10 coins. Number of elements shows the number of times this has been repeated

# Plotting the binomial distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Binomial Distribution")
plt.show()
# With enough data points, a normal distibution and binomial can and will overlap
# %% Poisson Distributions - Discrete
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.poisson(lam=2, size=100)
print(x) 

# Plotting the poisson distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Poisson Distribution")
plt.show()
# %% Uniform Distributions - All elements have an equal chance of occuring
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.uniform(low=0, high=1, size=100) # low and high are set to 0 and 1 respectively by default
print(x) 

# Plotting the uniform distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Uniform Distribution")
plt.show()
# %% Logistic Distributions - Used to describe growth
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2,3))
print(x) 

# Plotting the logistic distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Logistic Distribution")
plt.show()

# Difference between logistic distributions and normal distributions: 
# Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}

sns.displot(data, kind="kde")
plt.show()
# %% Multinomial Distributions - Extension of binomial distribution
from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x) # Die Roll
# %% Exponential Distributions - Describes the time b/w another event occurs. Scale is the inverse of lam in poisson
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.exponential(scale=2, size=(2,3))
print(x)

# Plotting the exponential distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Exponential Distribution")
plt.show()

# Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events.
# %% Chisquare distributions - A Chi-square distribution measures how much variation (or deviation) there is in your data
# Sum of squares of random variables
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.chisquare(df=2, size=(2,3)) # Degree of freedom = df. 
print(x)

# Plotting the chisquare distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Chi-square Distribution")
plt.show()
# %% Rayleigh Distributions - The Rayleigh distribution models the magnitude (length) of a 2D vector whose components are independent standard normal variables.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.rayleigh(scale=2, size=(2,3)) # Scale is 1.0 by default
print(x)

# Plotting the rayleigh distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Rayleigh Distribution")
plt.show()
# %% Pareto Distributions - A distribution following Pareto's law i.e. 80-20 distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.pareto(a=2, size=(2,3)) # a is the shape parameter. Shows how fast the graph falls
print(x)

# Plotting the pareto distribution
sns.displot(x.flatten(), kind="kde")
plt.title("Pareto Distribution")
plt.show()
# %% Zipf Distributions - In many natural datasets, the frequency of an item is inversely proportional to its rank.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.zipf(a=2, size=(2,3)) # a is the shape parameter
print(x)

# Plotting the zipf distribution
sns.displot(x, kind="kde")
plt.title("Zipf Distribution")
plt.show()