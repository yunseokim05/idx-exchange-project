import numpy as np
import pandas as pd

# ==========================================================
# Week 6 – Feature Engineering and Market Metrics
# ==========================================================

# Load cleaned datasets from Weeks 4–5
listings = pd.read_csv("cleaned_listings.csv", low_memory=False)
sold = pd.read_csv("cleaned_sold.csv", low_memory=False)

print("=" * 70)
print("WEEK 6 FEATURE ENGINEERING")
print("=" * 70)

print("Listings rows:", len(listings))
print("Sold rows:", len(sold))


# ----------------------------------------------------------
# Convert date columns
# ----------------------------------------------------------

date_columns = [
    "CloseDate",
    "PurchaseContractDate",
    "ListingContractDate",
    "ContractStatusChangeDate"
]

for col in date_columns:
    if col in listings.columns:
        listings[col] = pd.to_datetime(listings[col], errors="coerce")

    if col in sold.columns:
        sold[col] = pd.to_datetime(sold[col], errors="coerce")


# ----------------------------------------------------------
# Convert numeric columns
# ----------------------------------------------------------

numeric_columns = [
    "ClosePrice",
    "OriginalListPrice",
    "ListPrice",
    "LivingArea",
    "DaysOnMarket"
]

for col in numeric_columns:
    if col in listings.columns:
        listings[col] = pd.to_numeric(listings[col], errors="coerce")

    if col in sold.columns:
        sold[col] = pd.to_numeric(sold[col], errors="coerce")


# ----------------------------------------------------------
# Safe division function
# ----------------------------------------------------------

def safe_divide(numerator, denominator):
    return np.where(
        denominator.notna() & (denominator > 0),
        numerator / denominator,
        np.nan
    )


# ----------------------------------------------------------
# Sold dataset market metrics
# ----------------------------------------------------------

sold["PriceRatio"] = safe_divide(
    sold["ClosePrice"],
    sold["OriginalListPrice"]
)

sold["CloseToOriginalListRatio"] = sold["PriceRatio"]

sold["PricePerSqFt"] = safe_divide(
    sold["ClosePrice"],
    sold["LivingArea"]
)

sold["DaysOnMarketMetric"] = sold["DaysOnMarket"]

sold["Year"] = sold["CloseDate"].dt.year
sold["Month"] = sold["CloseDate"].dt.month
sold["YrMo"] = sold["CloseDate"].dt.to_period("M").astype("string")

sold["ListingToContractDays"] = (
    sold["PurchaseContractDate"]
    - sold["ListingContractDate"]
).dt.days

sold["ContractToCloseDays"] = (
    sold["CloseDate"]
    - sold["PurchaseContractDate"]
).dt.days


# ----------------------------------------------------------
# Listings dataset time fields
# ----------------------------------------------------------

listings["Year"] = listings["ListingContractDate"].dt.year
listings["Month"] = listings["ListingContractDate"].dt.month
listings["YrMo"] = (
    listings["ListingContractDate"]
    .dt.to_period("M")
    .astype("string")
)

# Add applicable price metrics to listings
listings["PriceRatio"] = safe_divide(
    listings["ClosePrice"],
    listings["OriginalListPrice"]
)

listings["CloseToOriginalListRatio"] = listings["PriceRatio"]

listings["PricePerSqFt"] = safe_divide(
    listings["ClosePrice"],
    listings["LivingArea"]
)

listings["DaysOnMarketMetric"] = listings["DaysOnMarket"]

listings["ListingToContractDays"] = (
    listings["PurchaseContractDate"]
    - listings["ListingContractDate"]
).dt.days

listings["ContractToCloseDays"] = (
    listings["CloseDate"]
    - listings["PurchaseContractDate"]
).dt.days


# ----------------------------------------------------------
# Sample output
# ----------------------------------------------------------

feature_columns = [
    "ClosePrice",
    "OriginalListPrice",
    "LivingArea",
    "PriceRatio",
    "CloseToOriginalListRatio",
    "PricePerSqFt",
    "DaysOnMarketMetric",
    "Year",
    "Month",
    "YrMo",
    "ListingToContractDays",
    "ContractToCloseDays"
]

print("\nSample engineered metrics:")
print(sold[feature_columns].head(10))


# ----------------------------------------------------------
# Feature summary
# ----------------------------------------------------------

print("\nFeature summary:")
print(
    sold[
        [
            "PriceRatio",
            "CloseToOriginalListRatio",
            "PricePerSqFt",
            "DaysOnMarketMetric",
            "ListingToContractDays",
            "ContractToCloseDays"
        ]
    ].describe()
)


# ----------------------------------------------------------
# Segmented market summary by county
# ----------------------------------------------------------

county_summary = (
    sold.groupby("CountyOrParish", dropna=False)
    .agg(
        UnitsSold=("ListingKey", "count"),
        MedianClosePrice=("ClosePrice", "median"),
        MedianPricePerSqFt=("PricePerSqFt", "median"),
        AveragePriceRatio=("PriceRatio", "mean"),
        AverageDaysOnMarket=("DaysOnMarketMetric", "mean")
    )
    .sort_values("UnitsSold", ascending=False)
)

print("\nCounty summary:")
print(county_summary.head(20))

county_summary.to_csv("county_market_summary.csv")


# ----------------------------------------------------------
# Save featured datasets
# ----------------------------------------------------------

listings.to_csv("featured_listings.csv", index=False)
sold.to_csv("featured_sold.csv", index=False)

print("\nWeek 6 complete.")
print("Saved featured_listings.csv")
print("Saved featured_sold.csv")
print("Saved county_market_summary.csv")
