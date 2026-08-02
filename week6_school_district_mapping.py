import pandas as pd
import geopandas as gpd

# ==========================================================
# Week 6 – Unified School District Spatial Mapping
# ==========================================================

GEOJSON_FILE = "DistrictAreas2526_-284845464123469011.geojson"
LISTINGS_FILE = "featured_listings.csv"
SOLD_FILE = "featured_sold.csv"

LISTINGS_OUTPUT = "featured_listings_with_districts.csv"
SOLD_OUTPUT = "featured_sold_with_districts.csv"

CHUNK_SIZE = 100000


# ----------------------------------------------------------
# Load and prepare school district boundaries
# ----------------------------------------------------------

districts = gpd.read_file(GEOJSON_FILE)

print("=" * 70)
print("SCHOOL DISTRICT MAPPING")
print("=" * 70)

print("Original district records:", len(districts))
print("Original CRS:", districts.crs)

# Keep Unified School Districts only
unified_districts = districts[
    districts["DistrictType"].astype(str).str.strip().eq("Unified")
].copy()

print("Unified district records:", len(unified_districts))

# Convert district polygons to latitude/longitude CRS
unified_districts = unified_districts.to_crs("EPSG:4326")

# Keep only fields needed for the spatial join
unified_districts = unified_districts[
    ["DistrictName", "geometry"]
].copy()


# ----------------------------------------------------------
# Spatial mapping function
# ----------------------------------------------------------

def add_school_districts(input_file, output_file, dataset_name):
    print("\n" + "=" * 70)
    print(f"PROCESSING {dataset_name.upper()}")
    print("=" * 70)

    df = pd.read_csv(input_file, low_memory=False)

    print("Input rows:", len(df))

    # Convert coordinates to numeric values
    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")

    # Start with an empty district column so every original row is preserved
    df["UnifiedSchoolDistrict"] = pd.NA

    # Only spatially map plausible California coordinates
    valid_mask = (
        df["Latitude"].notna()
        & df["Longitude"].notna()
        & df["Latitude"].between(32, 43)
        & df["Longitude"].between(-125, -114)
    )

    valid_indices = df.index[valid_mask]

    print("Rows with valid California coordinates:", len(valid_indices))
    print("Rows without valid coordinates:", len(df) - len(valid_indices))

    # Process in chunks to reduce memory usage
    for start in range(0, len(valid_indices), CHUNK_SIZE):
        chunk_indices = valid_indices[start:start + CHUNK_SIZE]
        chunk = df.loc[chunk_indices].copy()

        points = gpd.points_from_xy(
            chunk["Longitude"],
            chunk["Latitude"]
        )

        properties_gdf = gpd.GeoDataFrame(
            chunk,
            geometry=points,
            crs="EPSG:4326"
        )

        joined = gpd.sjoin(
            properties_gdf,
            unified_districts,
            how="left",
            predicate="within"
        )

        # Protect against duplicate matches along overlapping boundaries
        joined = joined[
            ~joined.index.duplicated(keep="first")
        ]

        df.loc[joined.index, "UnifiedSchoolDistrict"] = (
            joined["DistrictName"]
        )

        completed = min(start + CHUNK_SIZE, len(valid_indices))
        print(
            f"Mapped {completed:,} of "
            f"{len(valid_indices):,} valid-coordinate rows"
        )

    matched = df["UnifiedSchoolDistrict"].notna().sum()
    unmatched = df["UnifiedSchoolDistrict"].isna().sum()

    print("\nMapping results")
    print("Matched district rows:", matched)
    print("Unmatched district rows:", unmatched)
    print("Match rate:", f"{matched / len(df) * 100:.2f}%")

    print("\nTop Unified School Districts")
    print(df["UnifiedSchoolDistrict"].value_counts().head(10))

    df.to_csv(output_file, index=False)

    print("\nSaved:", output_file)


# ----------------------------------------------------------
# Map both datasets
# ----------------------------------------------------------

add_school_districts(
    LISTINGS_FILE,
    LISTINGS_OUTPUT,
    "featured listings"
)

add_school_districts(
    SOLD_FILE,
    SOLD_OUTPUT,
    "featured sold"
)

print("\n" + "=" * 70)
print("SCHOOL DISTRICT MAPPING COMPLETE")
print("=" * 70)
print("Saved:", LISTINGS_OUTPUT)
print("Saved:", SOLD_OUTPUT)
