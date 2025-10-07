# Caprae Capital Developer Intern Challenge Submission

## Project Overview

This repository contains my submission for the Caprae Capital Developer Intern pre-work challenge. I've enhanced the SaaSquatchLeads tool with intelligent lead scoring and advanced filtering capabilities to demonstrate business impact through data-driven lead prioritization.

## Files Included

1. `app.py` - Main Streamlit application with enhanced lead scoring and filtering
2. `requirements.txt` - Python dependencies
3. `README.md` - Setup instructions and project overview
4. `report.md` - Detailed report on approach, implementation, and business value
5. `business_understanding.md` - Answers to business understanding questions
6. `video_script.md` - Script for the required 1-2 minute demo video

## Key Enhancements

### Intelligent Lead Scoring Algorithm
- Multi-factor scoring based on employee count, revenue estimates, and funding stage
- Weighted approach (40% revenue, 30% employee count, 30% funding stage)
- Visual distribution of lead scores

### Advanced Filtering Capabilities
- Industry, location, and tech stack filters
- Employee count and revenue range sliders
- Funding stage multiselect
- Lead score range filter

### Enhanced Data Visualization
- Lead score distribution histogram
- Industry breakdown pie chart
- Funding stage bar chart

### Export Functionality
- One-click CSV export of filtered leads
- Clean formatting for CRM integration

## Business Value

This enhanced tool helps sales teams:
- Prioritize leads based on data-driven scoring
- Filter prospects by specific criteria quickly
- Gain insights into their lead pipeline
- Export qualified leads for outreach campaigns

## How to Run

1. Ensure Python 3.8+ is installed
2. Install dependencies with `pip install -r requirements.txt`
3. Run with `streamlit run app.py`
4. Access the application at http://localhost:8501

## Future Enhancements

- Integration with real data sources (LinkedIn Sales Navigator, Apollo.io, etc.)
- ML-based predictive lead scoring using historical conversion data
- CRM integration (Salesforce, HubSpot, etc.)
- Email verification and social media enrichment features

## Time Investment

This enhancement was completed within the 5-hour time constraint, with careful attention to business value and user experience.