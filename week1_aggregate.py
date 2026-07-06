import pandas as pd
from pathlib import Path

months = [f"{y}{m:02d}" for y in [2024, 2025] for m in range(1, 13)] + [f"2026{m:02d}" for m in range(1, 6)]

def pick_file(prefix, month):
    normal = Path(f"{prefix}{month}.csv")
    filled = Path(f"{prefix}{month}_filled.csv")
    if normal.exists():
        return normal
    if filled.exists():
        return filled
    raise FileNotFoundError(f"Missing: {normal.name} or {filled.name}")

listing_files = [pick_file("CRMLSListing", mo) for mo in months]
sold_files = [pick_file("CRMLSSold", mo) for mo in months]

listings = pd.concat([pd.read_csv(f, low_memory=False) for f in listing_files], ignore_index=True)
sold = pd.concat([pd.read_csv(f, low_memory=False) for f in sold_files], ignore_index=True)

print("Before Residential filter")
print("Listings rows:", len(listings))
print("Sold rows:", len(sold))

listings = listings[listings["PropertyType"] == "Residential"]
sold = sold[sold["PropertyType"] == "Residential"]

print("After Residential filter")
print("Listings rows:", len(listings))
print("Sold rows:", len(sold))

listings.to_csv("listings.csv", index=False)
sold.to_csv("sold.csv", index=False)

print("Done: saved listings.csv and sold.csv")
