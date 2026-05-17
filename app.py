from flask import Flask, render_template, request
import joblib

# ---------------------------------------------------
# Create Flask application
# ---------------------------------------------------
app = Flask(__name__)

# ---------------------------------------------------
# Load trained Machine Learning model
# The model was saved using joblib after training
# ---------------------------------------------------
model = joblib.load("models/ids_model.pkl")

# ---------------------------------------------------
# Home Route
# Displays the main webpage
# ---------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------------------------------------------
# Prediction Route
# Handles form submission and predicts attack type
# ---------------------------------------------------
@app.route('/predict', methods=['POST'])
def predict():

    # -----------------------------------------------
    # Get input values from HTML form
    # Convert all values into float numbers
    # -----------------------------------------------
    features = [list(map(float, request.form.values()))]

    # -----------------------------------------------
    # Predict attack type using trained model
    # -----------------------------------------------
    prediction = model.predict(features)

    # -----------------------------------------------
    # Dictionary to convert encoded labels
    # into actual attack names
    # -----------------------------------------------
    attack_labels = {
        0: "back",
        1: "buffer_overflow",
        2: "ftp_write",
        3: "guess_passwd",
        4: "imap",
        5: "ipsweep",
        6: "land",
        7: "loadmodule",
        8: "multihop",
        9: "neptune",
        10: "nmap",
        11: "normal",
        12: "perl",
        13: "phf",
        14: "pod",
        15: "portsweep",
        16: "rootkit",
        17: "satan",
        18: "smurf",
        19: "spy",
        20: "teardrop",
        21: "warezclient",
        22: "warezmaster"
    }

    # -----------------------------------------------
    # Get attack name from predicted label
    # If label not found, show "Unknown"
    # -----------------------------------------------
    result = attack_labels.get(prediction[0], "Unknown")

    # -----------------------------------------------
    # Return result back to webpage
    # -----------------------------------------------
    return render_template(
        'index.html',
        prediction_text=f'Prediction Result: {result}'
    )

# ---------------------------------------------------
# Run Flask development server
# debug=True automatically reloads server on changes
# ---------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)