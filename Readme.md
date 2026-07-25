# 👕 AI-Based Garment Production Time Prediction System

An end-to-end Machine Learning application that predicts the total sewing time required for garment production based on garment type, order quantity, and stitch operations. The project includes model training, prediction pipeline, and a Flask-based web interface for real-time predictions.

---

## 📌 Project Overview

Garment manufacturing industries require accurate production time estimation for effective planning and scheduling. This project leverages Machine Learning to estimate the total sewing time for a production order, helping optimize resource allocation and improve production efficiency.

Users can enter:
- Garment Type
- Order Quantity
- Number of Stitch Operations

The application predicts the estimated sewing time in minutes.

---

## 🚀 Features

- Machine Learning based prediction
- Random Forest Regression Model
- Interactive Flask Web Application
- Real-time predictions
- User-friendly interface
- Model saved using Joblib
- Label Encoding for categorical features
- Easy deployment

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Regressor

### Data Processing
- Pandas
- NumPy

### Backend
- Flask

### Frontend
- HTML
- CSS
- JavaScript

### Model Persistence
- Joblib

---

## 📂 Project Structure

```
Garment-Time-Prediction/
│
├── artifacts/
│   ├── model.pkl
│   └── encoder.pkl
├──src
│   └── predict.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── predict.py
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## 📊 Input Features

| Feature | Description |
|----------|-------------|
| Garment Type | Type of garment |
| Order Quantity | Total production quantity |
| Stitch Operations | Number of stitching operations |

### Target Variable

- Total Sewing Time (Minutes)

---

## 🤖 Machine Learning Workflow

1. Dataset Collection
2. Data Preprocessing
3. Label Encoding
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Model Serialization
8. Flask Deployment

---

## 📈 Model Used

### Random Forest Regressor

Why Random Forest?

- Handles non-linear relationships
- High prediction accuracy
- Less prone to overfitting
- Robust to noisy data
- Works well with structured datasets
- Easy to deploy

---

## 📊 Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Garment-Time-Prediction.git
```

Move to project folder

```bash
cd Garment-Time-Prediction
```

Create Virtual Environment

```bash
python -m venv env
```

Activate Environment

Windows

```bash
env\Scripts\activate
```

Linux/Mac

```bash
source env/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📝 Example Input

Garment Type

```
Shirt
```

Order Quantity

```
1000
```

Number of Stitch Operations

```
10
```

### Example Output

```
Estimated Sewing Time

1250 Minutes
```

---

## 🎯 Future Enhancements

- Real manufacturing dataset integration
- User Authentication
- Cloud Deployment
- Production Scheduling Dashboard
- Prediction History
- REST API Support
- Deep Learning Models
- Docker Deployment

---

## 👨‍💻 Author

**Mohit Jadhav**

Artificial Intelligence & Data Science Student

---

## 📜 License

This project is developed for educational and portfolio purposes.
