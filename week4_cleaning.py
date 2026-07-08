import pandas as pd

# Load current residential datasets
listings = pd.read_csv("listings.csv", low_memory=False)
sold = pd.read_csv("sold.csv", low_memory=False)

print("=" * 60)
print("WEEK 4 CLEANING START")
print("=" * 60)

print("\nBefore Cleaning")
print("Listings rows:", len(listings))
print("Sold rows:", len(sold))


def clean_dataset(df, dataset_name):
    df = df.copy()

    print("\n" + "=" * 60)
    print(f"CLEANING {dataset_name.upper()}")
    print("=" * 60)

    # Date columns
    date_cols = [
        "CloseDate",
        "PurchaseContractDate",
        "ListingContractDate",
        "ContractStatusChangeDate"
    ]

    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Numeric columns
    numeric_cols = [
        "ClosePrice",
        "ListPrice",
        "OriginalListPrice",
        "LivingArea",
        "LotSizeAcres",
        "BedroomsTotal",
        "BathroomsTotalInteger",
        "DaysOnMarket",
        "Latitude",
        "Longitude"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Invalid value flags
    if "ClosePrice" in df.columns:
        df["invalid_closeprice_flag"] = df["ClosePrice"] <= 0

    if "LivingArea" in df.columns:
        df["invalid_livingarea_flag"] = df["LivingArea"] <= 0

    if "DaysOnMarket" in df.columns:
        df["negative_dom_flag"] = df["DaysOnMarket"] < 0

    if "BedroomsTotal" in df.columns:
        df["negative_bedrooms_flag"] = df["BedroomsTotal"] < 0

    if "BathroomsTotalInteger" in df.columns:
        df["negative_bathrooms_flag"] = df["BathroomsTotalInteger"] < 0

    # Date consistency flags
    if "ListingContractDate" in df.columns and "CloseDate" in df.columns:
        df["listing_after_close_flag"] = (
            df["ListingContractDate"].notna()
            & df["CloseDate"].notna()
            & (df["ListingContractDate"] > df["CloseDate"])
        )

    if "PurchaseContractDate" in df.columns and "CloseDate" in df.columns:
        df["purchase_after_close_flag"] = (
            df["PurchaseContractDate"].notna()
            & df["CloseDate"].notna()
            & (df["PurchaseContractDate"] > df["CloseDate"])
        )

    if (
        "ListingContractDate" in df.columns
        and "PurchaseContractDate" in df.columns
        and "CloseDate" in df.columns
    ):
        df["negative_timeline_flag"] = (
            df["ListingContractDate"].notna()
            & df["PurchaseContractDate"].notna()
            & df["CloseDate"].notna()
            & (
                (df["ListingContractDate"] > df["PurchaseContractDate"])
                | (df["PurchaseContractDate"] > df["CloseDate"])
                | (df["ListingContractDate"] > df["CloseDate"])
            )
        )

    # Geographic quality flags
    if "Latitude" in df.columns and "Longitude" in df.columns:
        df["missing_coordinate_flag"] = (
            df["Latitude"].isna() | df["Longitude"].isna()
        )

        df["zero_coordinate_flag"] = (
            (df["Latitude"] == 0) | (df["Longitude"] == 0)
        )

        df["positive_longitude_flag"] = df["Longitude"] > 0

        # Approximate California bounding box
        df["out_of_state_coordinate_flag"] = (
            df["Latitude"].notna()
            & df["Longitude"].notna()
            & (
                (df["Latitude"] < 32)
                | (df["Latitude"] > 43)
                | (df["Longitude"] < -125)
                | (df["Longitude"] > -114)
            )
        )

    # Print flag counts
    flag_cols = [col for col in df.columns if col.endswith("_flag")]

    print("\nFlag Counts")
    for col in flag_cols:
        print(col + ":", int(df[col].sum()))

    print("\nData Types for Key Columns")
    key_cols = date_cols + numeric_cols
    existing_key_cols = [col for col in key_cols if col in df.columns]
    print(df[existing_key_cols].dtypes)

    print("\nRows after cleaning:", len(df))

    return df


cleaned_listings = clean_dataset(listings, "listings")
cleaned_sold = clean_dataset(sold, "sold")

# Save cleaned datasets
cleaned_listings.to_csv("cleaned_listings.csv", index=False)
cleaned_sold.to_csv("cleaned_sold.csv", index=False)

print("\n" + "=" * 60)
print("WEEK 4 CLEANING COMPLETE")
print("=" * 60)
print("Saved cleaned_listings.csv")
print("Saved cleaned_sold.csv")
