# clean_skills.py
# This script loads and inspects job skills data

import pandas as pd

# Load the job skills CSV
skills_df = pd.read_csv("data/job_skills.csv")

# Basic information about the dataset
print("Dataset shape:")
print(skills_df.shape)

print("\nColumns in job_skills.csv:")
print(skills_df.columns)

# Preview first 10 rows
print("\nSample rows:")
print(skills_df.head(10))

# Check for missing values
print("\nMissing values per column:")
print(skills_df.isnull().sum())

# ---------------------------------------------------
# Clean and normalize skills
# ---------------------------------------------------

# Drop rows where job_skills is missing
skills_df = skills_df.dropna(subset=["job_skills"])

def clean_skill_list(skill_text):
    """
    Takes a comma-separated skill string and returns
    a cleaned list of individual skills.
    """
    skills = skill_text.split(",")

    cleaned_skills = []
    for skill in skills:
        skill = skill.strip().lower()
        if skill:
            cleaned_skills.append(skill)

    return cleaned_skills

# Apply cleaning function
skills_df["skills_cleaned"] = skills_df["job_skills"].apply(clean_skill_list)

# Explode skills into one skill per row
skills_exploded = skills_df[["job_link", "skills_cleaned"]].explode("skills_cleaned")

# Rename column for clarity
skills_exploded = skills_exploded.rename(columns={"skills_cleaned": "skill"})

print("\nSample cleaned and exploded skills:")
print(skills_exploded.head(10))

print("\nTotal unique skills:")
print(skills_exploded["skill"].nunique())


# ---------------------------------------------------
# Save cleaned skills data
# ---------------------------------------------------

output_path = "data/job_skills_cleaned.csv"
skills_exploded.to_csv(output_path, index=False)

print(f"\nCleaned skills data saved to: {output_path}")
print(f"Total rows (job-skill pairs): {len(skills_exploded)}")
