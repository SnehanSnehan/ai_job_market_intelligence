# app.py
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import os
# 1. Load data
jobs_file = "data/job_postings_cleaned.csv"
top_skills_file = "data/top_skills_by_role.csv"

jobs_df = pd.read_csv(jobs_file)
role_skill_counts = pd.read_csv(top_skills_file)

# Ensure clean column names
jobs_df.columns = jobs_df.columns.str.strip()
role_skill_counts.columns = role_skill_counts.columns.str.strip()

# 2. Streamlit app layout
st.title("📊 AI Job Market Intelligence Dashboard")

# --- User Inputs ---
roles = role_skill_counts['job_title_clean'].unique().tolist()
selected_role = st.selectbox("Select your target role", options=roles)

skills_input = st.text_input(
    "Enter your skills (comma separated)", 
    placeholder="e.g., Python, SQL, Machine Learning"
)

candidate_skills = [s.strip().lower() for s in skills_input.split(",") if s.strip()]
st.markdown(f"**Candidate skills:** {candidate_skills}")
# 3. Filter top skills for selected role
role_skills = role_skill_counts[role_skill_counts['job_title_clean'] == selected_role]

# Sort by count descending
role_skills = role_skills.sort_values("count", ascending=False)

# Top 20 skills for visualization
top20 = role_skills.head(20)

st.markdown(f"🔥 Top Skills for {selected_role}")
st.dataframe(top20.reset_index(drop=True))

# 4. Generate recommendations dynamically
st.markdown("🎯 **Learning Recommendations**")

# Recommendation priority based on top 20
recommendations = []
for idx, row in top20.iterrows():
    skill = row['skill_normalized']
    if skill.lower() not in candidate_skills:
        priority = "High" if idx < 5 else "Medium" if idx < 10 else "Low"
        recommendations.append({
            "role": selected_role,
            "recommended_skill": skill,
            "priority": priority,
            "market_demand": row['count']
        })

if recommendations:
    rec_df = pd.DataFrame(recommendations)
    st.dataframe(rec_df)
else:
    st.write("You already have all top skills for this role! 🎉")

# 5. Visualization
st.markdown(f"📊 **Top Skills Visualization for {selected_role}**")

plt.figure(figsize=(10, 6))
sns.barplot(
    x="count",
    y="skill_normalized",
    data=top20,
    palette="magma",
    dodge=False
)
plt.title(f"Top 20 Skills for {selected_role}")
plt.xlabel("Job Postings Count")
plt.ylabel("Skill")
plt.tight_layout()
st.pyplot(plt.gcf())
plt.clf()
