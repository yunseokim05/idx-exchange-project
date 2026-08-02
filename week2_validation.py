import pandas as pd

# ==========================================================
# Week 2 – Dataset Structuring and Validation
# ==========================================================

LISTINGS_FILE = "listings.csv"
SOLD_FILE = "sold.csv"

listings = pd.read_csv(LISTINGS_FILE, low_memory=False)
sold = pd.read_csv(SOLD_FILE, low_memory=False)


def validate_dataset(df, dataset_name, output_file):
    df = df.copy()

    print("\n" + "=" * 70)
    print(dataset_name.upper())
    print("=" * 70)

    # ------------------------------------------------------
    # Dataset structure
    # ------------------------------------------------------

    print("\nDataset shape")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\nColumn names")
    print(df.columns.tolist())

    print("\nFirst 5 rows")
    print(df.head())

    print("\nColumn data types")
    print(df.dtypes)

    # ------------------------------------------------------
    # Property type review and Residential filtering
    # ------------------------------------------------------

    if "PropertyType" in df.columns:
        print("\nUnique PropertyType values")
        print(df["PropertyType"].unique())

        print("\nPropertyType counts")
        print(df["PropertyType"].value_counts(dropna=False))

        before_filter = len(df)

        df = df[df["PropertyType"] == "Residential"].copy()

        after_filter = len(df)

        print("\nResidential filter")
        print("Rows before filter:", before_filter)
        print("Rows after filter:", after_filter)
        print("Rows removed:", before_filter - after_filter)

    # ------------------------------------------------------
    # Missing value report
    # ------------------------------------------------------

    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df) * 100).round(2)

    missing_report = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percent": missing_percent
    }).sort_values(
        by="missing_percent",
        ascending=False
    )

    print("\nMissing value summary")
    print(missing_report)

    print("\nColumns above 90% missing")
    high_missing = missing_report[
        missing_report["missing_percent"] > 90
    ]

    if high_missing.empty:
        print("No columns exceed 90% missing.")
    else:
        print(high_missing)

    # Save missing report for documentation
    missing_report.to_csv(
        f"{dataset_name.lower()}_missing_report.csv"
    )

    # ------------------------------------------------------
    # Core numeric distribution summary
    # ------------------------------------------------------

    core_numeric_columns = [
        "ClosePrice",
        "LivingArea",
        "DaysOnMarket"
    ]

    print("\nCore numeric distribution summary")

    for col in core_numeric_columns:
        if col not in df.columns:
            print(f"\n{col}: column not found")
            continue

        values = pd.to_numeric(df[col], errors="coerce")

        print("\n" + "-" * 50)
        print(col)
        print("-" * 50)

        print(
            values.describe(
                percentiles=[
                    0.01,
                    0.05,
                    0.25,
                    0.50,
                    0.75,
                    0.95,
                    0.99
                ]
            )
        )

        print("Missing values:", values.isna().sum())
        print("Minimum:", values.min())
        print("Maximum:", values.max())
        print("Mean:", values.mean())
        print("Median:", values.median())

    # ------------------------------------------------------
    # Save validated Residential dataset
    # ------------------------------------------------------

    df.to_csv(output_file, index=False)

    print("\nSaved validated dataset:", output_file)

    return df


validated_listings = validate_dataset(
    listings,
    "Listings",
    "validated_listings.csv"
)

validated_sold = validate_dataset(
    sold,
    "Sold",
    "validated_sold.csv"
)

print("\n" + "=" * 70)
print("WEEK 2 VALIDATION COMPLETE")
print("=" * 70)

print("Saved validated_listings.csv")
print("Saved validated_sold.csv")
print("Saved listings_missing_report.csv")
print("Saved sold_missing_report.csv")
