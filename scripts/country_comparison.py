import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, kruskal

# Plot boxplots for a list of metrics
def plot_metric_boxplots(df_all, metrics=["GHI", "DNI", "DHI"]):
    for metric in metrics:
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df_all, x="Country", y=metric, palette="Set2")
        plt.title(f"{metric} Distribution by Country")
        plt.ylabel(f"{metric} (W/m²)")
        plt.xlabel("Country")
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()


# Create summary table of mean, median, std
def compute_summary_statistics(df_all):
    summary = df_all.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])
    summary.columns = ['_'.join(col) for col in summary.columns]
    return summary.reset_index()


# Run one-way ANOVA and Kruskal-Wallis tests
def run_statistical_tests(benin, sierraleone, togo):
    ghi_benin = benin["GHI"]
    ghi_sl = sierraleone["GHI"]
    ghi_togo = togo["GHI"]

    f_stat, p_anova = f_oneway(ghi_benin, ghi_sl, ghi_togo)
    h_stat, p_kruskal = kruskal(ghi_benin, ghi_sl, ghi_togo)

    return {
        "ANOVA_p_value": p_anova,
        "Kruskal_p_value": p_kruskal
    }


# Bar chart of average GHI
def plot_average_ghi(df_all):
    avg_ghi = df_all.groupby("Country")["GHI"].mean().sort_values(ascending=False)

    plt.figure(figsize=(6, 4))
    sns.barplot(x=avg_ghi.index, y=avg_ghi.values, palette="viridis")
    plt.ylabel("Average GHI (W/m²)")
    plt.title("Average GHI by Country")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
