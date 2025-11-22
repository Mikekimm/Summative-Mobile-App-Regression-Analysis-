#!/usr/bin/env python3
"""
Generate model files for API deployment
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle
import warnings
warnings.filterwarnings('ignore')

print("Generating model files for API...")

# Load data
df = pd.read_csv('insurance.csv')
print(f"✓ Loaded {len(df)} records")

# Preprocessing
df_processed = df.copy()
label_encoders = {}

for col in ['sex', 'smoker', 'region']:
    le = LabelEncoder()
    df_processed[col] = le.fit_transform(df_processed[col])
    label_encoders[col] = le

X = df_processed.drop('expenses', axis=1)
y = df_processed['expenses']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("✓ Data split complete")

# Standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("✓ Standardization complete")

# Train Random Forest (best model)
print("✓ Training Random Forest...")
rf_params = {
    'n_estimators': [200],
    'max_depth': [15],
    'min_samples_split': [2],
    'min_samples_leaf': [1]
}

rf_model = RandomForestRegressor(random_state=42, n_jobs=-1)
rf_grid = GridSearchCV(rf_model, rf_params, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
rf_grid.fit(X_train_scaled, y_train)
best_model = rf_grid.best_estimator_

print("✓ Model training complete")

# Save all components
with open('best_insurance_model.pkl', 'wb') as f:
    pickle.dump(best_model, f)

with open('insurance_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

with open('insurance_label_encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

with open('insurance_feature_names.pkl', 'wb') as f:
    pickle.dump(list(X.columns), f)

print("\n✓ All model files saved successfully!")
print("  - best_insurance_model.pkl")
print("  - insurance_scaler.pkl")
print("  - insurance_label_encoders.pkl")
print("  - insurance_feature_names.pkl")
print("\n✓ Ready for API deployment!")
