import pandas as pd
from titanic_analysis.data_loader import load_titanic_data
import os

def test_load_titanic_data():
    # Use a relative path based on the current file's location
    data_path = os.path.join("data", "titanic.csv")  # Adjust this if the path changes
    
    df = load_titanic_data(data_path)
    
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
