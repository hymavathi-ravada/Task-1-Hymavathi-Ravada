# ==========================================
# DATA CLEANING & PREPARATION PROJECT
# ==========================================

# Import libraries
import pandas as pd
import numpy as np

# ==========================================
# STEP 1 - LOAD DATASET
# ==========================================

print("Loading dataset...")

file_path = "../data/sales_data.xlsx"

df = pd.read_excel(file_path)

print("Dataset Loaded Successfully!")
print()

# ==========================================
# STEP 2 - BASIC DATA EXPLORATION
# ==========================================

print("FIRST 5 RECORDS")
print(df.head())
print()

print("DATASET SHAPE")
print(df.shape)
print()

print("COLUMN NAMES")
print(df.columns)
print()

print("DATA TYPES")
print(df.dtypes)
print()

# ==========================================
# STEP 3 - CHECK MISSING VALUES
# ==========================================

print("MISSING VALUES")
print(df.isnull().sum())
print()

# ==========================================
# ==========================================
# STEP 4 - HANDLE MISSING VALUES
# ==========================================

# Fill missing numeric values with median
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing text values
text_columns = df.select_dtypes(include=['object', 'string']).columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# Special handling for CouponCode column
if 'CouponCode' in df.columns:
    df['CouponCode'] = df['CouponCode'].fillna("No Coupon")

print("Missing values handled successfully!")
print()

# ==========================================
# STEP 5 - REMOVE DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print(f"Duplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

print("Duplicates removed successfully!")
print()

# ==========================================
# STEP 6 - STANDARDIZE COLUMN NAMES
# ==========================================

df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

print("Column names standardized!")
print()

# ==========================================
# STEP 7 - CLEAN TEXT DATA
# ==========================================

text_columns = df.select_dtypes(include='object').columns

for column in text_columns:
    df[column] = df[column].str.strip()
    df[column] = df[column].str.title()

print("Text formatting cleaned!")
print()

# ==========================================
# STEP 8 - DATE FORMAT CORRECTION
# ==========================================

# Example date column
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

print("Date formatting corrected!")
print()

# ==========================================
# STEP 9 - REMOVE NEGATIVE VALUES
# ==========================================

numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df = df[df[column] >= 0]

print("Negative values removed!")
print()

# ==========================================
# STEP 10 - CHECK OUTLIERS
# ==========================================

print("NUMERICAL SUMMARY")
print(df.describe())
print()

# ==========================================
# STEP 11 - FINAL DATASET CHECK
# ==========================================

print("FINAL DATASET INFO")
print(df.info())
print()

print("FINAL SHAPE")
print(df.shape)
print()

# ==========================================
# STEP 12 - SAVE CLEANED DATASET
# ==========================================

output_path = "../output/cleaned_dataset.xlsx"

df.to_excel(output_path, index=False)

print("===================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("Cleaned dataset saved!")
print("===================================")