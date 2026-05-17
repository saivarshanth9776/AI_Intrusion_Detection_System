import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ---------------------------------------------------
# Column names for NSL-KDD dataset
# The dataset does not contain headers,
# so we manually define all column names
# ---------------------------------------------------
columns = [
    "duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot",
    "num_failed_logins","logged_in","num_compromised","root_shell",
    "su_attempted","num_root","num_file_creations","num_shells",
    "num_access_files","num_outbound_cmds","is_host_login",
    "is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate",
    "same_srv_rate","diff_srv_rate","srv_diff_host_rate",
    "dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
    "dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "label","difficulty"
]

# ---------------------------------------------------
# Load NSL-KDD training dataset
# ---------------------------------------------------
data = pd.read_csv(
    "dataset/KDDTrain+.txt",
    names=columns
)

# ---------------------------------------------------
# Remove missing/null values from dataset
# ---------------------------------------------------
data.dropna(inplace=True)

# ---------------------------------------------------
# Create LabelEncoder object
# Used to convert text values into numeric values
# Machine learning models only understand numbers
# ---------------------------------------------------
encoder = LabelEncoder()

# ---------------------------------------------------
# Encode categorical columns into numeric values
# Example:
# tcp -> 1
# udp -> 2
# ---------------------------------------------------
data['protocol_type'] = encoder.fit_transform(data['protocol_type'])
data['service'] = encoder.fit_transform(data['service'])
data['flag'] = encoder.fit_transform(data['flag'])
data['label'] = encoder.fit_transform(data['label'])

# ---------------------------------------------------
# Display first 5 rows after preprocessing
# ---------------------------------------------------
print(data.head())

# ---------------------------------------------------
# Import Machine Learning libraries
# ---------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------------------------------------------
# Select important features for training
# These features will also be used in Flask form
# ---------------------------------------------------
X = data[[
    'duration',
    'protocol_type',
    'service',
    'flag',
    'src_bytes'
]]

# ---------------------------------------------------
# Target variable (attack labels)
# ---------------------------------------------------
y = data['label']

# ---------------------------------------------------
# Split dataset into training and testing sets
# 80% -> Training
# 20% -> Testing
# ---------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------
# Create Random Forest Classifier model
# ---------------------------------------------------
model = RandomForestClassifier()

# ---------------------------------------------------
# Train Machine Learning model using training data
# ---------------------------------------------------
model.fit(X_train, y_train)

# ---------------------------------------------------
# Predict attack labels using test data
# ---------------------------------------------------
predictions = model.predict(X_test)

# ---------------------------------------------------
# Calculate model accuracy
# ---------------------------------------------------
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# ---------------------------------------------------
# Import joblib library
# Used for saving trained ML model
# ---------------------------------------------------
import joblib

# ---------------------------------------------------
# Save trained model into models folder
# ---------------------------------------------------
joblib.dump(model, "models/ids_model.pkl")

print("Model saved successfully!")