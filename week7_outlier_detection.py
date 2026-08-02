import pandas as pd

# ==========================================================
# Week 7 – Outlier Detection and Data Quality
# ==========================================================

LISTINGS_FILE = "featured_listings_with_districts.csv"
SOLD_FILE = "featured_sold_with_districts.csv"

OUTLIER_COLUMNS = [
    "ClosePrice",
    "LivingArea",
    "DaysOnMarket"
]


def add_iqr_flags(df, dataset_name):
    df = df.copy()

    print("\n" + "=" * 70)
    print(f"OUTLIER DETECTION: {dataset_name.upper()}")
    print("=" * 70)

    for col in OUTLIER_COLUMNS:
        if col not in df.columns:
            print(f"{col}: column not found")
            continue

        df[col] = pd.to_numeric(df[col], errors="coerce")

        valid_values = df[col].dropna()

        q1 = valid_values.quantile(0.25)
        q3 = valid_values.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        flag_col = f"{col}_outlier_flag"

        df[flag_col] = (
            df[col].notna()
            & (
                (df[col] < lower_bound)
                | (df[col] > upper_bound)
            )
        )

        print(f"\n{col}")
        print("Q1:", q1)
        print("Q3:", q3)
        print("IQR:", iqr)
        print("Lower bound:", lower_bound)
        print("Upper bound:", upper_bound)
        print("Outlier rows:", int(df[flag_col].sum()))

    # Business-rule invalid records
    df["business_rule_invalid_flag"] = (
        (df["ClosePrice"].notna() & (df["ClosePrice"] <= 0))
        | (df["LivingArea"].notna() & (df["LivingArea"] <= 0))
        | (df["DaysOnMarket"].notna() & (df["DaysOnMarket"] < 0))
    )

    outlier_flag_cols = [
        f"{col}_outlier_flag"
        for col in OUTLIER_COLUMNS
        if f"{col}_outlier_flag" in df.columns
    ]

    df["any_outlier_flag"] = df[outlier_flag_cols].any(axis=1)

    # Preserve full flagged dataset
    flagged_df = df.copy()

    # Create separate clean filtered dataset
    filtered_df = df[
        ~df["any_outlier_flag"]
        & ~df["business_rule_invalid_flag"]
    ].copy()

    print("\nDataset Comparison")
    print("Rows before filtering:", len(flagged_df))
    print("Rows after filtering:", len(filtered_df))
    print("Rows removed:", len(flagged_df) - len(filtered_df))

    print("\nMedian Comparison")
    for col in OUTLIER_COLUMNS:
        before_median = flagged_df[col].median()
        after_median = filtered_df[col].median()

        print(
            f"{col}: "
            f"before={before_median}, "
            f"after={after_median}"
        )

    return flagged_df, filtered_df


# Load datasets
listings = pd.read_csv(LISTINGS_FILE, low_memory=False)
sold = pd.read_csv(SOLD_FILE, low_memory=False)

# Apply outlier detection
flagged_listings, filtered_listings = add_iqr_flags(
    listings,
    "listings"
)

flagged_sold, filtered_sold = add_iqr_flags(
    sold,
    "sold"
)

# Save full flagged datasets
flagged_listings.to_csv(
    "flagged_listings.csv",
    index=False
)

flagged_sold.to_csv(
    "flagged_sold.csv",
    index=False
)

# Save clean filtered datasets
filtered_listings.to_csv(
    "filtered_listings.csv",
    index=False
)

filtered_sold.to_csv(
    "filtered_sold.csv",
    index=False
)

print("\n" + "=" * 70)
print("WEEK 7 COMPLETE")
print("=" * 70)
print("Saved flagged_listings.csv")
print("Saved flagged_sold.csv")
print("Saved filtered_listings.csv")
print("Saved filtered_sold.csv")
