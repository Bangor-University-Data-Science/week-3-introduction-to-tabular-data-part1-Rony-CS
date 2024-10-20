import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
    # Use the absolute path to your dataset for testing
    data_path = r"M:\Data Science\week-3-introduction-to-tabular-data-part1-Rony-CS\data\titanic.csv"
    
    df = load_titanic_data(data_path)
    
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
