# DSML Project - Predictive Maintenance System for Industrial Machines

## Project Description

This project focuses on developing a machine learning-based predictive maintenance solution for industrial equipment. By analyzing machine sensor readings, the system aims to identify potential failures before they occur, helping organizations reduce downtime and improve maintenance efficiency.

The project was completed as part of a Data Science and Machine Learning internship program and demonstrates the application of data preprocessing, feature engineering, imbalance handling, and predictive modeling techniques.

---

## Objective

Unexpected equipment failures can lead to production delays and increased operational expenses. The objective of this project is to build a reliable classification model capable of predicting machine failures using historical sensor data.

The solution helps maintenance teams make informed decisions and schedule repairs proactively.

---

## Key Features

* Sensor data analysis and visualization
* Data cleaning and preprocessing
* Feature extraction and engineering
* Class imbalance handling using SMOTE
* Machine learning model development
* Performance evaluation and comparison
* Failure prediction framework
* Data-driven maintenance support

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Random Forest Classifier
* Joblib
* Matplotlib
* Imbalanced-learn (SMOTE)
* Jupyter Notebook
---
## Machine Learning Model

### Random Forest Classifier

The predictive maintenance system uses a **Random Forest Classifier** to predict whether a machine is likely to fail.

Why Random Forest?

- Handles complex relationships between sensor features.
- Works well with non-linear data.
- Reduces overfitting by combining multiple decision trees.
- Provides strong performance on classification tasks.

The trained model is saved as:

```text
outputs/best_random_forest_model.pkl 
```

The Streamlit application (`app.py`) loads this model and performs real-time predictions based on user inputs.
## Dataset Information

The dataset contains operational measurements collected from industrial machines. These measurements are used to determine whether a machine is operating normally or approaching a failure condition.

Example attributes include:

* Air Temperature
* Process Temperature
* Rotational Speed
* Torque
* Tool Wear
* Failure Status

---

## Methodology

### Data Understanding

* Load and inspect the dataset.
* Analyze feature distributions and target classes.

### Data Preparation

* Handle missing or inconsistent values.
* Prepare data for machine learning workflows.

### Feature Engineering

* Generate meaningful features from raw sensor readings.
* Identify patterns associated with machine failures.

### Addressing Class Imbalance

* Apply SMOTE to improve learning from minority classes.
* Prevent bias toward normal operating conditions.

### Model Development

* Train classification models on processed data.
* Evaluate model effectiveness using multiple metrics.

### Model Evaluation

The model is assessed using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Robustness Assessment

* Test model performance under varying data conditions.
* Examine reliability and consistency of predictions.

---

## Project Directory Structure

```text
DSML/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│
├── Notebooks/
│   └── eda.ipynb
│
└── outputs/
    └── best_random_forest_model.pkl
```

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/your-username/DSML-Project.git
```

Move into the project directory:

```bash
cd DSML-Project
```

Install required packages:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---
## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

Enter the machine parameters in the sidebar or input fields and click the prediction button to determine whether the machine is likely to fail. 

## Outcomes

The predictive maintenance model is capable of identifying machine failure patterns from sensor data and assisting in preventive maintenance planning.

Benefits include:

* Reduced unexpected breakdowns
* Improved equipment reliability
* Better maintenance scheduling
* Increased operational productivity

---

## Potential Enhancements

* Real-time monitoring integration
* Advanced ensemble learning techniques
* Explainable AI for prediction interpretation
* Web-based dashboard deployment
* Cloud integration for scalable monitoring

---

## Summary

This project showcases how machine learning can be applied in industrial environments to predict equipment failures using sensor information. The developed solution contributes to smarter maintenance practices and more efficient operational management.

---

## Author

Data Science & Machine Learning Internship Project

Anas Tp

2026
