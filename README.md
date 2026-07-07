# IDX Exchange Project

## Overview

This project is part of my Data Analyst Internship at IDX Exchange.

The objective is to build an end-to-end real estate analytics workflow using Python and Tableau by collecting, cleaning, validating, and analyzing MLS listing and sold property datasets.

---

# Project Objectives

- Extract monthly MLS Listing and Sold datasets
- Maintain updated master datasets (202401–202605)
- Validate and clean data quality
- Perform exploratory data analysis (EDA)
- Merge external mortgage rate data (FRED)
- Build Tableau dashboards for housing market analysis

---

# Repository Structure

| File | Description |
|------|-------------|
| `crmls_listed.py` | Download monthly Listing datasets |
| `crmls_sold.py` | Download monthly Sold datasets |
| `week1_aggregate.py` | Aggregate monthly CSV files and filter Residential properties |
| `week2_validation.py` | Validate dataset structure and missing values |
| `week3_eda.py` | Exploratory Data Analysis with descriptive statistics and visualizations |
| `week3_mortgage_merge.py` | Merge monthly mortgage rates from FRED |
| `README.md` | Project documentation |

---

# Workflow

### Week 0
- Download monthly MLS datasets
- Maintain historical data archive

### Week 1
- Aggregate monthly Listing and Sold files
- Filter Residential properties
- Generate master datasets:
  - `listings.csv`
  - `sold.csv`

### Week 2
- Validate datasets
- Check:
  - Row counts
  - Column counts
  - PropertyType distribution
  - Missing values

### Week 3
- Exploratory Data Analysis
- Summary statistics
- Median / Mean
- Missing value analysis
- Histograms
- Boxplots
- Outlier detection
- Property type distribution
- County median price analysis
- Above / Below list price analysis
- Date consistency check

### Mortgage Integration
- Download 30-Year Fixed Mortgage Rate data from FRED
- Convert weekly data to monthly averages
- Merge mortgage rates into MLS datasets

---

# Current Dataset

### Listings

- Residential properties only
- **585,954 records**
- **84 columns**

### Sold

- Residential properties only
- **430,481 records**
- **84 columns**

Coverage:

- January 2024
- through
- May 2026

---

# Technologies

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- Tableau Public

---

# Progress

## ✅ Completed

- Historical MLS extraction (202401–202605)
- Listing aggregation
- Sold aggregation
- Residential filtering
- Data validation
- Missing value analysis
- Exploratory Data Analysis
- Mortgage rate integration
- GitHub project organization

---

# Future Work

- Feature engineering
- Tableau dashboards
- Housing market trend analysis
- Predictive modeling
- Weekly automated data refresh

---

# Notes

Raw MLS datasets are stored locally and are not uploaded to GitHub.

This repository contains the Python workflow and project documentation developed throughout the internship.
