import pandas as pd
import os

def load_titanic_data(filepath: str = r"M:\Data Science\week-3-introduction-to-tabular-data-part1-Rony-CS\data\titanic.csv") -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    # Check if the provided filepath exists
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    return pd.read_csv(filepath)
