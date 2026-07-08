# IDX Exchange Project

## Overview

This project is part of my Data Analyst Internship at IDX Exchange.

The objective is to build an end-to-end real estate analytics pipeline using California MLS residential property data. The project covers data extraction, aggregation, validation, exploratory data analysis (EDA), data cleaning, and mortgage rate enrichment to prepare analysis-ready datasets for Tableau dashboards and market intelligence.

---

## Project Objectives

- Extract monthly MLS Listing and Sold datasets
- Aggregate monthly datasets into master files
- Validate data quality
- Perform exploratory data analysis (EDA)
- Clean and standardize MLS data
- Enrich datasets with 30-Year Fixed Mortgage Rates from FRED
- Prepare clean datasets for Tableau dashboard development

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
| `week4_cleaning.py` | Data cleaning, validation flags, datatype conversion, geographic and timeline quality checks |
| `README.md` | Project documentation |

---

# Data Coverage

**January 2024 – June 2026**

Datasets included:

- MLS Listings
- MLS Sold Transactions

---

# Current Dataset Summary

## Listings

- Residential properties only
- **610,035 records**
- **84 columns**

## Sold

- Residential properties only
- **448,022 records**
- **84 columns**

---

# Project Workflow

## Week 0 — MLS Pipeline Orientation

- Download monthly MLS datasets
- Review Trestle Property Metadata
- Understand MLS extraction workflow

## Week 1 — Dataset Aggregation

- Combine monthly Listing datasets
- Combine monthly Sold datasets
- Filter Residential properties
- Export:
  - `listings.csv`
  - `sold.csv`

## Weeks 2–3 — Validation & Exploratory Data Analysis

Performed:

- Dataset structure validation
- Row and column verification
- Property type validation
- Missing value analysis
- High-null column identification
- Numeric distribution summaries
- Histograms
- Boxplots
- Percentile analysis
- Outlier inspection

Additional market analysis:

- Average vs. Median Close Price
- Days on Market distribution
- Homes sold above vs. below list price
- Date consistency validation
- County median price analysis

---

## Mortgage Rate Enrichment

Fetched the **30-Year Fixed Mortgage Rate (MORTGAGE30US)** from the Federal Reserve (FRED).

Workflow:

- Download weekly mortgage rates
- Convert weekly observations to monthly averages
- Create Year-Month keys
- Merge onto Listings and Sold datasets
- Validate merge completeness

Validation Results:

- Listings missing mortgage rates: **0**
- Sold missing mortgage rates: **0**

---

## Week 4 — Data Cleaning & Preparation

Implemented:

- Date column conversion to `datetime`
- Numeric datatype conversion
- Invalid value flagging
- Date consistency validation
- Geographic data quality validation
- Dataset quality summaries
- Export cleaned datasets

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

---

# Technologies

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Tableau Public

---

# Current Progress

✅ Week 0 Complete

✅ Week 1 Complete

✅ Weeks 2–3 Complete

✅ Mortgage Rate Enrichment Complete

✅ Week 4 Complete

Current MLS Coverage:

**202401 – 202606**

---

# Next Steps

- Week 5: Additional data preparation
- Week 6: Feature engineering
- Market metrics
- Tableau dashboard development
- Housing market analysis

---

# Notes

Large MLS datasets are maintained locally and are not uploaded to GitHub because of file size limitations.

This repository contains the complete Python workflow developed during the IDX Exchange Data Analyst Internship.
# Notes

Raw MLS datasets are stored locally and are not uploaded to GitHub.

This repository contains the Python workflow and project documentation developed throughout the internship.
