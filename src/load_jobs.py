# load_jobs.py
import pandas as pd

# Step 1: Load the main job postings CSV
file_path = "data/job_postings.csv"
df = pd.read_csv(file_path)

# Step 2: Preview the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: See the columns
print("\nColumns in the dataset:")
print(df.columns)

# Step 4: Total number of job postings
print("\nTotal number of job postings:", len(df))
