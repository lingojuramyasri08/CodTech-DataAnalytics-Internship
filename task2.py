# TASK 2 - MACHINE LEARNING USING TITANIC DATASET

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("titanic.csv")

# Select useful columns
df = df[['Pclass', 'Sex', 'Age', 'Survived']]

# Convert male/female into numbers
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Remove missing values
df = df.dropna()

# Input data
X = df[['Pclass', 'Sex', 'Age']]

# Output data
y = df['Survived']

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create machine learning model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict using test data
predictions = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Example prediction
example = pd.DataFrame([[3, 1, 21]],
columns = ['Pclass','Sex','Age'])

result = model.predict(example)

print("\nPrediction for Passenger:")
print("Passenger Class = 3")
print("Gender = Female")
print("Age = 21")

if result[0] == 1:
    print("Prediction: Survived")
else:
    print("Prediction: Not Survived")