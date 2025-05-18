# Data loading and cleaning functions
import pandas as pd
import numpy as np
from scipy import stats

def load_data(path):
    return pd.read_csv(path, parse_dates=['Timestamp'])

def clip_negative_radiation(df, irr_cols=('GHI', 'DNI', 'DHI')):
    cols = list(irr_cols)                # ← make it a list
    # sanity check
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise KeyError(f"clip_negative_radiation: missing columns {missing}")
    df[cols] = df[cols].clip(lower=0)    # now Pandas understands “these columns”
    return df

def detect_outliers(df, key_cols=('GHI','DNI','DHI','ModA','ModB','WS','WSgust'), threshold=3):
    cols = list(key_cols)
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise KeyError(f"Missing columns for outlier detection: {missing}")
    zs = np.abs(stats.zscore(df[cols], nan_policy='omit'))
    return (zs > threshold).any(axis=1)

def impute_missing(df, key_cols=('GHI','DNI','DHI','ModA','ModB','WS','WSgust')):
    for c in key_cols:
        df[c].fillna(df[c].median(), inplace=True)
    return df

def drop_outliers(df, mask):
    return df.loc[~mask].reset_index(drop=True)
