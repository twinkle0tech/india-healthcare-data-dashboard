# 🏥 Healthcare Infrastructure vs Population in India
A Data Analytics & Visualization Dashboard (Streamlit)

live - https://india-healthcare-dashboard.streamlit.app/
---

## 📌 Project Overview

During the COVID-19 pandemic, India faced a severe shortage of hospital beds, healthcare facilities, and medical infrastructure. Many people struggled to find basic treatment facilities, highlighting deep inequalities in healthcare availability across different states and regions.

This project aims to analyze India’s healthcare infrastructure relative to population size, identify underserved states, and present the findings through an interactive dashboard built using Python and Streamlit.

- The dashboard helps answer an important question:

Is healthcare infrastructure in India evenly distributed according to population needs?

---

## 🎯 Problem Statement

India has wide regional disparities in healthcare availability.
While some states have strong healthcare infrastructure, others struggle with limited hospital beds, facilities, and access to care.

The key challenges addressed:

- Unequal distribution of hospital beds across states

- High population pressure on limited healthcare facilities

- Lack of easy-to-understand visual tools for policy-level insights

- This project focuses on per-capita healthcare metrics rather than raw numbers, making comparisons fair and meaningful.
  
---

## 🧠 Why This Project?

I selected this project because:

- Real-world impact: COVID-19 exposed major gaps in India’s healthcare system, making this        problem highly relevant and meaningful.

- Strong problem statement: Healthcare availability is not equal across states, and this          project directly explores that inequality.

- Per-capita analysis focus: Instead of raw numbers, I used Beds per 1 Lakh Population to make    comparisons fair and realistic.

- It combines data analysis + visualization + real-world impact

- This project helped me apply data analytics concepts to a socially relevant problem.

---

## 📊 Dataset Description

The dataset includes state-wise healthcare and population data sourced from public government records.

 **Population Data:** Census of India (2011) with projected estimates  
- **Healthcare Infrastructure Data:** Ministry of Health & Family Welfare (MoHFW), Government of India  
- **Time Period:** 2019–2021 (latest publicly available)

 **Key data fields:**

- Population (Census-based)

- Total Hospital Beds

- District Hospitals

- Sub-District / Sub-Divisional Hospitals

- Medical Colleges

- Beds per 1 Lakh Population

- Healthcare Adequacy Level (Low / Medium / High)

- Underserved Status

- Region & State Category

---

## 🔍 Key Metrics (KPIs)

The dashboard highlights four important indicators:

- Total Population
Shows the population covered under the selected filters.

- Total Hospitals
Indicates the available healthcare facilities.

- Average Beds per 1 Lakh Population
A standardized metric to compare states fairly.

- Underserved States
Identifies states that fall below acceptable healthcare thresholds.

- These KPIs provide a quick snapshot of healthcare capacity.

## 🗺️ Visualizations & Features
-- 1️⃣ India Map – Beds per 1 Lakh Population

Displays state-wise healthcare capacity

Color-coded for easy comparison 

Hover tooltips show detailed state information

Why used:
Maps help instantly identify regional disparities.

-- 2️⃣ Bar Chart – Beds per Lakh vs State

Compares healthcare availability across states

Highlights high-performing and low-performing regions

Why used:
Bar charts allow direct state-to-state comparison.

-- 3️⃣ Pie Chart – Healthcare Adequacy Distribution

Shows proportion of states in Low / Medium / High categories

Why used:
Helps understand the overall national healthcare situation at a glance.

-- 4️⃣ Interactive Filters

Users can filter data by:

State category (Large / Low population)

Region

Healthcare adequacy level

- Why used:
Allows focused analysis for specific regions or policy questions.

---

## 🧪 Data Cleaning & Processing

-- The dataset was initially cleaned and structured in Excel to review and handle missing or inconsistent values.

-- New derived columns (such as beds per 1 lakh population, healthcare adequacy level, and underserved status) were created to support more meaningful and standardized analysis.

-- Some values are missing due to non-availability or non-reporting of certain healthcare facilities for specific states/UTs in the original public records.

-- These missing values reflect real-world data limitations rather than data errors.

-- The processed dataset was then further validated in Python to ensure numeric consistency and analytical reliability.

## 🛠️ Tech Stack

- Python

- Streamlit

- Pandas

- Plotly

- OpenPyXL

- CSS (for UI styling)
  
---
## 📁 Project Structure
```
 Dashboard_healthcare-infrastructure
 ├── app.py
 ├── data/
 │   ├── raw/
 │   └── processed/
 ├── assets/
 │   └── logo.png
 ├── styles/
 │   └── style.css
 ├── requirements.txt
 └── README.md

```

## 🚀 How to Run the Project

- Install dependencies:

    pip install -r requirements.txt


- Run the app:

   streamlit run app.py


- Open in browser:

    http://localhost:8501

## 🧩 Key Learnings

- Importance of per-capita analysis

- Handling real-world messy datasets

- Building interactive dashboards

- Translating data into actionable insights

- UI/UX considerations for analytics tools

## 🔮 Future Improvements

- Time-series analysis (pre vs post COVID)

- District-level deep dive

- Integration with real-time health data

- Exportable reports (PDF)


## Data Limitations
- Government healthcare data may have reporting delays and may not reflect recent infrastructure upgrades.
- Private hospital capacity may be underrepresented in certain states.
- Beds per 1 lakh population indicates availability but does not account for quality of care or staffing levels.

## 🏁 Conclusio

This project demonstrates how data analytics and visualization can help identify gaps in healthcare infrastructure and support data-driven policy decisions.

It reflects my understanding of:

- Data cleaning

- Analytical thinking

- Visualization

- Real-world problem solving
  
---
## preview
<img width="1862" height="963" alt="Screenshot 2026-01-06 232236" src="https://github.com/user-attachments/assets/d945a76b-6030-4af2-abd8-ab1c2336cf2c" />

---

## 👤 Author

Muskan Tamang /
Student 
