# AI-Powered Job Market Intelligence & Skill Gap Analyzer

## Project Overview

This project analyzes real job postings to identify in-demand skills, job role trends, and personalized skill gaps for candidates. It provides actionable insights through an interactive dashboard that helps job seekers understand market requirements and plan their learning journey accordingly.

## Project Structure

The project is organized into the following directories:
```
ai_job_market_intelligence/
│
├── data/
│   ├── job_postings_cleaned.csv
│   ├── top_skills_by_role.csv
│   └── [raw and processed datasets]
│
├── src/
│   ├── app.py                    # Streamlit dashboard
│   ├── generate_insights.py      # Skill aggregation logic
│   ├── recommend_skills.py       # Learning recommendation logic
│   └── [additional Python modules]
│
├── notebooks/
│   └── [Jupyter notebooks for data exploration]
│
├── plots/
│   └── [Generated visualizations]
│
├── dashboard/
│   └── [Streamlit dashboard scripts]
│
├── docs/
│   └── [Documentation and reports]
│
├── venv/                         # Python virtual environment
├── run_all.py                    # Master script for end-to-end execution
├── requirements.txt              # Project dependencies
└── README.md
```

## Key Features

The project delivers the following capabilities:

- **Job Market Analysis**: Processes and analyzes real job postings to extract high-demand skills across various roles
- **Skill Gap Assessment**: Compares candidate skills against current market requirements to identify learning opportunities
- **Personalized Recommendations**: Provides tailored learning recommendations based on individual skill gaps
- **Interactive Visualizations**: Displays skill demand trends through charts and tables for easy interpretation
- **Role-Based Insights**: Allows users to explore top skills filtered by specific job roles

## Technology Stack

This project is built using:

- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation and analysis
- **Streamlit**: Interactive web dashboard framework
- **Seaborn & Matplotlib**: Data visualization libraries
- **CSV-based datasets**: Data storage and processing

## Getting Started

Follow these steps to run the project on your local machine:

### Prerequisites

Ensure you have Python installed on your system (Python 3.8 or higher recommended).

### Installation and Execution

1. **Activate the Virtual Environment**

   On Windows:
```bash
   venv\Scripts\activate
```

   On macOS/Linux:
```bash
   source venv/bin/activate
```

2. **Install Required Dependencies**

   If you haven't installed the dependencies yet:
```bash
   pip install -r requirements.txt
```

3. **Launch the Dashboard**

   Run the Streamlit application:
```bash
   streamlit run src/app.py
```

4. **Access the Dashboard**

   Open your web browser and navigate to:
```
   http://localhost:8501
```

### Alternative: Run Complete Pipeline

To execute the entire project pipeline from data processing to visualization:
```bash
python run_all.py
```

## Dashboard Functionality

The interactive dashboard provides:

- **Role Selection**: Choose from available job roles in the market data
- **Top Skills Display**: View the most in-demand skills ranked by frequency
- **Skill Gap Analysis**: Receive personalized recommendations based on your current skill set
- **Visual Insights**: Explore interactive charts showing skill demand patterns
- **Learning Pathways**: Get suggested resources and skills to focus on for career growth

## Data Organization

The project handles data in multiple stages:

- **Raw Data**: Original job posting datasets stored in the data directory
- **Cleaned Data**: Processed and normalized datasets ready for analysis
- **Analysis Outputs**: CSV files containing aggregated insights (e.g., top_skills_by_role.csv)
- **Visualizations**: Charts and plots saved in the plots directory

## Future Enhancements

Planned improvements for the project include:

- Salary trend analysis by role and skill level
- Location-based job market insights and regional demand patterns
- Enhanced skill gap scoring with weighted recommendations
- Database integration for scalable data management
- Resume parsing and automatic skill matching
- Real-time job posting scraping and updates
- Comparative analysis across different experience levels

## Project Documentation

Additional documentation and analysis notebooks are available in the following directories:

- **notebooks/**: Jupyter notebooks with exploratory data analysis
- **docs/**: Detailed documentation and analytical reports
- **plots/**: Visual outputs from various analyses

## Author

**Snehan**  
AI & Data Analytics Project

## License

This project is developed for educational and portfolio purposes.

---

For questions or suggestions regarding this project, please feel free to reach out or open an issue in the repository.