import os
import pickle
import datetime
import tensorflow as tf
from .preprocessing import load_and_process

class FraudDetectionModel:
    def __init__(self):
        self.model = None


    def train_model():
        # Load and preprocess the data
        X_train, X_test, y_train, y_test = load_and_process()

        # Define the Tensorflow model
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        
        # Compile the model
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        
        # Create a TensorBoard callback
        log_dir = 'tensorboard_logs/fit/' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
        
        # Train the model
        model.fit(
            X_train, 
            y_train, 
            epochs=10, 
            validation_data=(X_test, y_test), 
            callbacks=[tensorboard_callback]
            )
        
        # Save the trained model to the 'models' directory
        model_path = 'models/fraud_detection_model.pkl'
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)

        return model
    
    def predict(self, X):
        # Load the trained model
        model_path = os.path.join('data', 'models', 'fraud_detection_model.pkl')
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        
        # Use the model to make predictions on the input data
        y_pred = model.predict(X)
        
        return y_pred
