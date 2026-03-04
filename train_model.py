import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Simple training data (you can expand later)
data = [
    # length, dots, https, @, -, suspicious_tld, suspicious_word, label
    [20, 2, 1, 0, 0, 0, 0, 0],  # normal
    [45, 3, 0, 1, 1, 1, 1, 1],  # phishing
    [30, 2, 1, 0, 1, 0, 1, 1],  # phishing
    [18, 1, 1, 0, 0, 0, 0, 0],  # normal
]

df = pd.DataFrame(data, columns=[
    "length", "dots", "https", "@", "-", "suspicious_tld", "suspicious_word", "label"
])

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model retrained successfully!")