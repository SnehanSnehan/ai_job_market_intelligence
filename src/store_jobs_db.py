
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Load CSV
df = pd.read_csv("data/job_postings.csv")

# Step 2: Create SQLite engine
engine = create_engine("sqlite:///data/job_postings.db")  # creates job_postings.db in data/

# Step 3: Store CSV into SQLite
df.to_sql("job_postings", engine, if_exists="replace", index=False)

print("Data successfully stored in SQLite database: data/job_postings.db")
