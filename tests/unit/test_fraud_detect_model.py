import os
import sys
import pytest

from src.models.fraud_detection_model import FraudDetectionModel
from src.models.preprocessing import load_and_process

# from models.fraud_detection_model import FraudDetectionModel

@pytest.fixture(scope='module')
def model():
    # model_path = os.path.join('data', 'models', 'fraud_detection_model.pkl')
    return FraudDetectionModel()

def test_predict(model):
    # create a test data sample
    data = {
        'trans_date_trans_time': '2019-01-01 12:00:00',
        'cc_num': '1234567890123456',
        'merchant': 'Example Merchant',
        'category': 'Grocery',
        'amt': 100.00,
        'first': 'John',
        'last': 'Doe',
        'gender': 'M',
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345',
        'lat': 37.7749,
        'long': -122.4194,
        'city_pop': 10000,
        'job': 'Engineer',
        'dob': '1990-01-01',
        'trans_num': '1234567890',
        'unix_time': 1546300800,
        'merch_lat': 37.7749,
        'merch_long': -122.4194,
    }

    # test predict method
    result = model.predict(data)
    assert result == 0 or result == 1  # fraud or not fraud
    
