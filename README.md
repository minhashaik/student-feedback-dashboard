# 🎓 Student Feedback Dashboard with Machine Learning

## 📌 Project Overview

This project analyzes student feedback data to uncover insights about teaching quality, course difficulty, and student satisfaction.
It further extends into a machine learning system that predicts student satisfaction based on course-related factors.

The goal is to help universities make **data-driven academic decisions**.

---

## 🚀 Features

### 📊 Data Analysis

* Explored student feedback dataset using **Pandas**
* Identified trends in satisfaction, difficulty, and workload
* Generated insights using aggregation and statistical analysis

### 📈 Interactive Dashboard

* Built using **Streamlit**
* Multi-page navigation:

  * Dashboard (overview)
  * Analysis (deep insights)
  * Data (raw dataset)
  * About (project info)
* Includes:

  * Filters (course, teacher)
  * KPI metrics
  * Interactive charts (Plotly)

### 🤖 Machine Learning

* Built a **Linear Regression model**
* Predicts student satisfaction using:

  * Difficulty
  * Study Hours
  * Teaching Quality
* Model performance:

  * MAE ≈ 0.07
  * R² ≈ 0.97

### 🔗 Model Integration

* Model saved using **Pickle**
* Integrated into dashboard
* Users can input values and get **real-time predictions**

---

## 🧠 Tech Stack

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Scikit-learn

---

## 📂 Project Structure

```
student-feedback-dashboard/
│
├── data/
│   └── feedback.csv
│
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Analysis.py
│   ├── 3_Data.py
│   └── 4_About.py
│
├── scripts/
│   └── train_model.py
│
├── dashboard.py
├── model.pkl
└── README.md
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m streamlit run dashboard.py
```

---

## 📊 Machine Learning Workflow

1. Data Loading (CSV → Pandas)
2. Feature Selection
3. Train-Test Split
4. Model Training (Linear Regression)
5. Evaluation (MAE, R²)
6. Model Saving (Pickle)
7. Deployment in Streamlit

---

## 💡 Key Insights

* High difficulty + high workload often reduces satisfaction
* Teaching quality strongly influences student experience
* Balanced courses achieve better outcomes

---

## 🎯 Conclusion

This project demonstrates a complete **end-to-end data science pipeline**:

* Data Analysis → Visualization → Machine Learning → Deployment

It shows how raw data can be transformed into **actionable insights and intelligent systems**.

---