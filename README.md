# SaaSquatch Leads Enhanced - Caprae Capital Challenge

This is my submission for the Caprae Capital Developer Intern pre-work challenge. I've enhanced the SaaSquatchLeads tool with intelligent lead scoring and advanced filtering capabilities.

## 🚀 Features Added

1. **Intelligent Lead Scoring Algorithm**:
   - Scores leads based on employee count, revenue estimates, and funding stage
   - Weighted scoring system to prioritize high-value prospects
   - Visual distribution of lead scores

2. **Advanced Filtering Options**:
   - Industry, location, and tech stack filters
   - Employee count and revenue range sliders
   - Funding stage multiselect
   - Lead score range filter

3. **Enhanced Data Visualization**:
   - Lead score distribution histogram
   - Industry breakdown pie chart
   - Funding stage bar chart

4. **Export Functionality**:
   - One-click CSV export of filtered leads
   - Clean data formatting for CRM integration

5. **Business Intelligence**:
   - Explanation of lead scoring methodology
   - Data-driven insights for sales prioritization

## 🛠️ Technical Implementation

- **Streamlit**: For rapid prototyping and intuitive UI
- **Pandas**: For data manipulation and analysis
- **Plotly**: For interactive data visualizations
- **Caching**: For efficient data loading and processing

## 📦 Setup Instructions

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd lead-enrich-streamlit
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. The app will open in your default browser at `http://localhost:8501`

## 🎯 Business Value

This enhanced tool helps sales teams:
- Prioritize leads based on data-driven scoring
- Filter prospects by specific criteria quickly
- Gain insights into their lead pipeline
- Export qualified leads for outreach campaigns

The lead scoring algorithm focuses on factors that indicate a company's potential value as a customer, helping sales teams maximize their efficiency.

## 📹 Demo

[Link to demo video would go here]

## 📝 Challenge Response

### What is Caprae's Mission?
Caprae Capital's mission is to transform businesses through strategic initiatives, particularly by leveraging AI to unlock new growth opportunities. Unlike traditional PE firms that rely heavily on financial engineering, Caprae focuses on operational value creation post-acquisition through their unique SaaS and M&A as a Service models.

### How is Caprae Changing the ETA Space and Broader PE?
Caprae is revolutionizing the ETA space and broader PE industry by treating M&A as a seven-year journey where greater value creation happens post-acquisition rather than at the time of acquisition. They combine technology with a unique support model to turn good businesses into great ones, emphasizing founder/operator culture over purely financial metrics.

## 📬 Submission

To run this project:
1. Ensure Python 3.8+ is installed
2. Install dependencies with `pip install -r requirements.txt`
3. Run with `streamlit run app.py`
4. Access the application at http://localhost:8501

## 📁 Project Structure

```
lead-enrich-streamlit/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── report.md              # Detailed implementation report
├── business_understanding.md  # Answers to business questions
├── video_script.md        # Script for demo video
├── SUBMISSION_SUMMARY.md  # Submission overview
├── SUBMISSION_EMAIL_TEMPLATE.md  # Email template
└── STOP_APPLICATION.md    # Instructions to stop the app
```

## ⏱️ Time Investment

This enhancement was completed within the 5-hour time constraint specified in the challenge, with careful attention to:
- Business value and user experience
- Technical implementation quality
- Code organization and documentation
- Future extensibility

## 🧩 Future Enhancements

- Integration with real data sources (LinkedIn Sales Navigator, Apollo.io, etc.)
- ML-based predictive lead scoring using historical conversion data
- CRM integration (Salesforce, HubSpot, etc.)
- Email verification and social media enrichment features