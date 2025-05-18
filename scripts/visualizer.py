import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_time_series(df):
    fig, ax = plt.subplots(figsize=(12,4))
    df.set_index('Timestamp')[['GHI','DNI','DHI']].plot(ax=ax)
    ax.set_title('Solar Irradiance Over Time')
    ax.set_ylabel('W/m²')
    plt.show()

def plot_cleaning_impact(df):
    avg_mod = df.groupby('Cleaning')[['ModA','ModB']].mean()
    avg_mod.plot(kind='bar', figsize=(6,4), rot=0)
    plt.title('Module Output Before vs. After Cleaning')
    plt.ylabel('Mean Module Reading')
    plt.show()

def plot_correlation(df):
    features = ['GHI','DNI','DHI','TModA','TModB','WS','RH']
    plt.figure(figsize=(6,5))
    sns.heatmap(df[features].corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Feature Correlations')
    plt.show()

def plot_histogram(df):
    plt.figure(figsize=(6,3))
    df['GHI'].hist(bins=50)
    plt.title('GHI Distribution')
    plt.xlabel('GHI (W/m²)')
    plt.show()

def plot_wind_rose(df, bin_size=30):
    df['WD_bin'] = (df['WD'] // bin_size) * bin_size
    wind = df.groupby('WD_bin')['WS'].mean().reset_index()
    angles = np.deg2rad(wind['WD_bin'])
    ws_avg = wind['WS']
    fig = plt.figure(figsize=(6,6))
    ax = plt.subplot(111, projection='polar')
    ax.bar(angles, ws_avg, width=np.deg2rad(bin_size), alpha=0.7)
    ax.set_title('Avg Wind Speed by Direction', y=1.08)
    plt.show()

def plot_humidity_temp(df):
    plt.figure(figsize=(6,4))
    sc = plt.scatter(df['RH'], df['Tamb'], c=df['GHI'], alpha=0.6)
    plt.colorbar(sc, label='GHI')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Ambient Temp (°C)')
    plt.title('Humidity vs. Temperature (colour = GHI)')
    plt.show()

def plot_bubble(df):
    plt.figure(figsize=(6,4))
    sizes = (df['RH'] - df['RH'].min()) * 3
    plt.scatter(df['Tamb'], df['GHI'], s=sizes, alpha=0.4, edgecolor='k')
    plt.xlabel('Ambient Temp (°C)')
    plt.ylabel('GHI (W/m²)')
    plt.title('Bubble Chart: GHI vs Temp (bubble = RH)')
    plt.show()
