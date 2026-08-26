"""
cleaning.py — Reusable data preprocessing functions for Stage 6 homework.
"""




def fill_missing_median(df, columns):
    """
    Fill missing values in the given numeric columns with each column's median.

    Assumption: missingness in these columns is MCAR or MAR (i.e., not
    systematically related to the missing value itself), so replacing it
    with the median is a reasonable, low-bias estimate that won't be
    skewed by outliers.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to clean.
    columns : list of str
        Names of numeric columns to fill.

    Returns
    -------
    pandas.DataFrame
        A copy of df with missing values in `columns` filled by median.
    """
    df = df.copy()
    for col in columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
    return df



def drop_missing(df, threshold=0.5):
    """
    Drop columns whose missing-value proportion exceeds `threshold`.

    Assumption: columns with excessive missingness carry too little
    information to be reliably imputed, and are treated as non-essential
    to the analysis. This may discard rare-but-valid signals if the
    threshold is set too aggressively — a tradeoff worth documenting.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to clean.
    threshold : float, default 0.5
        Maximum allowed proportion of missing values (0 to 1) in a column
        before it is dropped. E.g. 0.5 means: drop any column that is
        more than 50% missing.

    Returns
    -------
    pandas.DataFrame
        A copy of df with high-missingness columns removed.
    """
    df = df.copy()
    missing_fraction = df.isna().mean()
    cols_to_drop = missing_fraction[missing_fraction > threshold].index
    return df.drop(columns=cols_to_drop)



def normalize_data(df, columns):
    """
    Scale the given numeric columns to the [0, 1] range (min-max scaling).

    Assumption: the min and max values observed in the data are
    representative of the true range of each feature (i.e., not extreme
    outliers or data-entry errors). If a column is constant (min == max),
    it is left unchanged to avoid a divide-by-zero error.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to clean.
    columns : list of str
        Names of numeric columns to scale.

    Returns
    -------
    pandas.DataFrame
        A copy of df with `columns` rescaled to [0, 1].
    """
    df = df.copy()
    for col in columns:
        col_min = df[col].min()
        col_max = df[col].max()
        if col_max == col_min:
            continue  # avoid divide-by-zero for a constant column
        df[col] = (df[col] - col_min) / (col_max - col_min)
    return df