import pandas as pd
import os

def load_titanic_data(filepath: str = None) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    if filepath is None:
        # Use a default path relative to the current file's directory
        filepath = os.path.join(os.path.dirname(__file__), '../../data/titanic.csv')
    
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
    
    return df
