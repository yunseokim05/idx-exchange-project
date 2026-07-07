# IDX Exchange Project

## Overview

This project analyzes California MLS residential real estate data using Python and Tableau.

The project builds an end-to-end workflow that includes:

- Monthly MLS data extraction
- Dataset aggregation
- Data validation
- Exploratory Data Analysis (EDA)
- Mortgage rate enrichment using FRED
- Dashboard preparation for Tableau

---

## Objectives

- Extract monthly MLS Listing and Sold datasets
- Aggregate all monthly datasets into master files
- Filter Residential properties only
- Validate dataset quality
- Perform exploratory data analysis
- Merge external mortgage rate data
- Prepare datasets for Tableau dashboards

---

## Project Structure

| File | Description |
|------|-------------|
| crmls_listed.py | Download monthly Listing datasets |
| crmls_sold.py | Download monthly Sold datasets |
| week1_aggregate.py | Merge monthly CSV files and filter Residential properties |
| week2_validation.py | Dataset validation and missing value analysis |
| week3_eda.py | Exploratory Data Analysis |
| week3_mortgage_merge.py | Merge monthly mortgage rates from FRED |
| README.md | Project documentation |

---

## Data Coverage

Current MLS coverage:

**January 2024 – June 2026**

Datasets included:

- Listings
- Sold Transactions

---

## Current Dataset Summary

### Listings

- Residential properties only
- **610,035 records**
- **84 columns**

### Sold

- Residential properties only
- **448,022 records**
- **84 columns**

---

## Workflow

### Week 0

- Download monthly MLS files
- Understand MLS metadata
- Review extraction scripts

### Week 1

- Combine all monthly CSV files
- Filter Residential properties
- Export

```
listings.csv
sold.csv
```

### Week 2

- Dataset validation
- Property type verification
- Missing value analysis
- Null percentage review

### Week 3

- Exploratory Data Analysis
- Distribution analysis
- Outlier inspection
- Market summary statistics
- Mortgage rate enrichment (FRED)

---

## Week 3 Analysis

EDA includes:

- ClosePrice
- ListPrice
- OriginalListPrice
- LivingArea
- LotSizeAcres
- BedroomsTotal
- BathroomsTotalInteger
- DaysOnMarket
- YearBuilt

Generated:

- Summary statistics
- Missing value counts
- Percentiles
- Histograms
- Boxplots

Additional market analysis:

- Average vs Median Close Price
- Days on Market distribution
- Sold Above / Below List %
- Date consistency validation
- Top counties by median Close Price

---

## Mortgage Rate Enrichment

Source:

Federal Reserve Economic Data (FRED)

Series:

MORTGAGE30US

Workflow:

- Download weekly mortgage rates
- Convert to monthly averages
- Merge with Listings dataset
- Merge with Sold dataset
- Validate merge completeness

Missing mortgage rates:

- Listings: **0**
- Sold: **0**

---

## Current Progress

✅ Week 0 Complete

✅ Week 1 Complete

✅ Week 2 Complete

✅ Week 3 Complete

Current coverage:

**202401 – 202606**

---

## Next Steps

- Feature engineering
- Data cleaning
- Tableau dashboards
- Predictive modeling
- Market trend analysis

# Notes

Raw MLS datasets are stored locally and are not uploaded to GitHub.

This repository contains the Python workflow and project documentation developed throughout the internship.
