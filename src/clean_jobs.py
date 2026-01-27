
# This script loads job data from SQLite and performs basic cleaning

import pandas as pd
from sqlalchemy import create_engine

# Connect to the SQLite database
engine = create_engine("sqlite:///data/job_postings.db")

# Load data from the job_postings table
query = "SELECT * FROM job_postings"
df = pd.read_sql(query, engine)

# Show basic information before cleaning
print("Initial dataset shape:")
print(df.shape)

print("\nColumns available:")
print(df.columns)

# Keep only columns relevant for analysis
columns_to_keep = [
    "job_link",         
    "job_title",
    "company",
    "job_location",
    "job_level",
    "job_type"
]


df_clean = df[columns_to_keep]

# Remove rows with missing job titles
df_clean = df_clean.dropna(subset=["job_title"])

# Strip extra spaces from text columns
for col in df_clean.columns:
    df_clean[col] = df_clean[col].astype(str).str.strip()

# Show result after cleaning
print("\nDataset shape after cleaning:")
print(df_clean.shape)

print("\nSample cleaned data:")
print(df_clean.head())

# Standardize job titles for analysis
def clean_job_title(title):
    """
    Cleans and standardizes a job title string.
    """
    title = title.lower()
    title = title.replace(",", " ")
    title = title.replace("/", " ")
    title = title.replace("-", " ")
    title = " ".join(title.split())

    # Standardize seniority terms
    title = title.replace("sr ", "senior ")
    title = title.replace("jr ", "junior ")

    return title


# Apply cleaning function
df_clean["job_title_clean"] = df_clean["job_title"].apply(clean_job_title)

print("\nCleaned job titles (sample):")
print(df_clean[["job_title", "job_title_clean"]].head())
# Save cleaned job data for later phases

output_path = "data/job_postings_cleaned.csv"
df_clean.to_csv(output_path, index=False)

print(f"\nCleaned job data saved to: {output_path}")
