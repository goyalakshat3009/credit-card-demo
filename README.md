# 💳 Credit Card Fraud Detection

## 📌 Overview

This project focuses on detecting fraudulent credit card transactions using Machine Learning techniques. The model analyzes transaction-related features and predicts whether a transaction is legitimate or fraudulent.

The project was developed as part of the **CodeSoft Machine Learning Internship**.

---

## 🚀 Features

* Data preprocessing and cleaning
* Handling missing values
* Exploratory Data Analysis (EDA)
* Fraud transaction detection
* Multiple Machine Learning models:

  * Logistic Regression
  * Decision Tree
  * Random Forest
* Model evaluation using:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report
* Interactive Streamlit Web Application

---

## 📊 Dataset

Dataset used:

**Fraud Detection Dataset**
https://www.kaggle.com/datasets/kartik2112/fraud-detection

Files:

* fraudTrain.csv
* fraudTest.csv

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📈 Model Performance

| Model               | Accuracy              |
| ------------------- | --------------------- |
| Logistic Regression | 99.61%                |
| Decision Tree       | 99.37%                |
| Random Forest       | Best Performing Model |

Evaluation Metrics:

* Accuracy Score
* Confusion Matrix
* Precision
* Recall
* F1-Score

---

## 🎯 Input Features Used

The final deployed model uses the following features:

* Transaction Amount (amt)
* Customer Latitude (lat)
* Customer Longitude (long)
* City Population (city_pop)
* Unix Time (unix_time)
* Merchant Latitude (merch_lat)
* Merchant Longitude (merch_long)

---

## 🌐 Streamlit Application

Run locally:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
Credit-Card-Fraud-Detection/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
├── README.md
└── notebook.ipynb
```

---

## 📷 Output

The Streamlit application predicts whether a transaction is:

✅ Legitimate Transaction

or

⚠️ Fraudulent Transaction

---

## 👨‍💻 Author

Akshat Goyal

CodeSoft Machine Learning Internship
