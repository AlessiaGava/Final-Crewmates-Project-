import pandas as pd


def read_volley(path):
    if path.split('.')[-1] != 'csv':
        return False

    try:
        df = pd.read_csv(path, sep=";")
        df.set_index('currency', inplace=True)
    except Exception:
        return False
    return df
