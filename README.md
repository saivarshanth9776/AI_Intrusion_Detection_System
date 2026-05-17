# AI-Powered Intrusion Detection System (IDS)

## 📌 Project Overview

The AI-Powered Intrusion Detection System (IDS) is a cybersecurity-based machine learning project developed to detect malicious network activities and cyber attacks.  
The system analyzes network traffic features and predicts whether the traffic is normal or an intrusion attack.

This project uses the NSL-KDD dataset and Random Forest Machine Learning algorithm to classify different types of network attacks.

---

## 🚀 Features

- Detects cyber attacks using Machine Learning
- Predicts intrusion types in real-time
- Flask-based web application
- Responsive user interface using Bootstrap
- Preprocessing and feature encoding
- Random Forest Classifier implementation
- Attack prediction dashboard
- Model accuracy evaluation
- GitHub-ready project structure

---

## 🛠 Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Web Framework
- Flask

### Frontend
- HTML
- Bootstrap 5

### Model
- Random Forest Classifier

---

## 📂 Project Structure

```bash
IDS_Project/
│
├── dataset/
│   ├── KDDTrain+.txt
│   └── KDDTest+.txt
│
├── models/
│   └── ids_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Used

- NSL-KDD Dataset

The dataset contains network traffic records labeled as:
- Normal Traffic
- DoS Attacks
- Probe Attacks
- R2L Attacks
- U2R Attacks

---

## ⚙️ Installation Steps

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI_Intrusion_Detection_System.git
```

### 2️⃣ Open Project Folder

```bash
cd AI_Intrusion_Detection_System
```

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

### Train Model

```bash
python train_model.py
```

### Run Flask Application

```bash
python app.py
```

---

## 🌐 Open in Browser

```bash
http://127.0.0.1:5000
```

---

## 📈 Model Accuracy

- Random Forest Accuracy: ~97% to 99%

Accuracy may vary depending on training data and selected features.

---

## 🧠 Machine Learning Workflow

1. Load NSL-KDD Dataset
2. Data Preprocessing
3. Feature Encoding
4. Train-Test Splitting
5. Random Forest Training
6. Prediction and Evaluation
7. Flask Web Deployment

---

## 🔐 Attack Types Detected

- Neptune
- Smurf
- Satan
- Portsweep
- Back
- Rootkit
- Teardrop
- Warezmaster
- Normal Traffic
- and more...

---

## 📱 Responsive Design

The web application is fully responsive and works on:
- Desktop
- Laptop
- Tablet
- Mobile devices

---

## 🔌 API Integration

The project uses Flask routes as API endpoints for:
- User Input Handling
- Attack Prediction
- Dynamic Result Display

---

## 📌 Future Enhancements

- Real-time packet sniffing
- Live traffic monitoring
- Email alert system
- Graphical analytics dashboard
- User authentication
- Cloud deployment

---

## 👨‍💻 Author

Chilla Sai Varshanth

---

## 📜 License

This project is developed for educational and academic purposes.