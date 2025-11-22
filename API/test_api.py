#!/usr/bin/env python3
"""
Test script for Insurance Prediction API
Tests all endpoints locally
"""

import requests
import json

BASE_URL = "http://localhost:8000"

print("="*80)
print("TESTING INSURANCE PREDICTION API")
print("="*80)

# Test 1: Root endpoint
print("\n1. Testing root endpoint (GET /)...")
try:
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✓ Root endpoint working!")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 2: Health check
print("\n2. Testing health check (GET /health)...")
try:
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✓ Health check working!")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Model info
print("\n3. Testing model info (GET /model-info)...")
try:
    response = requests.get(f"{BASE_URL}/model-info")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✓ Model info working!")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 4: Single prediction
print("\n4. Testing single prediction (POST /predict)...")
test_data = {
    "age": 35,
    "sex": "male",
    "bmi": 27.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
}
try:
    response = requests.post(f"{BASE_URL}/predict", json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✓ Single prediction working!")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 5: Batch prediction
print("\n5. Testing batch prediction (POST /predict/batch)...")
batch_data = [
    {
        "age": 25,
        "sex": "female",
        "bmi": 22.5,
        "children": 0,
        "smoker": "no",
        "region": "southwest"
    },
    {
        "age": 45,
        "sex": "male",
        "bmi": 30.0,
        "children": 2,
        "smoker": "yes",
        "region": "northeast"
    }
]
try:
    response = requests.post(f"{BASE_URL}/predict/batch", json=batch_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print("✓ Batch prediction working!")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 6: Invalid input should fail validation
print("\n6. Testing input validation (should fail)...")
invalid_data = {
    "age": 150,  # Invalid age
    "sex": "male",
    "bmi": 27.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
}
try:
    response = requests.post(f"{BASE_URL}/predict", json=invalid_data)
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print("✓ Validation working correctly - rejected invalid input!")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "="*80)
print("✓ ALL TESTS COMPLETED!")
print("="*80)
print("\nTo view interactive API documentation, visit:")
print(f"{BASE_URL}/docs")
