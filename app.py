import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
from typing import List, Dict
import requests
from io import StringIO

# Set page config
st.set_page_config(
    page_title="SaaSquatch Leads Enhanced",
    page_icon="🦥",
    layout="wide"
)

# Title and description
st.title("🦥 SaaSquatch Leads Enhanced")
st.markdown("""
This enhanced version of SaaSquatchLeads adds intelligent lead scoring and advanced filtering capabilities 
to help sales teams prioritize high-value prospects more effectively.
""")

# Sample data generation function
@st.cache_data
def generate_sample_data(n_companies=1000) -> pd.DataFrame:
    """Generate sample lead data for demonstration"""
    np.random.seed(42)
    
    companies = [f"Company {i}" for i in range(1, n_companies+1)]
    websites = [f"www.company{i}.com" for i in range(1, n_companies+1)]
    
    # Tech stacks
    tech_stacks = [
        "Python, Django, PostgreSQL",
        "React, Node.js, MongoDB",
        "Java, Spring, MySQL",
        "Vue.js, Express, PostgreSQL",
        "Angular, .NET, SQL Server",
        "Ruby on Rails, PostgreSQL",
        "Flutter, Firebase",
        "React Native, Node.js",
        "Swift, iOS",
        "Kotlin, Android"
    ]
    
    # Industries
    industries = [
        "Software", "Healthcare", "Finance", "E-commerce", 
        "Education", "Manufacturing", "Retail", "Real Estate"
    ]
    
    # Locations
    locations = [
        "San Francisco, CA", "New York, NY", "London, UK", "Berlin, Germany",
        "Austin, TX", "Seattle, WA", "Boston, MA", "Toronto, Canada",
        "Vancouver, Canada", "Sydney, Australia"
    ]
    
    # Generate data
    data = {
        "company": companies,
        "website": websites,
        "industry": np.random.choice(industries, n_companies),
        "location": np.random.choice(locations, n_companies),
        "tech_stack": np.random.choice(tech_stacks, n_companies),
        "employee_count": np.random.randint(10, 5000, n_companies),
        "revenue_estimate": np.random.randint(100000, 10000000, n_companies),
        "funding_stage": np.random.choice(["Seed", "Series A", "Series B", "Series C+", "Public"], n_companies),
        "description": [f"A {np.random.choice(industries).lower()} company using {np.random.choice(tech_stacks[:3])} technology" for _ in range(n_companies)]
    }
    
    df = pd.DataFrame(data)
    
    # Add some realistic correlations
    # Larger companies tend to have higher revenue
    df["revenue_estimate"] = df["revenue_estimate"] * (df["employee_count"] / 1000)
    
    # Later stage companies tend to have higher revenue
    stage_multiplier = {"Seed": 0.5, "Series A": 1, "Series B": 2, "Series C+": 3, "Public": 5}
    df["revenue_estimate"] = df["revenue_estimate"] * df["funding_stage"].map(stage_multiplier)
    
    # Add lead score based on multiple factors
    df["lead_score"] = calculate_lead_score(df)
    
    return df

def calculate_lead_score(df: pd.DataFrame) -> np.ndarray:
    """Calculate lead score based on multiple factors"""
    # Normalize factors to 0-1 scale
    employee_score = (df["employee_count"] - df["employee_count"].min()) / (df["employee_count"].max() - df["employee_count"].min())
    revenue_score = (df["revenue_estimate"] - df["revenue_estimate"].min()) / (df["revenue_estimate"].max() - df["revenue_estimate"].min())
    
    # Funding stage score (later stages are better)
    stage_scores = {"Seed": 0.2, "Series A": 0.5, "Series B": 0.7, "Series C+": 0.9, "Public": 1.0}
    funding_score = df["funding_stage"].map(stage_scores)
    
    # Weighted combination
    lead_score = (employee_score * 0.3 + revenue_score * 0.4 + funding_score * 0.3) * 100
    return lead_score.round(2)

# Load data
@st.cache_data
def load_data():
    return generate_sample_data()

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Lead Filters")

# Industry filter
industries = st.sidebar.multiselect(
    "Industry",
    options=df["industry"].unique(),
    default=None
)

# Location filter
locations = st.sidebar.multiselect(
    "Location",
    options=df["location"].unique(),
    default=None
)

