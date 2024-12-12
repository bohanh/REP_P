import os

import matplotlib.pyplot as plt
import pandas as pd

# Path to the folder containing the results
folder_path = "./results"
output_folder = "./output_graphs"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Initialize a DataFrame to collect aggregate results
aggregate_results = pd.DataFrame()


def process_file(file_path, file_name):
    df = pd.read_csv(file_path)
    df.plot(kind='bar', x='Language', y=['CPU', 'Time', 'GPU', 'DRAM'], figsize=(10, 6), logy=True)
    plt.title(f'Performance Metrics ({file_name})')
    plt.ylabel('Metrics')
    plt.xlabel('Programming Language')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(title="Metrics")
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, f"{file_name}_metrics.png"))
    plt.close()
    return df


for file_name in os.listdir(folder_path):
    if file_name.endswith(".csv"):
        file_path = os.path.join(folder_path, file_name)
        print(f"Processing file: {file_name}")
        df = process_file(file_path, file_name)
        if aggregate_results.empty:
            aggregate_results = df.copy()
        else:
            aggregate_results = pd.concat([aggregate_results, df], axis=0)

agg_metrics = aggregate_results.groupby('Language').agg(
    Mean_CPU=('CPU', 'mean'),
    Std_CPU=('CPU', 'std'),
    Mean_Time=('Time', 'mean'),
    Std_Time=('Time', 'std'),
    Mean_GPU=('GPU', 'mean'),
    Std_GPU=('GPU', 'std'),
    Mean_DRAM=('DRAM', 'mean'),
    Std_DRAM=('DRAM', 'std')
).reset_index()

agg_metrics["CPU_Rank"] = agg_metrics["Mean_CPU"].rank()
agg_metrics["Time_Rank"] = agg_metrics["Mean_Time"].rank()
agg_metrics["Overall_Rank"] = agg_metrics[["CPU_Rank", "Time_Rank"]].mean(axis=1)
agg_metrics = agg_metrics.sort_values("Overall_Rank")

plt.figure(figsize=(12, 6))
agg_metrics.plot(kind='bar', x='Language', y=["Mean_CPU", "Mean_Time", "Mean_GPU", "Mean_DRAM"], figsize=(10, 6), logy=True)
plt.title('Aggregated Performance Metrics')
plt.ylabel('Average Metrics (Log Scale)')
plt.xlabel('Programming Language')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title="Metrics")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "aggregated_metrics.png"))

print("\nFinal Efficiency Analysis:\n", agg_metrics)
