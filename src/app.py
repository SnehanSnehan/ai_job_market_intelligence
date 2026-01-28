
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="AI Job Market Intelligence",
    page_icon="📊",
    layout="wide"
)


# 1. Load data
jobs_file = "data/job_postings_cleaned.csv"
top_skills_file = "data/top_skills_by_role.csv"

jobs_df = pd.read_csv(jobs_file)
role_skill_counts = pd.read_csv(top_skills_file)

jobs_df.columns = jobs_df.columns.str.strip()
role_skill_counts.columns = role_skill_counts.columns.str.strip()

# 2. Header
st.title("📊 AI Job Market Intelligence Dashboard")
st.markdown(
    "Analyze real job postings to understand **in-demand skills**, "
    "**market trends**, and **personalized learning paths**."
)
st.markdown("---")

# 3. User Inputs (clean layout)
input_col1, input_col2 = st.columns([1, 2])

with input_col1:
    roles = role_skill_counts['job_title_clean'].unique().tolist()
    selected_role = st.selectbox("🎯 Select your target role", options=roles)

with input_col2:
    skills_input = st.text_input(
        "🧠 Enter your skills (comma separated)",
        placeholder="e.g., Python, SQL, Machine Learning"
    )

candidate_skills = [s.strip().lower() for s in skills_input.split(",") if s.strip()]

st.markdown(
    f"**Candidate skills:** "
    f"`{', '.join(candidate_skills) if candidate_skills else 'None entered'}`"
)

st.markdown("---")

# 4. Top skills table
role_skills = role_skill_counts[
    role_skill_counts['job_title_clean'] == selected_role
].sort_values("count", ascending=False)

top20 = role_skills.head(20)

st.subheader(f"🔥 Top Skills for {selected_role}")
st.dataframe(
    top20.reset_index(drop=True),
    use_container_width=True
)

st.markdown("---")

# 5. Learning recommendations
st.subheader("🎯 Learning Recommendations")

recommendations = []
for idx, row in top20.iterrows():
    skill = row['skill_normalized']
    if skill.lower() not in candidate_skills:
        priority = "High" if idx < 5 else "Medium" if idx < 10 else "Low"
        recommendations.append({
            "Role": selected_role,
            "Recommended Skill": skill,
            "Priority": priority,
            "Market Demand": row['count']
        })

if recommendations:
    rec_df = pd.DataFrame(recommendations)
    st.dataframe(rec_df, use_container_width=True)
else:
    st.success("You already have all top skills for this role! 🎉")

st.markdown("---")

# 6. Visualization
st.subheader(f"📊 Top Skills Visualization for {selected_role}")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x="count",
    y="skill_normalized",
    data=top20,
    palette="magma",
    ax=ax
)

ax.set_title(f"Top 20 Skills for {selected_role}", fontsize=14)
ax.set_xlabel("Job Postings Count")
ax.set_ylabel("Skill")

st.pyplot(fig)
plt.close(fig)
