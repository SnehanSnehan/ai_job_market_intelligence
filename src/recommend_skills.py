# src/app.py

import streamlit as st
import pandas as pd

# -------------------------------
# Load preprocessed data
# -------------------------------
top_skills_by_role_file = "data/top_skills_by_role.csv"
top_skills_overall_file = "data/top_skills_overall.csv"

top_skills_role_df = pd.read_csv(top_skills_by_role_file)
top_skills_overall_df = pd.read_csv(top_skills_overall_file)

# Get unique roles dynamically
roles = sorted(top_skills_role_df['job_title_clean'].unique())

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("📊 AI Job Market Intelligence Dashboard")

st.sidebar.header("User Input")
selected_role = st.sidebar.selectbox("Select your target role", roles)
candidate_skills_input = st.sidebar.text_input(
    "Enter your skills (comma separated)", ""
)
candidate_skills = [s.strip().lower() for s in candidate_skills_input.split(",") if s.strip()]

# -------------------------------
# Top Skills for Selected Role
# -------------------------------
st.subheader(f"🔥 Top Skills for {selected_role.title()}")

role_top_skills = (
    top_skills_role_df[top_skills_role_df["job_title_clean"] == selected_role]
    .sort_values("count", ascending=False)
)
st.dataframe(role_top_skills.reset_index(drop=True))

# -------------------------------
# Skill Gap Calculation
# -------------------------------
if candidate_skills:
    role_skills_list = role_top_skills['skill_normalized'].str.lower().tolist()
    matched_skills = [s for s in candidate_skills if s in role_skills_list]
    missing_skills = [s for s in role_skills_list if s not in candidate_skills]

    skill_gap_pct = round(100 * (len(missing_skills) / len(role_skills_list)), 1) if role_skills_list else 0

    st.subheader("📉 Skill Gap")
    st.write(f"**Skill Gap Percentage:** {skill_gap_pct}%")
    st.write("**Matched skills:**", matched_skills if matched_skills else "None")
    st.write("**Missing skills:**", missing_skills if missing_skills else "None")
else:
    st.subheader("📉 Skill Gap")
    st.write("Enter your skills above to see skill gap and recommendations.")

# -------------------------------
# Learning Recommendations
# -------------------------------
st.subheader("🎯 Learning Recommendations")
if candidate_skills:
    # Assign priority based on count
    recommendations = []
    for _, row in role_top_skills.iterrows():
        skill = row['skill_normalized'].lower()
        if skill not in candidate_skills:
            count = row['count']
            if count >= 50:
                priority = "High"
            elif count >= 20:
                priority = "Medium"
            else:
                priority = "Low"
            recommendations.append({
                "role": selected_role,
                "recommended_skill": skill,
                "priority": priority,
                "market_demand": count
            })

    if recommendations:
        recommendations_df = pd.DataFrame(recommendations)
        st.dataframe(recommendations_df)
    else:
        st.write("You already have all top skills for this role! 🎉")
else:
    st.write("Enter your skills above to generate recommendations.")

# -------------------------------
# Top Skills Visualization
# -------------------------------
st.subheader(f"📊 Top Skills Visualization for {selected_role.title()}")
st.bar_chart(role_top_skills.set_index("skill_normalized")["count"])
