# visualize_skills.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# -------------------------------------------------
# 1. Load top skills data
# -------------------------------------------------
top_skills_file = "data/top_skills_by_role.csv"
if not os.path.exists(top_skills_file):
    raise FileNotFoundError(f"{top_skills_file} not found. Run analysis scripts first.")

role_skill_counts = pd.read_csv(top_skills_file)

# Normalize column names
role_skill_counts.columns = role_skill_counts.columns.str.strip()

# -------------------------------------------------
# 2. Get user input
# -------------------------------------------------
candidate_skills_input = input("Enter your skills, separated by commas (optional, press Enter to skip): ").strip()
candidate_skills = [s.strip().lower() for s in candidate_skills_input.split(",") if s.strip()]
print("Candidate skills:", candidate_skills)

role_input = input("Enter your desired role (e.g., data scientist): ").strip().lower()

# -------------------------------------------------
# 3. Normalize role input
# -------------------------------------------------
role_mapping = {
    "ml engineer": "machine learning engineer",
    "machine learning engineer": "machine learning engineer",
    "ai engineer": "ai engineer",
    "data scientist": "data scientist",
    "data engineer": "data engineer"
}

role_input = role_mapping.get(role_input, role_input)  # map common variations

# -------------------------------------------------
# 4. Filter top skills for the role
# -------------------------------------------------
subset = role_skill_counts[
    role_skill_counts["job_title_clean"].str.lower() == role_input
].copy()

if subset.empty:
    print(f"No data found for role '{role_input}'. Showing top 20 skills across all AI jobs instead.")
    # fallback to top 20 overall
    top20 = role_skill_counts.groupby("skill_normalized").sum().reset_index().sort_values("count", ascending=False).head(20)
    subset = top20.rename(columns={"skill_normalized": "skill_normalized", "count": "count"})
else:
    # Limit to top 20 skills for clarity
    subset = subset.sort_values("count", ascending=False).head(20)

# -------------------------------------------------
# 5. Compare candidate skills
# -------------------------------------------------
role_top_skills = [s.lower() for s in subset["skill_normalized"].tolist()]

matched_skills = [s for s in candidate_skills if s in role_top_skills]
missing_skills = [s for s in role_top_skills if s not in candidate_skills]

if candidate_skills:
    print(f"Matched skills in top 20 for {role_input}: {matched_skills}")
    print(f"Missing skills in top 20 for {role_input}: {missing_skills}")

# -------------------------------------------------
# 6. Visualization
# -------------------------------------------------
sns.set_style("whitegrid")
plt.figure(figsize=(10, 8))
sns.barplot(x="count", y="skill_normalized", data=subset, palette="magma", dodge=False)
plt.title(f"Top skills for {role_input.capitalize()}")
plt.xlabel("Number of Job Postings")
plt.ylabel("Skill")

plt.tight_layout()
plt.show()

# -------------------------------------------------
# 7. Optionally save the plot
# -------------------------------------------------
save_plot = input("Do you want to save the plot as an image? (yes/no): ").strip().lower()
if save_plot == "yes":
    plots_dir = "plots"
    os.makedirs(plots_dir, exist_ok=True)
    plot_file = os.path.join(plots_dir, f"top_skills_{role_input.replace(' ', '_')}.png")
    plt.savefig(plot_file)
    print(f"Plot saved as {plot_file}")
else:
    print("Plot not saved.")
