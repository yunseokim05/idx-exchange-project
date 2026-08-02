# IDX Exchange MLS Analytics Project

## Overview

This project was completed as part of the IDX Exchange Data Analyst Internship Program.

The objective is to transform raw MLS transaction data into an analysis-ready housing market dataset through a structured data engineering and analytics pipeline. The workflow includes data aggregation, validation, exploratory analysis, mortgage rate enrichment, data cleaning, feature engineering, school district mapping, and outlier detection.

Dataset coverage:

- January 2024 – June 2026
- California Residential MLS Listings and Sold Transactions
- Mortgage rate enrichment from FRED (MORTGAGE30US)

---

## Project Pipeline

### Week 0 – MLS Data Pipeline Orientation

Reviewed the MLS extraction process and dataset structure.

Completed:

- Downloaded monthly MLS datasets from FTP
- Reviewed Trestle Property Metadata
- Verified extraction scripts:
  - `crmls_listed.py`
  - `crmls_sold.py`

Source files:

- `CRMLSListingYYYYMM.csv`
- `CRMLSSoldYYYYMM.csv`

Coverage:

- 202401 – 202606

---

### Week 1 – Monthly Dataset Aggregation

Script:

- `week1_aggregate.py`

Tasks completed:

- Loaded all monthly MLS files
- Concatenated monthly datasets
- Filtered PropertyType = Residential
- Generated combined datasets

Outputs:

- `listings.csv`
- `sold.csv`

Dataset counts:

| Dataset | Rows |
|----------|----------:|
| Listings (Residential) | 610,035 |
| Sold (Residential) | 448,022 |

Skills:

- Multi-file ingestion
- Dataset aggregation
- Residential filtering

---

### Week 2 – Dataset Validation

Script:

- `week2_validation.py`

Tasks completed:

- Dataset structure review
- Column data type inspection
- Property type validation
- Missing value analysis
- Missing percentage calculations
- 90%+ missing column identification
- Core numeric distribution summaries:
  - ClosePrice
  - LivingArea
  - DaysOnMarket

Outputs:

- `validated_listings.csv`
- `validated_sold.csv`
- `listings_missing_report.csv`
- `sold_missing_report.csv`

Skills:

- Data validation
- Missing value assessment
- Dataset profiling

---

### Week 3 – Exploratory Data Analysis (EDA)

Script:

- `week3_eda.py`

Tasks completed:

- Histograms
- Boxplots
- Percentile analysis
- Distribution analysis

Analyzed:

- ClosePrice
- ListPrice
- OriginalListPrice
- LivingArea
- LotSizeAcres
- BedroomsTotal
- BathroomsTotalInteger
- DaysOnMarket
- YearBuilt

Business questions answered:

- Residential property share
- Average and median close prices
- Days on Market distribution
- Above-list vs below-list sales
- Date consistency issues
- Highest median-price counties

Outputs:

- Histogram visualizations
- Boxplot visualizations

Skills:

- Exploratory data analysis
- Distribution analysis
- Outlier identification

---

### Week 3 – Mortgage Rate Enrichment

Script:

- `week3_mortgage_merge.py`

Tasks completed:

- Fetched FRED MORTGAGE30US series
- Converted weekly data to monthly averages
- Created Year-Month join keys
- Merged mortgage rates onto MLS datasets
- Validated merge completeness

Outputs:

- `listings_with_rates.csv`
- `sold_with_rates.csv`

Validation:

- Listings missing rates: 0
- Sold missing rates: 0

Skills:

- API data integration
- Time-series resampling
- External economic data enrichment

---

### Week 4–5 – Data Cleaning & Preparation

Script:

- `week4_cleaning.py`

Tasks completed:

- Datetime conversion
- Numeric field conversion
- Data quality validation
- Date consistency checks
- Geographic validation checks

Quality flags created:

- invalid_closeprice_flag
- invalid_livingarea_flag
- negative_dom_flag
- negative_bedrooms_flag
- negative_bathrooms_flag
- listing_after_close_flag
- purchase_after_close_flag
- negative_timeline_flag
- missing_coordinate_flag
- zero_coordinate_flag
- positive_longitude_flag
- out_of_state_coordinate_flag

Outputs:

- `cleaned_listings.csv`
- `cleaned_sold.csv`

Skills:

- Data cleaning
- Quality assurance
- Geographic validation

---

### Week 6 – Feature Engineering

Script:

- `week6_feature_engineering.py`

Engineered metrics:

- PriceRatio
- CloseToOriginalListRatio
- PricePerSqFt
- DaysOnMarketMetric
- Year
- Month
- YrMo
- ListingToContractDays
- ContractToCloseDays

Segment analysis:

- County-level market summary

Outputs:

- `featured_listings.csv`
- `featured_sold.csv`
- `county_market_summary.csv`

Skills:

- Feature engineering
- Housing market analytics
- Time-series metric creation

---

### Week 6 – School District Mapping

Script:

- `week6_school_district_mapping.py`

Tasks completed:

- Downloaded California School District boundaries
- Filtered Unified School Districts
- Converted polygons to EPSG:4326
- Performed spatial joins using Latitude and Longitude
- Added school district information to MLS records

Results:

| Dataset | Match Rate |
|----------|----------:|
| Listings | 66.80% |
| Sold | 73.19% |

Outputs:

- `featured_listings_with_districts.csv`
- `featured_sold_with_districts.csv`

Skills:

- GeoPandas
- Spatial joins
- Geospatial analytics

---

### Week 7 – Outlier Detection & Data Quality

Script:

- `week7_outlier_detection.py`

Method:

- Interquartile Range (IQR)

Fields analyzed:

- ClosePrice
- LivingArea
- DaysOnMarket

Generated:

- Individual outlier flags
- Business-rule validation flags
- Overall outlier indicators

Listings:

- Rows before filtering: 610,035
- Rows after filtering: 523,436
- Rows removed: 86,599

Sold:

- Rows before filtering: 448,022
- Rows after filtering: 377,495
- Rows removed: 70,527

Outputs:

- `flagged_listings.csv`
- `flagged_sold.csv`
- `filtered_listings.csv`
- `filtered_sold.csv`

Skills:

- IQR-based outlier detection
- Statistical data quality analysis
- Flagged vs filtered dataset design

---

## Current Project Status

Completed:

- Week 0
- Week 1
- Week 2
- Week 3 EDA
- Week 3 Mortgage Rate Enrichment
- Week 4–5 Cleaning
- Week 6 Feature Engineering
- Week 6 School District Mapping
- Week 7 Outlier Detection

Next Phase:

- Weeks 8–10 Tableau Dashboard Development
- Weeks 11–12 Market Intelligence Report and Presentation

---

## Technologies Used

- Python
- Pandas
- NumPy
- GeoPandas
- Matplotlib
- FRED Economic Data
- Git / GitHub
- Tableau Public (upcoming)

---

# Notes

Raw MLS datasets are stored locally and are not uploaded to GitHub.

This repository contains the Python workflow and project documentation developed throughout the internship.
