import pandas as pd

# 1. Load cleaned skills data
skills_df = pd.read_csv("data/job_skills_cleaned.csv")

print("Initial rows:", len(skills_df))
print(skills_df.head())


# 2. Define canonical skill mapping

SKILL_MAP = {
    "python": ["python", "python programming"],
    "sql": ["sql", "postgres", "mysql", "sqlite"],
    "machine learning": ["machine learning", "ml", "ml algorithms"],
    "deep learning": ["deep learning", "neural networks"],
    "pytorch": ["pytorch", "torch"],
    "tensorflow": ["tensorflow", "keras"],
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": ["gcp", "google cloud"],
    "docker": ["docker", "containerization"],
    "kubernetes": ["kubernetes", "k8s"],
    "spark": ["spark", "apache spark"],
    "nlp": ["nlp", "natural language processing"],
    "computer vision": ["computer vision", "cv"],
    "data engineering": ["data engineering", "data pipelines", "etl"],
    "statistics": ["statistics", "statistical modeling"],
}

# 3. Normalize skill names
def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()

    for canonical, variants in SKILL_MAP.items():
        for v in variants:
            if v in skill:
                return canonical

    return skill  # keep original if no match


skills_df["skill_normalized"] = skills_df["skill"].apply(normalize_skill)

print("\nAfter normalization:")
print(skills_df[["skill", "skill_normalized"]].head(15))

# 4. Save normalized skills

output_path = "data/job_skills_normalized.csv"
skills_df.to_csv(output_path, index=False)

print(f"\nNormalized skills saved to: {output_path}")
print("Total rows:", len(skills_df))
print("Unique normalized skills:", skills_df["skill_normalized"].nunique())
