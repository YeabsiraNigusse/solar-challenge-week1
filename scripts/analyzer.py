def summarize(df):
    print('Shape:', df.shape)
    display(df.head())
    display(df.describe(include='all').T)

def missing_report(df, threshold=0.05):
    na = df.isna().sum().sort_values(ascending=False)
    print('Missing per column:')
    display(na[na>0])
    important = na[na > threshold * len(df)]
    print('Columns with >5% nulls:', important.index.tolist())
