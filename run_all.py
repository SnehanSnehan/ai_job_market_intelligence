# run_all.py
import subprocess
import os

# Ensure 'plots' folder exists
os.makedirs("plots", exist_ok=True)

scripts = [
    "src/clean_jobs.py",
    "src/clean_skills.py",
    "src/normalize_skills.py",
    "src/analyze_top_skills.py",
    "src/analyze_skills_by_role.py",
    "src/skill_gap_analyzer.py",
    "src/visualize_skills.py"
]

for script in scripts:
    print(f"\n--- Running {script} ---\n")
    subprocess.run(["python", script], check=True)
