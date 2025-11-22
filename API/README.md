# Insurance Charges Prediction API

FastAPI-based REST API for predicting medical insurance charges using Machine Learning.

## Features

- **POST /predict** - Single prediction endpoint
- **POST /predict/batch** - Batch prediction endpoint
- **GET /model-info** - Model information and performance metrics
- **GET /health** - Health check endpoint
- **Interactive API Documentation** - Available at `/docs`

## Model Information

- **Model Type**: Random Forest Regressor
- **R² Score**: 0.8737 (87.37% accuracy)
- **RMSE**: $4,428.41

## Input Features

- **age**: Age of the customer (18-100 years)
- **sex**: Gender (male/female)
- **bmi**: Body Mass Index (10.0-60.0)
- **children**: Number of children/dependents (0-10)
- **smoker**: Smoking status (yes/no)
- **region**: US region (northeast/northwest/southeast/southwest)

## Installation

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

## API Usage Examples

### Single Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "sex": "male",
    "bmi": 27.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest"
  }'
```

### Batch Prediction

```bash
curl -X POST "http://localhost:8000/predict/batch" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "age": 35,
      "sex": "male",
      "bmi": 27.5,
      "children": 2,
      "smoker": "no",
      "region": "northwest"
    },
    {
      "age": 45,
      "sex": "female",
      "bmi": 30.0,
      "children": 1,
      "smoker": "yes",
      "region": "southeast"
    }
  ]'
```

## Deployment on Render

### Steps to Deploy:

1. Push code to GitHub repository
2. Go to [Render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Deploy!

### Environment Variables (Optional):
- `PORT`: Auto-set by Render

## Response Format

```json
{
  "predicted_charges": 12345.67,
  "prediction_details": {
    "age": 35,
    "sex": "male",
    "bmi": 27.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest",
    "formatted_charges": "$12,345.67",
    "monthly_charges": "$1,028.81"
  },
  "model_info": {
    "model_type": "Random Forest Regressor",
    "r2_score": 0.8737,
    "rmse": 4428.41,
    "description": "Optimized ensemble model with 87.4% accuracy"
  }
}
```

## CORS Configuration

CORS is enabled for all origins. Modify in `main.py` if you need to restrict access:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Data Validation

Input validation is enforced using Pydantic:
- Age must be between 18-100
- BMI must be between 10.0-60.0
- Children must be between 0-10
- Sex, smoker, and region must match specific values

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Root endpoint - API information |
| GET | /health | Health check |
| POST | /predict | Single prediction |
| POST | /predict/batch | Batch predictions |
| GET | /model-info | Model information |
| GET | /docs | Interactive API documentation (Swagger UI) |
| GET | /redoc | Alternative API documentation (ReDoc) |

## License

MIT License

## Contact

For questions or issues, please contact the development team.
