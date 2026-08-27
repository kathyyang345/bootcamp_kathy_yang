"""
src/features.py

Feature engineering functions for Stage 09 homework.
Each function takes a DataFrame and returns it with one new column added,
so they can be chained together or used independently.
"""

import pandas as pd


def add_spend_income_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add spend_income_ratio: monthly_spend divided by income.

    Rationale: captures how much of a customer's income goes toward monthly
    spending, which can signal financial strain independent of raw income level.
    """
    df = df.copy()
    df['spend_income_ratio'] = df['monthly_spend'] / df['income']
    return df


def add_rolling_spend_mean(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """
    Add rolling_spend_mean: rolling mean of monthly_spend over `window` periods.

    Rationale: smooths out one-off spikes in spending to reveal a customer's
    underlying short-term spending trend.
    """
    df = df.copy()
    df['rolling_spend_mean'] = df['monthly_spend'].rolling(window).mean()
    return df


def add_region_frequency_encoding(df: pd.DataFrame, column: str = 'region') -> pd.DataFrame:
    """
    Add {column}_freq: frequency encoding of a categorical column.

    Rationale: avoids the false ordering imposed by label encoding while
    still preserving how common each category is in the dataset, which
    one-hot encoding discards.
    """
    df = df.copy()
    freq = df[column].value_counts(normalize=True)
    df[f'{column}_freq'] = df[column].map(freq)
    return df


def build_all_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all engineered features in sequence and return the resulting DataFrame.
    """
    df = add_spend_income_ratio(df)
    df = add_rolling_spend_mean(df)
    df = add_region_frequency_encoding(df)
    return df