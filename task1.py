# TASK 1 - BIG DATA ANALYSIS USING DASK

# Import libraries
import dask.dataframe as dd
import matplotlib.pyplot as plt

# Load Titanic dataset
df = dd.read_csv("titanic.csv")

# Show first 5 rows
print("Fisrt 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Columns:")
print(df.columns)

# Average age of passengers
average_age = df['Age'].mean().compute()

print("\nAverage Age:")
print(average_age)

# Survival count
survival_count = df['Survived'].value_counts().compute()

print("\nSurvival Count:")
print(survival_count)

# Survival rate by gender
gender_survival = df.groupby('Sex')['Survived'].mean().compute()

print("\nSurvival Rate by Gender:")
print(gender_survival)

# Plot graph
gender_survival.plot(kind='bar')

plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")

plt.show()