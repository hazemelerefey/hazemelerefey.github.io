# 5 Data Analytics Portfolio Projects

## Project 1: Global E-Commerce Sales Forecasting
**Dataset source:** Kaggle Global Superstore Dataset (or simulated API)
**Tools used:** Python, Pandas, Statsmodels, Power BI
**5 key analysis tasks performed:**
1. Cleaned and processed multi-year sales data dealing with missing entries.
2. Explored seasonality and sales trends across different global regions.
3. Built an ARIMA-based time-series forecasting model for next-quarter sales.
4. Identified top 10 most profitable product sub-categories vs bottom 10.
5. Created a dynamic Power BI dashboard for executive overview.
**Business insight:** 
Revealed that expanding product line X in region Y instead of Z could increase quarterly profitability by 12% based on forecasted trends.

## Project 2: Customer Churn Prediction & Retention Strategy
**Dataset source:** Telco Customer Churn Dataset (Kaggle / Public API)
**Tools used:** Python, Scikit-Learn, Seaborn, SQL
**5 key analysis tasks performed:**
1. Extracted and joined customer demographic and subscription tables using SQL.
2. Conducted Exploratory Data Analysis (EDA) to map out correlated features (e.g. Contract length vs Churn).
3. Engineered new features handling categorical variables using One-Hot Encoding.
4. Trained a Random Forest Classifier achieving 85% prediction accuracy.
5. Visualized feature importance revealing crucial factors driving churn.
**Business insight:** 
Found that customers on month-to-month contracts lacking tech support are 4x more likely to churn. Recommends targeted 1-year contract discounts.

## Project 3: Real Estate Market Price Drivers
**Dataset source:** Zillow API or Airbnb Open Data
**Tools used:** Python, Pandas, NumPy, Matplotlib, Tableau
**5 key analysis tasks performed:**
1. Web scraped / queried large real estate datasets API.
2. Cleaned messy unstructured text columns (e.g., amenities, locations).
3. Performed geospatial analysis mapping average prices by neighborhood.
4. Analyzed sentiment of text reviews impacting pricing (if Airbnb dataset).
5. Built an interactive Tableau dashboard comparing property features.
**Business insight:** 
Identified that adding "smart home" amenities increases listing potential price by 8% in urban zip codes as opposed to suburban ones.

## Project 4: Healthcare Wait Time Optimization
**Dataset source:** Open Data portals (e.g., Medicare/Medicaid Hospital Wait Times)
**Tools used:** SQL, Python, Pandas, Power BI
**5 key analysis tasks performed:**
1. Consolidated multiple messy spreadsheets into a normalized SQL database.
2. Wrote complex SQL window functions to track patient journey times.
3. Statistically analyzed peak hours for emergency room admissions.
4. Created a Power BI dashboard tracking KPIs like "Time to see Doctor".
5. Modeled optimal staff scheduling based on historical admission data.
**Business insight:** 
Demonstrated that shifting 2 nurses from morning to evening shifts on weekends could reduce average patient wait times by 22%.

## Project 5: Social Media Campaign Sentiment Analysis
**Dataset source:** Twitter API or Reddit API (PRAW)
**Tools used:** Python, NLTK/VADER, Pandas, Seaborn
**5 key analysis tasks performed:**
1. Streamed thousands of tweets/posts related to a specific product launch.
2. Cleaned text data (removed URLs, emojis, stop words).
3. Applied VADER sentiment analysis to categorize text into Positive/Neutral/Negative.
4. Generated word clouds isolating most frequent pain points mentioned.
5. Plotted sentiment progression timeline over the 2-week campaign period.
**Business insight:** 
Highlighted that despite high overall engagement, a specific software update feature caused a 30% spike in negative sentiment on Day 3, enabling rapid PR response.

---

# Professional README.md Template for Data Analytics Projects

```markdown
# [PROJECT NAME]

![Project Banner](https://via.placeholder.com/800x200?text=Data+Analytics+Project+Banner)

## 📌 Project Overview & Objective
This project analyzes **[TOPIC]** to uncover actionable business insights. The main objective was to understand the underlying patterns of [Target Variable] and provide strategic recommendations to [Stakeholders].

## 📊 Dataset Description
The analysis leverages the **[Dataset Name]** dataset, containing over [Number] rows and [Number] columns of data spanning from [Year] to [Year].
- **Source:** [Link to Dataset Placeholder]
- **Key Features:** [Feature 1], [Feature 2], [Feature 3], [Feature 4]

## 🛠️ Methodology
1. **Data Collection:** Queried via SQL / Downloaded from Kaggle.
2. **Data Cleaning:** Addressed [X%] missing values, handled outliers using [Method].
3. **Exploratory Data Analysis (EDA):** Visualized distributions and correlations.
4. **Modeling / Deep Dive:** Applied [Algorithm/Statistical Method].
5. **Dashboarding:** Built interactive [Power BI / Tableau] visual reports.

## 💡 Key Findings & Insights
- **Insight 1:** Found that [X feature] increases the likelihood of [Y outcome] by [Z%].
- **Insight 2:** Identified a [positive/negative] trend in [Metric] during [Timeframe].
- **Insight 3:** [Business impact recommendation based on finding].

## 📈 Visualizations
![Visualization 1](https://via.placeholder.com/400x250?text=Chart+1+Placeholder)
![Visualization 2](https://via.placeholder.com/400x250?text=Chart+2+Placeholder)
*(You can interactive dashboard links here: [View Dashboard](#))*

## 🚀 How to Run the Notebook
1. Clone this repository:
   \`\`\`bash
   git clone https://github.com/[YOUR_USERNAME]/[PROJECT_NAME].git
   cd [PROJECT_NAME]
   \`\`\`
2. Install required packages:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
3. Launch Jupyter Notebook:
   \`\`\`bash
   jupyter notebook
   \`\`\`
4. Open \`analysis_notebook.ipynb\` and run the cells.

## 💻 Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

## 🎯 Conclusions
Summarize the final thoughts. For instance: By addressing the issues highlighted in the analysis, the business could save an estimated [Dollar amount] annually. Future work could include integrating a real-time data pipeline for live tracking.

---
**Author:** [Hazem Elerefy](https://github.com/hazemelerefey)
```
