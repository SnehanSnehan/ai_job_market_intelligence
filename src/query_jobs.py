# query_jobs.py
from sqlalchemy import create_engine
import pandas as pd

# Step 1: Connect to SQLite database
engine = create_engine("sqlite:///data/job_postings.db")

# Step 2: Example SQL queries
# Query 1: Total number of job postings
total_jobs = pd.read_sql("SELECT COUNT(*) AS total FROM job_postings", engine)
print("Total job postings:")
print(total_jobs)

# Query 2: Top 10 job titles
top_titles = pd.read_sql(
    "SELECT job_title, COUNT(*) AS count FROM job_postings GROUP BY job_title ORDER BY count DESC LIMIT 10",
    engine
)
print("\nTop 10 job titles:")
print(top_titles)

# Query 3: Jobs by location (top 10)
top_locations = pd.read_sql(
    "SELECT job_location, COUNT(*) AS count FROM job_postings GROUP BY job_location ORDER BY count DESC LIMIT 10",
    engine
)
print("\nTop 10 job locations:")
print(top_locations)
