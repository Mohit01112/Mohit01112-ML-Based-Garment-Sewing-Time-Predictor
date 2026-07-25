# 🧵 ML-Based Garment Sewing Time Predictor

An end-to-end **Machine Learning** application that predicts garment sewing time based on garment type, order quantity, and the number of stitch operations. The project uses a **Random Forest Regressor** for accurate predictions and is deployed as an interactive web application using **Streamlit**.

---

## 🚀 Live Demo

🌐 **Live Application**

https://mohit01112-ml-based-garment-sewing-time-predictor-9jcisyzk6c3t.streamlit.app/

💻 **GitHub Repository**

https://github.com/Mohit01112/Mohit01112-ML-Based-Garment-Sewing-Time-Predictor

---

## 📌 Project Overview

In garment manufacturing, accurately estimating sewing time is essential for production planning, resource allocation, and delivery scheduling. Manual estimation is often time-consuming and inconsistent.

This project leverages Machine Learning to automate sewing time prediction, enabling manufacturers to estimate production time quickly and efficiently.

---

## ✨ Features

- 🧵 Predict garment sewing time instantly
- 🤖 Machine Learning model using Random Forest Regression
- 📊 Interactive Streamlit web application
- ⚡ Fast and accurate predictions
- 📦 Pre-trained model using Joblib
- 🎯 User-friendly interface
- 🚀 Ready for cloud deployment

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Regressor

### Libraries
- Pandas
- NumPy
- Joblib

### Web Framework
- Streamlit

### Development Tools
- Git
- GitHub

---

## 📂 Project Structure

```
ML-Based-Garment-Sewing-Time-Predictor/
│
├── app.py                     # Streamlit Application
├── artifacts/
│   ├── model.pkl              # Trained Random Forest Model
│   └── encoder.pkl            # Label Encoder
│
├── src/
│   └── predict.py             # Prediction Pipeline
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Input Features

| Feature | Description |
|----------|-------------|
| Garment Type | Type of garment |
| Order Quantity | Total garments in the order |
| Number of Stitch Operations | Number of stitching operations required |

---

## 🎯 Output

**Predicted Sewing Time (Minutes)**

Example:

```
Garment Type: Shirt
Order Quantity: 500
Stitch Operations: 25

Predicted Sewing Time:
48.37 Minutes
```

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Label Encoding
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Serialization using Joblib
8. Streamlit Deployment

---

## 📈 Machine Learning Model

**Algorithm Used**

- Random Forest Regressor

### Why Random Forest?

- High prediction accuracy
- Handles non-linear relationships
- Reduces overfitting
- Works well on tabular datasets
- Robust against noisy data

---

## 📊 Model Pipeline

```
User Input
      │
      ▼
Data Validation
      │
      ▼
Label Encoding
      │
      ▼
Random Forest Model
      │
      ▼
Predicted Sewing Time
      │
      ▼
Display Result on Streamlit
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/Mohit01112/Mohit01112-ML-Based-Garment-Sewing-Time-Predictor.git
```

### Navigate to Project

```bash
cd Mohit01112-ML-Based-Garment-Sewing-Time-Predictor
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

#### Windows

```bash
env\Scripts\activate
```

#### Linux / macOS

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💻 Application Workflow

1. Select Garment Type
2. Enter Order Quantity
3. Enter Number of Stitch Operations
4. Click **Predict Sewing Time**
5. View the predicted sewing time instantly

---

## 📷 Sample Output

```
Garment Type: Jacket

Order Quantity: 800

Stitch Operations: 32

Predicted Sewing Time

65.42 Minutes
```

---

## 📈 Future Enhancements

- Deep Learning Models
- Model Comparison Dashboard
- Batch Prediction
- Production Cost Prediction
- Production Delay Prediction
- Cloud Database Integration
- CI/CD Pipeline
- Docker Deployment

---

## 📚 Libraries Used

- streamlit
- pandas
- numpy
- scikit-learn
- joblib

---

## 👨‍💻 Author

**Mohit Jadhav**

Artificial Intelligence & Data Science Engineer

### Connect with Me

GitHub:
https://github.com/Mohit01112

LinkedIn:
(Add your LinkedIn profile here)

---

## ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- Scikit-learn
- Streamlit
- Pandas
- NumPy
- Python Community

---

# ⭐ If you like this project, don't forget to give it a Star!
