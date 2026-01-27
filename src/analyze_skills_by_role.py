import pandas as pd
import os
# Create plots folder if it doesn't exist
os.makedirs("plots", exist_ok=True)
# 1. Load cleaned jobs and normalized skills
jobs_df = pd.read_csv("data/job_postings_cleaned.csv")
skills_df = pd.read_csv("data/job_skills_normalized.csv")
# Strip whitespace from column names
jobs_df.columns = jobs_df.columns.str.strip()
skills_df.columns = skills_df.columns.str.strip()
# 2. Define main roles for analysis
MAIN_ROLES = [
    "data scientist",
    "machine learning engineer",
    "data engineer"
]
# Keep only jobs matching main roles (case-insensitive)
jobs_df["job_title_clean_lower"] = jobs_df["job_title_clean"].str.lower()
jobs_main = jobs_df[jobs_df["job_title_clean_lower"].isin(MAIN_ROLES)]
# 3. Merge skills with main jobs
# Strip any whitespace from column names
skills_df.columns = skills_df.columns.str.strip()
jobs_main.columns = jobs_main.columns.str.strip()
skills_main = pd.merge(
    skills_df,
    jobs_main,
    on="job_link",
    how="inner"
)

print("Merged rows:", len(skills_main))
print(skills_main[["job_title_clean", "skill_normalized"]].head(10))
# 4. Count top skills per role
role_skill_counts = (
    skills_main.groupby(["job_title_clean", "skill_normalized"])
    .size()
    .reset_index(name="count")
)

# Sort by job title and count
role_skill_counts = role_skill_counts.sort_values(
    ["job_title_clean", "count"], ascending=[True, False]
)
# 5. Save results
output_path = "data/top_skills_by_role.csv"
role_skill_counts.to_csv(output_path, index=False)

print(f"\nTop skills by role saved to: {output_path}")

# Preview top 10 skills per role
for role in MAIN_ROLES:
    print(f"\nTop skills for {role}:")
    top_skills = role_skill_counts[role_skill_counts["job_title_clean"] == role].head(10)
    print(top_skills[["skill_normalized", "count"]])
