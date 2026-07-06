import pandas as pd

# Load data
sold = pd.read_csv("sold.csv", low_memory=False)

# Columns to analyze
columns = ["ClosePrice", "LivingArea", "DaysOnMarket"]

for col in columns:
    print("=" * 60)
    print(f"{col}")
    print("=" * 60)

    if col not in sold.columns:
        print(f"{col} not found.\n")
        continue

    values = pd.to_numeric(sold[col], errors="coerce")

    print(values.describe())

    print("\nMissing values:", values.isna().sum())
    print("Median:", values.median())
    print("Mean:", values.mean())
    print()
