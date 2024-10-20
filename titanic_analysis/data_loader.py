import pandas as pd
import os

def load_titanic_data(filepath: str = "data/titanic.csv") -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    # First, check if the provided filepath exists
    if not os.path.isfile(filepath):
        # Attempt to find a relative path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_path = os.path.join(current_dir, "data/titanic.csv")
        
        if not os.path.isfile(relative_path):
            raise FileNotFoundError(f"File not found at {filepath} or {relative_path}")
        
        # Use the relative path if the absolute path fails
        filepath = relative_path
    
    return pd.read_csv(filepath)
