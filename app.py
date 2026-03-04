from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load model
model = joblib.load("model.pkl")

# Feature extraction
def extract_features(url):
    suspicious_tlds = ["xyz", "tk", "ml", "ga", "cf"]
    suspicious_words = ["login", "secure", "update", "verify", "account", "bank"]

    return [
        len(url),
        url.count("."),
        1 if "https" in url else 0,
        1 if "@" in url else 0,
        1 if "-" in url else 0,
        1 if any(tld in url for tld in suspicious_tlds) else 0,
        1 if any(word in url.lower() for word in suspicious_words) else 0
    ]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    url = data["url"]
    features = extract_features(url)
    prediction = model.predict([features])[0]
    result = "This website appears to be suspicious." if prediction == 1 else "This website appears to be legitimate."
    return jsonify({"result": result})

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)