#Load the required libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#read the data from the file
ir = pd.read_csv('Iris.csv')

#Viewing the data
ir.sample(5)

#data type of values
ir.dtypes

#checking weather it cantains any missing values
ir.isnull().sum()

#Levels of the prediction column
ir['Species'].unique()

#counts the species values
ir["Species"].value_counts()

#removing the unwanted columns

ir = ir.drop(['Id'], axis = 1)

#understanding the central tendency of data
ir.describe()

#Summary of the data based on species
ir.groupby('Species').agg(['mean', 'median'])

"""#Histogram for Iris dataset"""

plt.figure(figsize = (7, 5)) 
x = ir["SepalLengthCm"] 
  
plt.hist(x, bins = 20, color = "green") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count")

plt.figure(figsize = (7, 5)) 
x = ir.SepalWidthCm 
  
plt.hist(x, bins = 20, color = "green") 
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count") 
  
plt.show()

plt.figure(figsize = (7, 5)) 
x = ir.PetalLengthCm 
  
plt.hist(x, bins = 20, color = "green") 
plt.title("Petal Length in cm") 
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count") 
  
plt.show()

plt.figure(figsize = (7, 5)) 
x = ir.PetalWidthCm 
  
plt.hist(x, bins = 20, color = "green") 
plt.title("Petal Width in cm") 
plt.xlabel("Petal_Width_cm") 
plt.ylabel("Count") 
  
plt.show()

"""For both petal length and petal width there seems to be a group of data points that have smaller values than the others.

#Box plot for Iris dataset
"""

#Box plot to understand how the distribution varies by class of flower.
#The graph represented the shape of data distribution and their upper and lower quartiles.

sns.set(style="ticks") 
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
sns.boxplot(x='Species',y='SepalLengthCm',data=ir)
plt.subplot(2,2,2)
sns.boxplot(x='Species',y='SepalWidthCm',data=ir)
plt.subplot(2,2,3)
sns.boxplot(x='Species',y='PetalLengthCm',data=ir)
plt.subplot(2,2,4)
sns.boxplot(x='Species',y='PetalWidthCm',data=ir)
plt.show()

"""Setosa has its petal mesurements smaller and less spread out than other species.There are notable 9 outliers.Working on identifying them.

#outlier detection by IQR method:
By using Inter Quartile Range(IQR), we detect outliers. IQR tells us the variation in the data set.Any value, which is beyond the range of -1.5 x IQR to 1.5 x IQR treated as outliers.

#outliers for setosa
"""

ir.loc[ir["Species"] == "Iris-setosa"] 
#print(ir.loc[data["Species"] == "Iris-setosa"])
sliced_data_setosa=ir[0:50] 
specific_data=sliced_data_setosa[["PetalLengthCm","PetalWidthCm","SepalLengthCm" , "SepalWidthCm", "Species"]] 

print("possible petallength outliers for setosa")
sample_setosa_petallength = sliced_data_setosa[["PetalLengthCm"]]
quartiles_setosa_petallength = np.percentile(sample_setosa_petallength, [5, 50, 95])
max_setosa_petallength = np.percentile(sample_setosa_petallength, 95)
min_setosa_petallength = np.percentile(sample_setosa_petallength, 5)
print("petallength max value for setosa:",max_setosa_petallength)
print("petallength min value for setosa:",min_setosa_petallength)
df_max_setosa_petallength = specific_data[specific_data.PetalLengthCm > max_setosa_petallength]
df_min_setosa_petallength = specific_data[specific_data.PetalLengthCm < min_setosa_petallength]
print(df_max_setosa_petallength)
print(df_min_setosa_petallength)

print("possible petalwidth outliers for setosa")
sample_setosa_petalwidth = sliced_data_setosa[["PetalWidthCm"]]
quartiles_setosa_petalwidth = np.percentile(sample_setosa_petalwidth, [5, 50, 95])
max_setosa_petalwidth = np.percentile(sample_setosa_petalwidth, 95)
min_setosa_petalwidth = np.percentile(sample_setosa_petalwidth, 5)
df_max_setosa_petalwidth = specific_data[specific_data.PetalWidthCm > max_setosa_petalwidth]
df_min_setosa_petalwidth = specific_data[specific_data.PetalWidthCm < min_setosa_petalwidth]
print("petalwidth max value for setosa:",max_setosa_petalwidth)
print("petalwidth min value for setosa:",min_setosa_petalwidth)
print(df_max_setosa_petalwidth)
print(df_min_setosa_petalwidth)

"""#outliers for versicolor"""

ir.loc[ir["Species"] == "Iris-versicolor"] 
#print(ir.loc[data["Species"] == "Iris-versicolor"])
sliced_data_versicolor=ir[50:100] 
specific_data_versicolor=sliced_data_versicolor[["PetalLengthCm","PetalWidthCm","SepalLengthCm" , "SepalWidthCm", "Species"]] 

print("possible petallength outliers for versicolor")
sample_versicolor_petallength = sliced_data_versicolor[["PetalLengthCm"]]
quartiles_versicolor_petallength = np.percentile(sample_versicolor_petallength, [5, 50, 95])
max_versicolor_petallength = np.percentile(sample_versicolor_petallength, 95)
min_versicolor_petallength = np.percentile(sample_versicolor_petallength, 5)
print("petallength max value for versicolor:",max_versicolor_petallength)
print("petallength min value for versicolor:",min_versicolor_petallength)
df_max_versicolor_petallength = specific_data_versicolor[specific_data_versicolor.PetalLengthCm > max_versicolor_petallength]
df_min_versicolor_petallength = specific_data_versicolor[specific_data_versicolor.PetalLengthCm < min_versicolor_petallength]
print(df_max_versicolor_petallength)
print(df_min_versicolor_petallength)

