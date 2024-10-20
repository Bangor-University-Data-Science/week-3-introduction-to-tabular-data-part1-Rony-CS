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
    # Try to use the provided filepath, falling back to a relative path
    if not os.path.isfile(filepath):
        default_path = os.path.join(os.path.dirname(__file__), "data/titanic.csv")
        if not os.path.isfile(default_path):
            raise FileNotFoundError(f"File not found: {filepath} or {default_path}")
        filepath = default_path
    
    return pd.read_csv(filepath)
