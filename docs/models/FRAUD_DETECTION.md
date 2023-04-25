
## ML Fraud Detection Model


### Structure of the model:
   
- Loads the raw data, cleans and preprocesses it, and splits it into training and test sets
    - Store in  (X_train, X_test, y_train, y_test) variables:
    - The X_train and y_train variables contain the features and labels of the training set.
    - The X_test and y_test variables contain the features and labels of the test set.
- Define a fraud_detection Tensorflow model, Its a sequential model with two layers:
    - Layer 1: A dense layer with 64 units and the ReLU activation function (Study more about this)
    - Layer 2: A dense layer with one unit and the sigmoid activation function
- Compile the model by specifying the optimizer (Adam), the loss function (binary crossentropy), 
    and the metrics to evaluate during training (accuracy).
- Creation of a TensorBoard callback to visualize the training process, used to log the training progress and create visualizations
    - The log_dir argument specifies the directory where to save the log files to be parsed by TensorBoard.
    - The histogram_freq argument specifies that the histogram of the weights and biases of the layers will be logged every 1 epoch.
- Train the model on the preprocessed training data
    - The `X_train` and `y_train` variables contain the features and labels of the training set.
    - The `X_test` and `y_test` variables contain the features and labels of the test set.
    - The `validation_data` argument specifies the data that the model will be evaluated on at the end of each epoch.
    - The `epochs` argument specifies the number of epochs (iterations) to train the model. 
    - The `callbacks` argument specifies the `TensorBoard` callback to use for logging the training progress and creating visualizations.
- Save the trained model to the models directory using the pickle module. 
    - The model_path variable specifies the path and filename of the saved model. 
    - The pickle.dump() function is used to serialize the trained model and save it to a file. 
    - Finally, the function returns the trained model object.

