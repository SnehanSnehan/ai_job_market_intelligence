
# This script analyzes the skill gap for a candidate
# based on their skills and a desired AI/ML role.


import pandas as pd

# 1. Load top skills by role CSV

top_skills_df = pd.read_csv("data/top_skills_by_role.csv")

print("Columns in top skills CSV:", top_skills_df.columns.tolist())
print("Sample top skills:")
print(top_skills_df.head())

# 2. Get user input
candidate_input = input("\nEnter your skills, separated by commas: ")
candidate_skills = [s.strip().lower() for s in candidate_input.split(",") if s.strip()]
print("Candidate skills:", candidate_skills)

desired_role = input("Enter your desired role (e.g., data scientist): ").strip().lower()
print("Desired role:", desired_role)

# 3. Extract top skills for the desired role
# Limit to top 20 skills for clarity

role_skills = (
    top_skills_df[top_skills_df["job_title_clean"].str.lower() == desired_role]
    .sort_values("count", ascending=False)
    .head(20)["skill_normalized"]
    .str.lower()
    .tolist()
)

if not role_skills:
    print(f"\nNo skills found for role '{desired_role}'. Please check role spelling.")
    exit()

print("\nTop skills for role (limited to top 20):", role_skills)


# 4. Compare candidate skills with role skills

matched_skills = [s for s in candidate_skills if s in role_skills]
missing_skills = [s for s in role_skills if s not in candidate_skills]

skill_gap_percent = round((len(missing_skills) / len(role_skills)) * 100, 2)


# 5. Print results

print("\nMatched skills:", matched_skills)
print("Missing skills:", missing_skills)
print(f"Skill gap: {skill_gap_percent}%")
