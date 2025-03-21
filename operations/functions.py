

import numpy as np
import pandas as pd
import scipy.stats as stats
import streamlit as st


# Function to detect outliers
def zscore_outliers(my_data, column_name, threshold=3):
    """
    Detects outliers in a given column using the Z-score method.

    Parameters:
    - my_data (pd.DataFrame): The dataset.
    - column_name (str): Column to check for outliers.
    - threshold (float): Z-score threshold (default = 3).

    Returns:
    - List of outlier indices.
    """
    if column_name not in my_data.columns:
        return "Column not found in the dataset.", None
    
    column = my_data[column_name].dropna()

    if column.empty:
        return "No valid data points in the column.", None
    
    zscores = np.abs(stats.zscore(column))
    outliers = column[zscores > threshold]
    
    return my_data.loc[outliers.index].index.tolist() if not outliers.empty else "No outliers detected.", outliers