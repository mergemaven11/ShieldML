import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pathlib as pl
from tqdm import tqdm

from src.utils.sml_logger import Logger

# from src.utils.sml_logger import Logger

def load_and_process(raw_path):
    # Load the data 
    # we should pass a path to file
    # raw_path = 'data/raw/fraudTest.csv'
    path = pl.Path(raw_path)
    df = pd.read_csv(path)
    Logger.info(f"Loaded data from {raw_path}")
    
    # Data Cleaning: Drop the duplicates and missing values
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    feat_removed = [
        'trans_date_trans_time', 
        'cc_num', 
        'first', 
        'last', 
        'street', 
        'city', 
        'state', 
        'zip',
        'job', 
        'dob', 
        'trans_num', 
        'unix_time'
        ]
    
    # Feature selection: remove useless features
    df.drop(feat_removed, axis=1, inplace=True)
    
    Logger.info(f"Removed {len(feat_removed)} features\n Removed Feat: {feat_removed}")
    # -> Feature Scaling: Scale numerical features using StandardScaler = 
    # It takes your data and transforms it so that each feature has a mean of 0 and a standard deviation of 1
    numerical_features = ['amt', 'lat', 'long', 'city_pop', 'merch_lat', 'merch_long']
    scaler = StandardScaler()
    # df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    # Using tqdm to show progress bar
    for col in tqdm(numerical_features, desc="Scaling numerical features"):
        df[col] = scaler.fit_transform(df[[col]])
    
    # Encoding categorical variables: Use one-hot encoding for categorical variables
    # We do this to convert categorical variables into a number so the ML algorithm can understand (0,1) 
    categorical_cols = ["merchant", 'category', 'gender']
    df = pd.get_dummies(df, columns=categorical_cols)
    
    # Split data into training and test sets
    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save the preprocessed data to the 'processed' directory
    dest_path = pl.Path('data\processed\preprocessed_data.csv')
    df.to_csv(dest_path, index=False)
    Logger.info('Saved preprocessed data to {dest_path}')
    return X_train, X_test, y_train, y_test