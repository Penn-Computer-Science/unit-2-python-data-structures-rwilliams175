import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pit

#load our dataframe
df = pd.read_csv('student_data.csv')
pennData = pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe")
print(pennData.head())

print("-_"*20)
print("Tail of the Dataframe")
print(pennData.tail())

print("-_"*20)
print("Summary of the Dataframe")
print(pennData.info())

print("-_"*20)
print("Statistics of the Dataframe")
print(round(pennData.describe()))

print("-_"*20)
print("Counts of Students in Pathways")
print(pennData['Pathway'].value_counts())

print("-_"*20)
print("Average GPA per Year")
print(pennData.groupby('Year')['GPA'].mean())

print("-_"*20)
print("Top 3 Students by GPA")
print(pennData.sort_values(by='GPA', ascending=False).head(3))

print("-_"*20)
print("Students with GPA greater than 3.5")
print(pennData[pennData['GPA']>3.5])

print("-_"*20)
print("First Student Data")
print(pennData.iloc[0])

