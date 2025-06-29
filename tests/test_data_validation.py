import pytest
import pandas as pd

@pytest.fixture(scope="module")
def iris_df():
    return pd.read_csv("iris.csv")

def test_data_shape(iris_df):
    assert iris_df.shape[1] == 5
    assert iris_df.shape[0] > 0

def test_no_missing_values(iris_df):
    assert iris_df.isnull().sum().sum() == 0, "Missing values found"
