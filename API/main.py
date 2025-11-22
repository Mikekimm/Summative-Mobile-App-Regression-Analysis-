"""
Insurance Charges Prediction API
FastAPI application for predicting insurance charges using the trained model
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
import pickle
import pandas as pd
import numpy as np
from typing import Literal
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Insurance Charges Prediction API",
    description="API for predicting medical insurance charges based on customer information",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load model components at startup
try:
    with open('best_insurance_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    with open('insurance_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    with open('insurance_label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)
    
    with open('insurance_feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    
    print("✓ Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


# Pydantic model for input validation
class InsuranceRequest(BaseModel):
    """
    Input model for insurance prediction with data validation
    """
    age: int = Field(
        ...,
        ge=18,
        le=100,
        description="Age of the customer (18-100 years)",
        example=35
    )
    sex: Literal['male', 'female'] = Field(
        ...,
        description="Gender of the customer",
        example="male"
    )
    bmi: float = Field(
        ...,
        ge=10.0,
        le=60.0,
        description="Body Mass Index (10.0-60.0)",
        example=27.5
    )
    children: int = Field(
        ...,
        ge=0,
        le=10,
        description="Number of children/dependents (0-10)",
        example=2
    )
    smoker: Literal['yes', 'no'] = Field(
        ...,
        description="Smoking status",
        example="no"
    )
    region: Literal['northeast', 'northwest', 'southeast', 'southwest'] = Field(
        ...,
        description="Residential region in the US",
        example="northwest"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "age": 35,
                "sex": "male",
                "bmi": 27.5,
                "children": 2,
                "smoker": "no",
                "region": "northwest"
            }
        }


# Pydantic model for response
class InsurancePrediction(BaseModel):
    """
    Output model for insurance prediction response
    """
    predicted_charges: float = Field(
        ...,
        description="Predicted annual insurance charges in USD"
    )
    prediction_details: dict = Field(
        ...,
        description="Details about the prediction and input"
    )
    model_info: dict = Field(
        ...,
        description="Information about the model used"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "predicted_charges": 12345.67,
                "prediction_details": {
                    "age": 35,
                    "sex": "male",
                    "bmi": 27.5,
                    "children": 2,
                    "smoker": "no",
                    "region": "northwest",
                    "formatted_charges": "$12,345.67"
                },
                "model_info": {
                    "model_type": "Random Forest Regressor",
                    "r2_score": 0.8737,
                    "rmse": 4428.41
                }
            }
        }


@app.get("/")
async def root():
    """
    Root endpoint - API information
    """
    return {
        "message": "Insurance Charges Prediction API",
        "version": "1.0.0",
        "status": "online",
        "endpoints": {
            "prediction": "/predict (POST)",
            "health": "/health (GET)",
            "documentation": "/docs (GET)"
        },
        "description": "API for predicting medical insurance charges based on customer demographics and health information"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    model_status = "loaded" if model is not None else "not loaded"
    return {
        "status": "healthy",
        "model_status": model_status,
        "api_version": "1.0.0"
    }


@app.post("/predict", response_model=InsurancePrediction)
async def predict_insurance(request: InsuranceRequest):
    """
    Predict insurance charges based on customer information
    
    Parameters:
    - age: Age of the customer (18-100)
    - sex: Gender (male/female)
    - bmi: Body Mass Index (10.0-60.0)
    - children: Number of children/dependents (0-10)
    - smoker: Smoking status (yes/no)
    - region: US region (northeast/northwest/southeast/southwest)
    
    Returns:
    - predicted_charges: Predicted annual insurance charges
    - prediction_details: Input details and formatted output
    - model_info: Information about the model
    """
    
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please contact administrator."
        )
    
    try:
        # Create input dataframe
        input_data = pd.DataFrame({
            'age': [request.age],
            'sex': [request.sex],
            'bmi': [request.bmi],
            'children': [request.children],
            'smoker': [request.smoker],
            'region': [request.region]
        })
        
        # Encode categorical features
        for col in ['sex', 'smoker', 'region']:
            input_data[col] = label_encoders[col].transform(input_data[col])
        
        # Ensure correct feature order
        input_data = input_data[feature_names]
        
        # Standardize features
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = float(model.predict(input_scaled)[0])
        
        # Round to 2 decimal places
        prediction = round(prediction, 2)
        
        # Prepare response
        response = InsurancePrediction(
            predicted_charges=prediction,
            prediction_details={
                "age": request.age,
                "sex": request.sex,
                "bmi": request.bmi,
                "children": request.children,
                "smoker": request.smoker,
                "region": request.region,
                "formatted_charges": f"${prediction:,.2f}",
                "monthly_charges": f"${prediction/12:,.2f}"
            },
            model_info={
                "model_type": "Random Forest Regressor",
                "r2_score": 0.8737,
                "rmse": 4428.41,
                "description": "Optimized ensemble model with 87.4% accuracy"
            }
        )
        
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )


@app.post("/predict/batch")
async def predict_batch(requests: list[InsuranceRequest]):
    """
    Batch prediction endpoint - predict for multiple customers at once
    
    Parameters:
    - requests: List of insurance request objects
    
    Returns:
    - predictions: List of predictions for each request
    """
    
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please contact administrator."
        )
    
    try:
        predictions = []
        
        for req in requests:
            # Create input dataframe
            input_data = pd.DataFrame({
                'age': [req.age],
                'sex': [req.sex],
                'bmi': [req.bmi],
                'children': [req.children],
                'smoker': [req.smoker],
                'region': [req.region]
            })
            
            # Encode categorical features
            for col in ['sex', 'smoker', 'region']:
                input_data[col] = label_encoders[col].transform(input_data[col])
            
            # Ensure correct feature order
            input_data = input_data[feature_names]
            
            # Standardize features
            input_scaled = scaler.transform(input_data)
            
            # Make prediction
            prediction = float(model.predict(input_scaled)[0])
            prediction = round(prediction, 2)
            
            predictions.append({
                "input": req.dict(),
                "predicted_charges": prediction,
                "formatted_charges": f"${prediction:,.2f}"
            })
        
        return {
            "total_predictions": len(predictions),
            "predictions": predictions
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Batch prediction error: {str(e)}"
        )


@app.get("/model-info")
async def get_model_info():
    """
    Get information about the trained model
    """
    return {
        "model_type": "Random Forest Regressor",
        "framework": "scikit-learn",
        "performance_metrics": {
            "r2_score": 0.8737,
            "rmse": 4428.41,
            "test_accuracy": "87.37%"
        },
        "features": [
            "age",
            "sex",
            "bmi",
            "children",
            "smoker",
            "region"
        ],
        "target": "expenses (annual insurance charges)",
        "training_data": {
            "total_samples": 1338,
            "train_samples": 1070,
            "test_samples": 268
        },
        "feature_importance": {
            "smoker": "Highest importance - smoking status dominates charges",
            "age": "Moderate importance - older individuals pay more",
            "bmi": "Moderate importance - higher BMI increases charges",
            "children": "Low importance",
            "sex": "Very low importance",
            "region": "Very low importance"
        }
    }


if __name__ == "__main__":
    # Run the application
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
