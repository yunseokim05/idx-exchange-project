# IDX Exchange Project

## Overview

This project is part of my Data Analyst Internship at IDX Exchange.

The objective is to build an end-to-end real estate analytics pipeline using California MLS residential property data. The project covers data extraction, aggregation, validation, exploratory data analysis (EDA), mortgage rate enrichment, and data cleaning to prepare analysis-ready datasets for Tableau dashboards and market intelligence.

---

## Project Objectives

- Extract monthly MLS Listing and Sold datasets
- Aggregate monthly datasets into master files
- Filter Residential properties only
- Validate dataset quality
- Perform exploratory data analysis (EDA)
- Enrich datasets with 30-Year Fixed Mortgage Rates from FRED
- Clean and standardize MLS data
- Prepare analysis-ready datasets for feature engineering and Tableau dashboard development

---

## Repository Structure

| File | Description |
|------|-------------|
| `crmls_listed.py` | Download monthly MLS Listing datasets |
| `crmls_sold.py` | Download monthly MLS Sold datasets |
| `week1_aggregate.py` | Combine monthly CSV files and filter Residential properties |
| `week2_validation.py` | Dataset validation and missing value analysis |
| `week3_eda.py` | Exploratory Data Analysis (EDA) |
| `week3_mortgage_merge.py` | Merge monthly mortgage rates from FRED |
| `week4_cleaning.py` | Weeks 4–5 data cleaning, datatype conversion, validation flags, and geographic and timeline quality checks |
| `README.md` | Project documentation |

---

## Data Coverage

**January 2024 – June 2026**

Datasets included:

- MLS Listings
- MLS Sold Transactions

---

## Current Dataset Summary

### Listings

- Residential properties only
- **610,035 records**
- **84 original columns**

### Sold

- Residential properties only
- **448,022 records**
- **84 original columns**

Additional validation flag columns are added during the Weeks 4–5 cleaning process.

---

## Project Workflow

### Week 0 — MLS Pipeline Orientation

- Download monthly MLS datasets
- Review Trestle Property Metadata
- Understand API authentication and pagination
- Review monthly extraction workflow
- Confirm monthly Listing and Sold files are available

### Week 1 — Dataset Aggregation

- Combine monthly Listing datasets from January 2024 through June 2026
- Combine monthly Sold datasets from January 2024 through June 2026
- Filter both datasets to `PropertyType == "Residential"`
- Confirm row counts before and after filtering
- Export:
  - `listings.csv`
  - `sold.csv`

### Weeks 2–3 — Validation and Exploratory Data Analysis

Performed:

- Dataset structure validation
- Row and column verification
- Property type validation
- Missing value analysis
- High-null column identification
- Numeric datatype review
- Numeric distribution summaries
- Percentile analysis
- Histograms
- Boxplots
- Extreme outlier inspection

Numeric fields analyzed:

- `ClosePrice`
- `ListPrice`
- `OriginalListPrice`
- `LivingArea`
- `LotSizeAcres`
- `BedroomsTotal`
- `BathroomsTotalInteger`
- `DaysOnMarket`
- `YearBuilt`

Additional market analysis:

- Average vs. median Close Price
- Days on Market distribution
- Homes sold above, below, or at list price
- Date consistency validation
- Top counties by median Close Price

---

## Mortgage Rate Enrichment

Fetched the **30-Year Fixed Mortgage Rate (`MORTGAGE30US`)** from Federal Reserve Economic Data (FRED).

Workflow:

- Download weekly mortgage rate observations
- Convert weekly observations to monthly averages
- Create Year-Month join keys
- Merge rates onto the Listings dataset using `ListingContractDate`
- Merge rates onto the Sold dataset using `CloseDate`
- Validate merge completeness
- Export:
  - `listings_with_rates.csv`
  - `sold_with_rates.csv`

Validation results:

- Listings missing mortgage rates: **0**
- Sold missing mortgage rates: **0**

---

## Weeks 4–5 — Data Cleaning and Preparation

Implemented:

- Converted date fields to `datetime`
- Converted key numeric fields to numeric datatypes
- Preserved original records while adding data-quality flags
- Validated transaction timeline consistency
- Validated geographic coordinate quality
- Confirmed key datatypes after conversion
- Printed before and after row counts
- Generated data-quality summaries
- Exported cleaned, analysis-ready datasets

Date fields standardized:

- `CloseDate`
- `PurchaseContractDate`
- `ListingContractDate`
- `ContractStatusChangeDate`

Numeric fields standardized:

- `ClosePrice`
- `ListPrice`
- `OriginalListPrice`
- `LivingArea`
- `LotSizeAcres`
- `BedroomsTotal`
- `BathroomsTotalInteger`
- `DaysOnMarket`
- `Latitude`
- `Longitude`

Generated validation flags:

- `invalid_closeprice_flag`
- `invalid_livingarea_flag`
- `negative_dom_flag`
- `negative_bedrooms_flag`
- `negative_bathrooms_flag`
- `listing_after_close_flag`
- `purchase_after_close_flag`
- `negative_timeline_flag`
- `missing_coordinate_flag`
- `zero_coordinate_flag`
- `positive_longitude_flag`
- `out_of_state_coordinate_flag`

Outputs:

- `cleaned_listings.csv`
- `cleaned_sold.csv`

Weeks 4–5 row counts:

### Cleaned Listings

- Before cleaning: **610,035**
- After cleaning: **610,035**

### Cleaned Sold

- Before cleaning: **448,022**
- After cleaning: **448,022**

No rows were permanently removed during this phase. Data-quality issues were preserved through validation flags for transparency and later review.

---

## Technologies

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Tableau Public

---

## Current Progress

- ✅ Week 0 Complete
- ✅ Week 1 Complete
- ✅ Weeks 2–3 Complete
- ✅ Mortgage Rate Enrichment Complete
- ✅ Weeks 4–5 Complete

Current MLS coverage:

**202401 – 202606**

---

## Next Steps

- Week 6: Feature engineering and market metrics
- Create price ratio and price-per-square-foot metrics
- Create Year, Month, and Year-Month fields
- Calculate listing-to-contract and contract-to-close durations
- Produce segmented market summary tables
- Prepare analysis-ready datasets for Tableau dashboard development

---


# Notes

Raw MLS datasets are stored locally and are not uploaded to GitHub.

This repository contains the Python workflow and project documentation developed throughout the internship.
