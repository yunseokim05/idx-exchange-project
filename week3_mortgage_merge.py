import pandas as pd

# Load datasets
listings = pd.read_csv("listings.csv", low_memory=False)
sold = pd.read_csv("sold.csv", low_memory=False)

# Fetch mortgage rate data from FRED
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=["observation_date"])
mortgage.columns = ["date", "rate_30yr_fixed"]

# Convert weekly data to monthly average
mortgage["year_month"] = mortgage["date"].dt.to_period("M")
mortgage_monthly = (
    mortgage.groupby("year_month")["rate_30yr_fixed"]
    .mean()
    .reset_index()
)

# Create matching year_month keys
sold["CloseDate"] = pd.to_datetime(sold["CloseDate"], errors="coerce")
listings["ListingContractDate"] = pd.to_datetime(
    listings["ListingContractDate"], errors="coerce"
)

sold["year_month"] = sold["CloseDate"].dt.to_period("M")
listings["year_month"] = listings["ListingContractDate"].dt.to_period("M")

# Merge mortgage rates
sold_with_rates = sold.merge(
    mortgage_monthly,
    on="year_month",
    how="left"
)

listings_with_rates = listings.merge(
    mortgage_monthly,
    on="year_month",
    how="left"
)

# Validation
print("Sold missing mortgage rates:",
      sold_with_rates["rate_30yr_fixed"].isna().sum())

print("Listings missing mortgage rates:",
      listings_with_rates["rate_30yr_fixed"].isna().sum())

# Save
sold_with_rates.to_csv("sold_with_rates.csv", index=False)
listings_with_rates.to_csv("listings_with_rates.csv", index=False)

print("Done.")
