import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
    # Provide the absolute path to your dataset for testing
    df = load_titanic_data(r"M:\Data Science\week-3-introduction-to-tabular-data-part1-Rony-CS\data\titanic.csv")
    
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
