import pandas as pd

results = pd.read_csv("data/dml_results.csv")

print("DML Results Loaded")
print("Total customers:", len(results))

avg_effect = results["treatment_effect"].mean()
min_effect = results["treatment_effect"].min()
max_effect = results["treatment_effect"].max()

print("\nAverage Treatment Effect:", round(avg_effect, 4))
print("Minimum Treatment Effect:", round(min_effect, 4))
print("Maximum Treatment Effect:", round(max_effect, 4))

results["recommendation"] = results["treatment_effect"].apply(
    lambda x: "High discount impact"
    if x > avg_effect
    else "Normal discount impact"
)

results.to_csv("data/dml_analysis.csv", index=False)

print("\nAnalysis completed!")
print("Saved: data/dml_analysis.csv")