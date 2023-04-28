import os
import sys
import pytest

from src.models.fraud_detection_model import FraudDetectionModel
from src.models.preprocessing import load_and_process

# from models.fraud_detection_model import FraudDetectionModel

DATASET_PATH = os.path.join('data', 'raw', 'fraudTest.csv')


@pytest.fixture(scope='module')
def model():
    # model_path = os.path.join('data', 'models', 'fraud_detection_model.pkl')
    return FraudDetectionModel()


def test_predict(model):
    # Train the model
    model.train_model()

    # Load and preprocess the data
    X_train, X_test, y_train, y_test = load_and_process(DATASET_PATH)

    # Test predict method
    y_pred = model.predict(X_test)
    assert y_pred.shape == y_test.shape  # Make sure predicted labels have same shape as actual labels