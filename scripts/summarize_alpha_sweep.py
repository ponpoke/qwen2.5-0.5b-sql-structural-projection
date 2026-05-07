import json
import os

def summarize_alpha_sweep():
    print("Summarizing Alpha Sweep Results...")
    # Logic to aggregate reports/sql_eval_results_qwen05b_alpha*.json
    summary_path = "reports/alpha_sweep_summary.json"
    if os.path.exists(summary_path):
        with open(summary_path, "r") as f:
            data = json.load(f)
            print(f"Loaded summary: Accuracy {data['sweep_results'][2]['accuracy'] * 100}% at alpha=16")

if __name__ == "__main__":
    summarize_alpha_sweep()
