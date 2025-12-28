#🏥 Insurance Premium Prediction — Production‑Grade Hybrid Regression System

> **A data‑science case study focused on accuracy, robustness, and error reduction in real‑world pricing models.**

---

## 📌 Project Overview

Accurately predicting insurance premiums is a **high‑stakes regression problem** where traditional metrics (like R²) alone are insufficient. Even models with strong average performance can fail catastrophically on specific customer segments, leading to severe under‑ or over‑pricing.

This project goes beyond baseline modeling by:

* Performing **deep error analysis**
* Identifying and mitigating **extreme relative errors**
* Designing a **hybrid residual learning architecture** to improve stability and reliability

The final system achieves **high predictive power while nearly eliminating extreme prediction failures**, making it suitable for real‑world deployment scenarios.

---

## 🎯 Problem Statement

Given customer demographic, lifestyle, and financial attributes, predict the **annual insurance premium amount** as accurately and robustly as possible.

Key challenges addressed:

* Highly skewed target variable
* Sparse and categorical feature interactions
* Disproportionate impact of errors on low‑premium customers
* Large percentage errors despite good global metrics

---

## 🧠 Modeling Philosophy

Rather than optimizing a single metric, this project emphasizes:

* **Error distribution analysis** over average accuracy
* **Tail‑risk mitigation** (reducing extreme relative errors)
* **Interpretability + non‑linear learning** through hybrid modeling

> *A model that performs well on average but fails badly for 30% of cases is not production‑ready.*

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy** — data processing
* **scikit‑learn** — preprocessing, Linear Regression
* **XGBoost** — residual learning
* **Matplotlib, Seaborn** — visualization

---

## 📊 Dataset & Features

### Target

* `annual_premium_amount` → log‑transformed for stability

### Feature Categories

* Demographics: age, gender, marital status, region
* Financials: income (continuous & categorical)
* Lifestyle: BMI category, smoking status
* Risk indicators: medical history, insurance plan

Categorical variables were one‑hot encoded. Numeric features were scaled where appropriate.

---

## 🔄 Project Workflow

### 1️⃣ Exploratory Data Analysis

* Identified heavy right‑skew in premium amounts
* Applied log transformation to stabilize variance

### 2️⃣ Baseline Linear Regression

* Achieved strong global performance (R² ≈ 0.94)
* **But** error analysis revealed:

  * ~33% of test samples had >10% relative error
  * Extreme errors clustered around low‑income and sparse feature combinations

### 3️⃣ Interaction Feature Engineering

* Created domain‑informed interaction terms
* Improved structural expressiveness
* Introduced multicollinearity and variance trade‑offs

### 4️⃣ Residual Learning Architecture (Core Contribution)

A **two‑stage hybrid model** was implemented:

1. **Linear Regression**

   * Captures global linear trends
   * Maintains interpretability

2. **XGBoost Regressor (Residual Model)**

   * Trained on prediction residuals
   * Learns non‑linear patterns missed by linear model

Final prediction:

```
Final Prediction = Linear Prediction + XGBoost Residual Prediction
```

---

## ✅ Final Results

| Metric                    | Baseline Linear Model | Hybrid Model |
| ------------------------- | --------------------- | ------------ |
| R²                        | ~0.94                 | **0.926**    |
| RMSE (log scale)          | ~0.20                 | **0.157** ↓  |
| Extreme Error Rate (>10%) | **~33.7%**            | **0.8%** 🔥  |

### Key Takeaway

> The hybrid model **nearly eliminates catastrophic prediction failures** while retaining high explanatory power.

---

## 📉 Error Analysis & Visualization Highlights

* Residual plots revealed heteroscedasticity in baseline models
* Feature distribution analysis showed **no systematic concentration of extreme errors** after hybrid modeling
* KDE plots were replaced with **rug plots** where data scarcity made density estimation statistically invalid

This ensured **honest and interpretable visualizations**.

---

## 🧪 Why This Matters in Production

In real insurance systems:

* A small number of bad predictions can cause large financial or regulatory impact
* Tail‑risk matters more than marginal R² improvements

This project demonstrates:

* Metric‑driven debugging
* Robust pipeline design
* Practical ML engineering decisions

---

## 📈 Possible Extensions

* Quantile regression for uncertainty estimation
* SHAP analysis for residual model interpretability
* Deployment via Streamlit or FastAPI
* Monitoring drift in residual distributions

---

## 🏁 Conclusion

This project demonstrates how **error‑aware modeling and hybrid architectures** can transform a strong baseline into a **production‑ready regression system**.

It reflects real‑world ML work: diagnosing failures, iterating intelligently, and prioritizing robustness over vanity metrics.

---

## 👤 Author

**Shubham Jha**
Aspiring Data Scientist | Machine Learning Enthusiast

---

⭐ *If you find this project insightful, feel free to star the repository or reach out for discussion.*
