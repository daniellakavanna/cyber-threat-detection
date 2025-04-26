import boto3
import torch
import json
from pydantic import BaseModel, ValidationError
from model import ThreatDetectionModel 
import enum

class PredictionInput(BaseModel):
    features: list[float]  

class DetectionLabel(str, enum.Enum):
    Malicious = "Malicious"
    Benign = "Benign"


def threat_detection_prediction_handler(event, context):

    local_model_path = "models/model.pth" 

    # Load the model architecture
    model = ThreatDetectionModel()

    # Load the weights into the model
    model.load_state_dict(torch.load(local_model_path, map_location=torch.device('cpu')))
    model.eval()  # Set to evaluation mode

    # Parse and validate input data using Pydantic
    try:
        features = json.loads(event['body'])  
        validated_input = PredictionInput(**features)
        input_tensor = torch.tensor(validated_input.features, dtype=torch.float32).unsqueeze(0)
    except (ValidationError, KeyError) as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Invalid input data: {str(e)}'})
        }

    try:
        with torch.no_grad():
            prediction_score = model(input_tensor).item()
            prediction_label = DetectionLabel.Malicious if prediction_score >= 0.5 else DetectionLabel.Benign
     
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Prediction failed: {str(e)}'})
        }


    return {
        'statusCode': 200,
        'body': json.dumps({'prediction': prediction_label})
    }
