import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Load dataset and model
data = pd.read_csv("data/iris.csv")
X = data.drop("species", axis=1)
y = data["species"]
model = joblib.load("models/iris_model.pkl")

# Evaluate
predictions = model.predict(X)
acc = accuracy_score(y, predictions)
print(f"✅ Model Accuracy: {acc:.2f}")
