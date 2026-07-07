import pandas as pd
import matplotlib.pyplot as plt

# Load data
sold = pd.read_csv("sold.csv", low_memory=False)

# Convert key numeric columns
numeric_columns = [
    "ClosePrice",
    "ListPrice",
    "OriginalListPrice",
    "LivingArea",
    "LotSizeAcres",
    "BedroomsTotal",
    "BathroomsTotalInteger",
    "DaysOnMarket",
    "YearBuilt"
]

print("=" * 60)
print("WEEK 3 EDA SUMMARY")
print("=" * 60)

print("\nDataset Shape")
print("Rows:", len(sold))
print("Columns:", len(sold.columns))

print("\nProperty Type Distribution")
print(sold["PropertyType"].value_counts(dropna=False))
print("\nProperty Type Share (%)")
print((sold["PropertyType"].value_counts(normalize=True, dropna=False) * 100).round(2))

for col in numeric_columns:
    print("\n" + "=" * 60)
    print(col)
    print("=" * 60)

    if col not in sold.columns:
        print(f"{col} not found.")
        continue

    values = pd.to_numeric(sold[col], errors="coerce")

    print(values.describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99]))
    print("Missing values:", values.isna().sum())
    print("Mean:", values.mean())
    print("Median:", values.median())
    print("Min:", values.min())
    print("Max:", values.max())

    # Histogram
    clean_values = values.dropna()
    if len(clean_values) > 0:
        clean_values.hist(bins=50)
        plt.title(f"{col} Histogram")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.savefig(f"{col}_hist.png")
        plt.close()

        # Boxplot
        clean_values.plot.box()
        plt.title(f"{col} Boxplot")
        plt.ylabel(col)
        plt.savefig(f"{col}_box.png")
        plt.close()

print("\n" + "=" * 60)
print("SUGGESTED INTERN QUESTIONS")
print("=" * 60)

# Average and median close prices
sold["ClosePrice"] = pd.to_numeric(sold["ClosePrice"], errors="coerce")
sold["ListPrice"] = pd.to_numeric(sold["ListPrice"], errors="coerce")

print("\nClose Price")
print("Average Close Price:", sold["ClosePrice"].mean())
print("Median Close Price:", sold["ClosePrice"].median())

# Days on Market distribution
sold["DaysOnMarket"] = pd.to_numeric(sold["DaysOnMarket"], errors="coerce")
print("\nDays on Market")
print(sold["DaysOnMarket"].describe(percentiles=[0.25, 0.5, 0.75, 0.9, 0.95, 0.99]))

# Sold above / below list price
valid_price = sold[["ClosePrice", "ListPrice"]].dropna()
above_list = (valid_price["ClosePrice"] > valid_price["ListPrice"]).mean() * 100
below_list = (valid_price["ClosePrice"] < valid_price["ListPrice"]).mean() * 100
at_list = (valid_price["ClosePrice"] == valid_price["ListPrice"]).mean() * 100

print("\nSold Compared to List Price")
print(f"Sold Above List: {above_list:.2f}%")
print(f"Sold Below List: {below_list:.2f}%")
print(f"Sold At List: {at_list:.2f}%")

# Date consistency check
sold["CloseDate"] = pd.to_datetime(sold["CloseDate"], errors="coerce")
sold["ListingContractDate"] = pd.to_datetime(sold["ListingContractDate"], errors="coerce")

listing_after_close = (sold["ListingContractDate"] > sold["CloseDate"]).sum()
print("\nDate Consistency")
print("Records where ListingContractDate is after CloseDate:", listing_after_close)

# Counties with highest median prices
if "CountyOrParish" in sold.columns:
    print("\nTop 10 Counties by Median Close Price")
    county_median = (
        sold.groupby("CountyOrParish")["ClosePrice"]
        .median()
        .sort_values(ascending=False)
        .head(10)
    )
    print(county_median)

print("\nDone: Week 3 EDA completed.")
