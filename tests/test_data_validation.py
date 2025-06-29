import pandas as pd

def test_data_shape():
        df = pd.read_csv("../iris.csv")
        assert df.shape == (150, 5), "Expected shape (150, 5)"
                
def test_no_missing_values():
        df = pd.read_csv("../iris.csv")
        assert df.isnull().sum().sum() == 0, "Missing values found"