"""#outliers for virginica"""

ir.loc[ir["Species"] == "Iris-virginica"] 
#print(ir.loc[data["Species"] == "Iris-virginica"])
sliced_data_virginica=ir[100:150] 
specific_data_virginica=sliced_data_virginica[["PetalLengthCm","PetalWidthCm","SepalLengthCm" , "SepalWidthCm", "Species"]] 

print("possible sepallength outliers for virginica")
sample_virginica_sepallength = sliced_data_virginica[["SepalLengthCm"]]
quartiles_virginica_sepallength = np.percentile(sample_virginica_sepallength, [5, 50, 95])
max_virginica_sepallength = np.percentile(sample_virginica_sepallength, 95)
min_virginica_sepallength = np.percentile(sample_virginica_sepallength, 5)
print("sepallength max value for virginica:",max_virginica_sepallength)
print("sepallength min value for virginica:",min_virginica_sepallength)
df_max_virginica_sepallength = specific_data_virginica[specific_data_virginica.SepalLengthCm > max_virginica_sepallength]
df_min_virginica_sepallength = specific_data_virginica[specific_data_virginica.SepalLengthCm < min_virginica_sepallength]
print(df_max_virginica_sepallength)
print(df_min_virginica_sepallength)

print("possible sepalwidth outliers for virginica")
sample_virginica_sepalwidth = sliced_data_virginica[["SepalWidthCm"]]
quartiles_virginica_sepalwidth = np.percentile(sample_virginica_sepalwidth, [5, 50, 95])
max_virginica_sepalwidth = np.percentile(sample_virginica_sepalwidth, 95)
min_virginica_sepalwidth = np.percentile(sample_virginica_sepalwidth, 5)
df_max_virginica_sepalwidth = specific_data_virginica[specific_data_virginica.SepalWidthCm > max_virginica_sepalwidth]
df_min_virginica_sepalwidth = specific_data_virginica[specific_data_virginica.SepalWidthCm < min_virginica_sepalwidth]
print("sepalwidth max value for virginica:",max_virginica_sepalwidth)
print("sepalwidth min value for virginica:",min_virginica_sepalwidth)
print(df_max_virginica_sepalwidth)
print(df_min_virginica_sepalwidth)

new_iris = ir.drop(ir.index[[13, 22, 23, 24,43,44,98,106,117,109,131]]) 
new_iris.head()

new_iris.describe()

"""13, 22, 23, 24,43,44,98,106,117,109,131 these are the outliers in the dataset.As you can see, the mean and standard deviation there is no different between the models. It is best to keep the points as there are no potential outliers.

#scatter plot for Iris dataset
"""

ax = ir[ir.Species=='Iris-setosa'].plot.scatter(x='SepalLengthCm', y='SepalWidthCm', color='red', label='setosa')
ir[ir.Species=='Iris-versicolor'].plot.scatter(x='SepalLengthCm', y='SepalWidthCm', color='green', label='versicolor', ax=ax)
ir[ir.Species=='Iris-virginica'].plot.scatter(x='SepalLengthCm', y='SepalWidthCm', color='blue', label='virginica', ax=ax)
ax.set_title("fig 1- sepalwidth VS sepallength")

#scatter plot 
ax = ir[ir.Species=='Iris-setosa'].plot.scatter(x='PetalLengthCm', y='PetalWidthCm', color='red', label='setosa')
ir[ir.Species=='Iris-versicolor'].plot.scatter(x='PetalLengthCm', y='PetalWidthCm', color='green', label='versicolor', ax=ax)
ir[ir.Species=='Iris-virginica'].plot.scatter(x='PetalLengthCm', y='PetalWidthCm', color='blue', label='virginica', ax=ax)
ax.set_title("fig 2- petalwidth VS petallength")

ax = ir[ir.Species=='Iris-setosa'].plot.scatter(x='PetalLengthCm', y='SepalLengthCm', color='red', label='setosa')
ir[ir.Species=='Iris-versicolor'].plot.scatter(x='PetalLengthCm', y='SepalLengthCm', color='green', label='versicolor', ax=ax)
ir[ir.Species=='Iris-virginica'].plot.scatter(x='PetalLengthCm', y='SepalLengthCm', color='blue', label='virginica', ax=ax)
ax.set_title("fig 3- sepallength VS petallength")

ax = ir[ir.Species=='Iris-setosa'].plot.scatter(x='PetalWidthCm', y='SepalWidthCm', color='red', label='setosa')
ir[ir.Species=='Iris-versicolor'].plot.scatter(x='PetalWidthCm', y='SepalWidthCm', color='green', label='versicolor', ax=ax)
ir[ir.Species=='Iris-virginica'].plot.scatter(x='PetalWidthCm', y='SepalWidthCm', color='blue', label='virginica', ax=ax)
ax.set_title("fig 4- sepalwidth VS petalwidth")

data = ir.copy()
corr = data.corr()
sns.heatmap(corr , xticklabels=corr.columns.values , yticklabels=corr.columns.values)
plt.show()

ir['PetalLengthCm'].corr(ir['PetalWidthCm'])

ir['SepalLengthCm'].corr(ir['SepalWidthCm'])

ir['PetalLengthCm'].corr(ir['SepalLengthCm'])

ir['PetalWidthCm'].corr(ir['SepalWidthCm'])

"""

 By using sepal length VS sepal width and petallength VS petalwidth we can distinguish setosa flowers than that of Versicolor and Virginica. Separating versicolor and virginica is very much harder as they have considerable overlap.​Petal length vs. sepal length and petal width vs sepal width are not correlated when compared with Petal Width vs. Length which are highly correlated (positively).The  sepal length vs. Sepal width are also correlated(inversely).

"""