# Tech stack filter
tech_keywords = st.sidebar.text_input(
    "Tech Stack Keywords",
    placeholder="e.g., Python, React, etc."
)

# Employee count range
employee_range = st.sidebar.slider(
    "Employee Count",
    min_value=int(df["employee_count"].min()),
    max_value=int(df["employee_count"].max()),
    value=(int(df["employee_count"].min()), int(df["employee_count"].max()))
)

# Revenue range
revenue_range = st.sidebar.slider(
    "Revenue Estimate ($)",
    min_value=int(df["revenue_estimate"].min()),
    max_value=int(df["revenue_estimate"].max()),
    value=(int(df["revenue_estimate"].min()), int(df["revenue_estimate"].max())),
    format="$%d"
)

# Funding stage filter
funding_stages = st.sidebar.multiselect(
    "Funding Stage",
    options=df["funding_stage"].unique(),
    default=None
)

# Lead score range
lead_score_range = st.sidebar.slider(
    "Lead Score",
    min_value=float(df["lead_score"].min()),
    max_value=float(df["lead_score"].max()),
    value=(float(df["lead_score"].min()), float(df["lead_score"].max()))
)

# Apply filters
filtered_df = df.copy()

if industries:
    filtered_df = filtered_df[filtered_df["industry"].isin(industries)]

if locations:
    filtered_df = filtered_df[filtered_df["location"].isin(locations)]

if tech_keywords:
    keywords = [kw.strip() for kw in tech_keywords.split(",")]
    mask = filtered_df["tech_stack"].str.contains("|".join(keywords), case=False, na=False)
    filtered_df = filtered_df[mask]

filtered_df = filtered_df[
    (filtered_df["employee_count"] >= employee_range[0]) &
    (filtered_df["employee_count"] <= employee_range[1]) &
    (filtered_df["revenue_estimate"] >= revenue_range[0]) &
    (filtered_df["revenue_estimate"] <= revenue_range[1]) &
    (filtered_df["lead_score"] >= lead_score_range[0]) &
    (filtered_df["lead_score"] <= lead_score_range[1])
]

if funding_stages:
    filtered_df = filtered_df[filtered_df["funding_stage"].isin(funding_stages)]

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"🎯 {len(filtered_df)} Leads Found")
    
    # Display leads in a table
    display_columns = ["company", "industry", "location", "tech_stack", "employee_count", "revenue_estimate", "funding_stage", "lead_score"]
    st.dataframe(
        filtered_df[display_columns].rename(columns={
            "company": "Company",
            "industry": "Industry",
            "location": "Location",
            "tech_stack": "Tech Stack",
            "employee_count": "Employees",
            "revenue_estimate": "Revenue Est.",
            "funding_stage": "Funding",
            "lead_score": "Lead Score"
        }),
        use_container_width=True,
        hide_index=True
    )

with col2:
    st.subheader("📊 Lead Insights")
    
    # Lead score distribution
    fig_score = px.histogram(filtered_df, x="lead_score", nbins=20, title="Lead Score Distribution")
    fig_score.update_layout(showlegend=False)
    st.plotly_chart(fig_score, use_container_width=True)
    
    # Industry breakdown
    industry_counts = filtered_df["industry"].value_counts().head(10)
    fig_industry = px.pie(values=industry_counts.values, names=industry_counts.index, title="Leads by Industry")
    st.plotly_chart(fig_industry, use_container_width=True)
    
    # Funding stage breakdown
    funding_counts = filtered_df["funding_stage"].value_counts()
    fig_funding = px.bar(x=funding_counts.index, y=funding_counts.values, title="Leads by Funding Stage")
    fig_funding.update_layout(xaxis_title="Funding Stage", yaxis_title="Count")
    st.plotly_chart(fig_funding, use_container_width=True)

# Export functionality
st.subheader("📤 Export Leads")
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="saasquatch_leads.csv",
    mime="text/csv"
)

# Lead scoring explanation
with st.expander("ℹ️ How Lead Scoring Works"):
    st.markdown("""
    Our lead scoring algorithm evaluates companies based on multiple factors:
    
    1. **Employee Count (30% weight)**: Larger companies often have more resources for partnerships
    2. **Revenue Estimate (40% weight)**: Higher revenue indicates business stability and potential value
    3. **Funding Stage (30% weight)**: Later-stage companies are more established and have proven market fit
    
    The score ranges from 0-100, with higher scores indicating more promising leads.
    """)