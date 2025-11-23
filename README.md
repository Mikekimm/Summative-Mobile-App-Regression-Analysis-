Youtube Video Link  https://youtu.be/0BJPtSDFAGw

Linear_Regression
Insurance charge prediction System

Mission
Predict annual medical insurance charges based on a person's health and demographic information.
Mission Statement
This system predicts annual medical insurance using machine learning. By analyzing demographic and health factors we provide accurate estimates that help people plan their healthcare budget.The solution combines regression analysis, REST API deployment, and a mobile application to make insurance predictions accessible and user-friendly.

Insurance Charges Prediction - 

Project Overview 
This project consists of three main components:
1. Jupyter Notebook - Regression analysis with 4 Machine learning models
2. FastAPI Backend - REST API deployed on Render
3. Flutter Mobile App - Cross-platform mobile application

Required Software
- Python 3.8+  (Python 3.13 is the one recommended)
- Flutter SDK 3.0+
- Git 
- VS Code or Android Studio
- Chrome Browser (for web testing)

Installation Instructions

Clone the Repository git clone:
https://github.com/Mikekimm/Summative-Mobile-App-Regression-Analysis-.git
cd Summative-Mobile-App-Regression-Analysis-

Jupyter Notebook
cd  Linear_regression
Install Python Dependencies pandas,numpy,scikit learn,matplotib,seaborn,jupyter
pip install -r requirements.txt
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
Launch Jupyter Notebook
Open and run insurance_regression_analysis.ipynb
Click cell and run all

FastAPI (Which is already deployed)
https://summative-mobile-app-regression-analysis-x6ss.onrender.com

Swagger https://summative-mobile-app-regression-analysis-x6ss.onrender.com/docs

Install dependencies pip install -r requirements.txt
Generate model files python generate_model_files.py
Run server python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload

Flutter Mobile App:
cd ../linear_regression_app
Install dependencies flutter pub get
Verify the installation using flutter doctor
Run it using flutter run
Test the app


Dataset Overview
We use the Medical Cost Personal Dataset from Kaggle

Dataset Source

Dataset Statistics
1,338 records
6 input features + 1 target variable
Zero missing values
Includes both numeric and categorical data

What’s Inside the Dataset

Feature
Type
What it Represents
Range/Values
age
Number
Person’s age
18–64
sex
Category
Gender
male / female
bmi
Number
Body Mass Index
15.96–53.13
children
Number
Number of dependents
0–5
smoker
Category
Whether the person smokes
yes / no
region
Category
U.S. residential region
northeast / northwest / southeast / southwest
charges
Number (Target)
Annual medical insurance cost
$1,121 – $63,770





Reasons why this Dataset Matters
It shows how lifestyle choices like smoking influence insurance pricing
Combines variety (categorical + numeric) with enough data for reliable modeling
It’s commonly used in industry for teaching costs
It address a real problem which growing of healthcare costs

Key Insights
Smoking - the number one 79% correlation with insurance charges where smokers pay 4 times more than non-smoking person
Age and BMI - Older people pay more while also high BMI results to high costs
Region - It’s a minor factor correlation is less than 10%

Visualizations
My project includes several visualizations:
Correlation heat map - Shows smoker = top predictor
Distribution plots - Charges are heavily skewed
Scatter plots Shows model performance
Boxplots - Clear gap between smokers vs non-smokers
Histograms for age & BMI - Useful for understanding population spread
Machine learning Models Used
Linear Regression - Baseline model
Stochastic Gradient Descent - Its more iterative optimization
Decision Tree - Captures nonlinear patterns
Random Forest - Best generalization performance

Best Model - Random Forest

Project Structure
Summative-Mobile-App-Regression-Analysis/
├── README.md
├── Linear_regression/
│   ├── insurance_regression_analysis.ipynb
│   ├── insurance.csv
│   ├── best_insurance_model.pkl
│   ├── insurance_scaler.pkl
│   ├── insurance_label_encoders.pkl
│   └── Visualization PNGs
├── API/
│   ├── main.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── README.md
│   └── Model files
└── linear_regression_app/
    ├── lib/main.dart
    ├── pubspec.yaml
    └── README_FLUTTER.md



Technologies used
Data and Machine Learning - Python, pandas, numpy, scikit-learn, matplotlib, seaborn, Jupyter Notebook
API Development - FastAPI, Uvicorn, Pydantic, CORS support
Mobile Application - Flutter,Dart,

Public API Endpoint
 **Swagger UI Documentation:**
🔗 https://your-api-name.onrender.com/docs
*Note: Replace with your actual Render deployment URL after deploying* **API Endpoint for Predictions:**
POST https://your-api-name.onrender.com/predict
**Test the API using Swagger UI:** 1. Click the link above to access interactive documentation 2. Click on "POST /predict" endpoint 3. Click "Try it out" 4. Enter sample data:
json
{
  "age": 30,
  "sex": "male",
  "bmi": 25.0,
  "children": 2,
  "smoker": "no",
  "region": "northeast"
}
5. Click "Execute" to see predictions
How to Run
Run Regression - cd Linear_regression, jupyter notebook insurance_regression_analysis.ipynb
Launch API -  cd API, pip install -r requirements.txt, uvicorn main:app 
Start Mobile App - cd linear_regression_app, flutter pub get, flutter run


Performance Summary
Model
R²
RMSE
Speed
Notes
Linear Regression
0.783
$5,799
Very Fast
Baseline
SGD
0.780
$5,842
Fast
Iterative
Decision Tree
0.866
$4,562
Fast
Captures nonlinearity
Random Forest
0.874
$4,428
Moderate
Best model — deployed


Project Highlights
Clear visualizations
Real-world use case
Clean and accurate machine learning pipeline
Production-ready API
Functional Flutter mobile app
Great dataset variety and size
Strong performance (87% accuracy)

Developer: Michael Kimani
Mobile App Regression Analysis - Summative

API Documentation: See `API/README.md`
Flutter App Guide: See `linear_regression_app/README_FLUTTER.md
 Jupyter Notebook: Open Linear_regression/insurance_regression_analysis.ipynb

Source: https://www.kaggle.com/code/abdulrahmanelbanna/medical-insurance-cost-prediction