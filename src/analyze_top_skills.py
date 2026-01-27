import pandas as pd

# -------------------------------------------------
# 1. Load normalized skills
# -------------------------------------------------
skills_df = pd.read_csv("data/job_skills_normalized.csv")

print("Total job-skill rows:", len(skills_df))
print(skills_df.head())


# -------------------------------------------------
# 2. Count skill frequency
# -------------------------------------------------
skill_counts = (
    skills_df["skill_normalized"]
    .value_counts()
    .reset_index()
)

skill_counts.columns = ["skill", "count"]

print("\nTop 20 skills in AI jobs:")
print(skill_counts.head(20))


# -------------------------------------------------
# 3. Save results
# -------------------------------------------------
output_path = "data/top_skills_overall.csv"
skill_counts.to_csv(output_path, index=False)

print(f"\nTop skills saved to: {output_path}")
