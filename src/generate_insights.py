import pandas as pd
from pathlib import Path

# Paths
DATA_DIR = Path("data")
INSIGHTS_DIR = Path("insights")
INSIGHTS_DIR.mkdir(exist_ok=True)

# Load datasets
top_overall = pd.read_csv(DATA_DIR / "top_skills_overall.csv")
top_by_role = pd.read_csv(DATA_DIR / "top_skills_by_role.csv")

insights = []
# Overall Market Insights
insights.append("=== OVERALL AI JOB MARKET INSIGHTS ===\n")

top_10_overall = top_overall.head(10)

insights.append("Top 10 most in-demand skills across AI jobs:\n")
for _, row in top_10_overall.iterrows():
    insights.append(f"- {row['skill']} ({row['count']} postings)\n")

insights.append(
    "\nInsight: Core programming (Python, SQL) and cloud platforms "
    "(AWS, Azure) dominate AI job requirements, indicating strong demand "
    "for production-ready AI professionals.\n\n"
)
# Role-wise Insights
insights.append("=== ROLE-WISE SKILL INSIGHTS ===\n")

roles = top_by_role["job_title_clean"].unique()

for role in roles:
    insights.append(f"\nRole: {role.title()}\n")
    role_skills = top_by_role[top_by_role["job_title_clean"] == role].head(5)

    for _, row in role_skills.iterrows():
        insights.append(f"- {row['skill_normalized']} ({row['count']})\n")

    insights.append(
        "Insight: This role emphasizes both technical depth and domain-specific tools.\n"
    )

# Learning & Career Insights
insights.append("\n=== CAREER & LEARNING INSIGHTS ===\n")

insights.append(
    "- Candidates lacking cloud or big data skills face significant skill gaps.\n"
    "- Learning paths should combine ML fundamentals with engineering tools.\n"
    "- Skill overlap across roles suggests flexibility in transitioning between AI roles.\n"
)

# Save insights
output_file = INSIGHTS_DIR / "market_insights.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(insights)

print(f"Insights generated and saved to: {output_file}")
