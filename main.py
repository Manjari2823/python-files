import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

math = np.array(df["math score"])
print(np.mean(math))
print(np.max(math))
print(np.min(math))
print(np.median(math))
print(np.std(math))

##pandas##

print(df["math score"].mean())
print(df["reading score"].mean())
print(df["writing score"].mean())
print(df["math score"].max())
print(df["math score"].min())

##bar plot##

subjects = ["Math","Reading","Writing"]

avg = [
df["math score"].mean(),
df["reading score"].mean(),
df["writing score"].mean()
]

plt.bar(subjects, avg)
plt.title("Average Scores")
plt.show()

##histogram ##

plt.hist(df["math score"])
plt.title("Math Score Distribution")
plt.show()

##scatter plot##

plt.scatter(df["math score"],df["reading score"])
plt.xlabel("Math")
plt.ylabel("Reading")
plt.show()

##line plot##
plt.plot(df["math score"])
plt.title("Math Scores")
plt.show()

##pie##
labels=["Math","Reading","Writing"]

values=[
df["math score"].mean(),
df["reading score"].mean(),
df["writing score"].mean()
]

plt.pie(values,labels=labels,autopct="%1.1f%%")
plt.show()

print("Dataset Analysis Completed Successfully")