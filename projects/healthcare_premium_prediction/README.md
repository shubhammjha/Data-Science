Healthcare Premium Prediction
📌 Project Overview

This project focuses on predicting healthcare insurance premiums using machine learning techniques based on an individual’s demographic, lifestyle, and medical attributes. Accurate premium prediction helps insurance providers design fair pricing models and enables individuals to better understand the factors influencing their insurance costs.
The project demonstrates a complete end-to-end data science workflow, including data analysis, preprocessing, model building, and evaluation.

🎯 Problem Statement
Healthcare insurance premiums vary significantly depending on multiple factors such as age, income level, medical history, lifestyle habits, and insurance plans. The goal of this project is to:
Build a machine learning model that predicts the insurance premium category/amount based on user attributes.

📊 Dataset Description
The dataset contains anonymized healthcare and demographic data. Key features include:

Age – Age of the individual

Gender – Male / Female

Income Level – Income category of the individual

Medical History – Existing medical conditions (e.g., Diabetes, Hypertension)

Lifestyle Factors – Smoking, physical activity, etc.

Insurance Plan – Type of insurance plan chosen

Target Variable – Insurance premium (or premium category)

📁 Dataset file: healthcare_premium_data.xlsx

🛠️ Tools & Technologies Used

Python

Pandas & NumPy – Data manipulation

Matplotlib & Seaborn – Data visualization

Scikit-learn – Machine learning models & evaluation

Jupyter Notebook – Interactive analysis

🔍 Project Workflow
1️⃣ Exploratory Data Analysis (EDA)

Understanding data distribution

Identifying missing values

Visualizing relationships between features

Crosstab analysis (e.g., Income vs Insurance Plan)

2️⃣ Data Preprocessing

Handling missing values

Encoding categorical variables

Feature scaling (if required)

Train-test split

3️⃣ Model Building

Baseline model selection

Training machine learning models such as:

Logistic Regression / Linear Regression

Decision Tree

Random Forest (if applicable)

4️⃣ Model Evaluation

Accuracy / RMSE / MAE (based on target type)

Confusion matrix (for classification)

Feature importance analysis

📈 Results & Insights

Identified key factors influencing insurance premiums

Demonstrated how medical history and income level affect premium pricing

Achieved reliable predictive performance on test data

📌 Exact metrics and visualizations are available in the notebook.

📂 Repository Structure

├── datasets/

│ └── healthcare_premium_data.xlsx

├── notebooks/

│ └── healthcare_premium_prediction.ipynb

├── src/

├── README.md

🚀 How to Run the Project

1. Clone the repository
git clone <[repository-url](https://github.com/shubhammjha/Data-Science/edit/main/projects/healthcare_premium_prediction/)>

2. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

3. Open the notebook
jupyter notebook healthcare_premium_prediction.ipynb

👨‍⚕️ Intended Audience

Beginners in Data Science & Machine Learning

Healthcare professionals exploring AI applications

Students building healthcare analytics projects

🔮 Future Improvements

Add advanced models (XGBoost, LightGBM)

Hyperparameter tuning

Convert project into a web app (Streamlit/Flask)

Deploy model using cloud services

📜 License
This project is licensed under the MIT License — free to use and modify.

🙌 Acknowledgements
Dataset used for educational purposes
Inspired by real-world healthcare analytics use cases

⭐ If you find this project useful, feel free to star the repository!
