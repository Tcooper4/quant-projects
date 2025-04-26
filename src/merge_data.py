import pandas as pd

def merge_data(ticker: str) -> pd.DataFrame:
    """
    Generate dummy stock close price data for a given ticker.
    """
    dates = pd.date_range(start="2020-01-01", periods=100)
    data = pd.DataFrame({f"{ticker}_Close": range(100)}, index=dates)
    return data
