# AnalystLab Africa – Data Cleaning & EDA Project

## Overview
This project was completed as part of the **AnalystLab Africa Data Analytics Internship (Batch B)**. It covers data cleaning and exploratory data analysis (EDA) on two real-world datasets using Python and pandas.

## Datasets
- **OnlineRetail.csv** – E-commerce transaction data (Kaggle)
- **netflix_titles.csv** – Netflix content catalog (Kaggle)

## Tools Used
- Python
- pandas
- VS Code

## What This Project Covers
1. **Initial Data Inspection** – shape, structure, data types, and null value overview
2. **Handling Missing Values** – identified nulls in `CustomerID` and `Description`, filled or dropped based on context
3. **Removing Duplicates** – detected and removed duplicate transaction records
4. **Standardizing Data** – fixed inconsistent text casing (e.g., `Country`, `Description`), standardized column names
5. **Data Type Conversion** – converted `InvoiceDate` to proper datetime format
6. **Feature Engineering** – created `Revenue` (Quantity × UnitPrice) and extracted `Month` from invoice dates
7. **Exploratory Data Analysis** – analyzed revenue by country, revenue by month, top customers by spend, and product-level summary statistics

## Key Steps in Code
See [`data_cleaning.py`](./data_cleaning.py) for the full cleaning and analysis workflow, including inline print statements documenting each transformation.

## Author
**Maryam Malik (Maryani)** — Data Annotator & Analytics Trainee
[LinkedIn Profile] | [experts.opentrain.ai/maryani-m]
