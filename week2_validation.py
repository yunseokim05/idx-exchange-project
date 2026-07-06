import pandas as pd

listings = pd.read_csv("listings.csv", low_memory=False)
sold = pd.read_csv("sold.csv", low_memory=False)

print("=" * 50)
print("LISTINGS")
print("=" * 50)
print("Rows:", len(listings))
print("Columns:", len(listings.columns))
print()

print("PropertyType values:")
print(listings["PropertyType"].value_counts(dropna=False))
print()

print("Top 20 columns with most missing values:")
missing = listings.isnull().sum().sort_values(ascending=False)
print(missing.head(20))
print()

print("=" * 50)
print("SOLD")
print("=" * 50)
print("Rows:", len(sold))
print("Columns:", len(sold.columns))
print()

print("PropertyType values:")
print(sold["PropertyType"].value_counts(dropna=False))
print()

print("Top 20 columns with most missing values:")
missing = sold.isnull().sum().sort_values(ascending=False)
print(missing.head(20))
