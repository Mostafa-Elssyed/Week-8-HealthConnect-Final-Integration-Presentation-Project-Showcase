# 🏥 HealthConnect Clinic Experience Lab - Data Analytics Workspace

## 📌 Project Master Overview & Business Context
**Project Title:** Improving Patient Appointment Attendance and Healthcare Support Using Data and AI  
**Track:** Data Analytics Stream  
**Operational Status:** ACTIVE / VALIDATED  

This workspace tracks a continuous, incremental analytical laboratory journey designed to isolate, understand, and predict the underlying logistical and behavioral drivers behind patient appointment no-shows. By programmatically auditing transactional booking logs, this system provides clinical leadership with a high-fidelity tool to identify operational bottlenecks and enhance care compliance.

---

## 💻 Local Deployment: Run the Portal on Your Machine

To execute this medical analytics interface and test the dynamic data models locally across any device, initialize the workspace container using these standard, environment-agnostic terminal commands:

### 1. Ingest Project Libraries Layer
Navigate to the project root directory in your command line interface and install our version-locked system dependencies:
```bash
pip install -r requirements.txt
```

### 2. Initialize the Active Dashboard Container
Fires up the dynamic execution server, broadcasting a fully responsive boardroom portal directly to a new browser tab:
```bash
streamlit run app.py
```
*Note: The system container initializes automatically at `http://localhost:8501`.*

---

## 🗃️ Repository Architecture Map & File Directory

### 📂 1. Primary Root Code Elements
*   **`/app.py`**: The primary executable interactive dashboard interface containing metric models, Plotly distributions, and live machine learning model validation panels.
*   **`/requirements.txt`**: Version-locked project environment configuration manifest mapping target code dependencies for portably deploying across external machines.
*   **`/README.md`**: *This file.* The master context manual providing onboarding rules and a complete project history overview.
*   **`/healthconnect_analysis.ipynb`**: Master progressive Jupyter Notebook containing historic sandbox data cleaning and wrangling scripts.

### 📂 2. Master Document Archive (`/documentation/`)
*   **`documentation/REPOSITORY_ROADMAPPING_GUIDE.md`**: Core reference file breaking down chronological phase shifts and file naming patterns across the lifecycle of the project.
*   **`documentation/WEEK_7_PROJECT_SUMMARY.md`**: Standalone summary report tracking Week 7 boundary metrics, float rounding corrections, and final operational readiness.
*   **`documentation/CROSS_TRACK_HANDOFF.txt`**: Technical ledger detailing the **Test ➔ Finding ➔ Fix ➔ Retest** interaction loop that successfully balanced our analytics aggregates with the ML Engineering track.
*   **`documentation/WEEK_6_ANALYTICS_REPORT.md`**: Historic Week 6 technical analysis detailing newly engineered column variables.
*   **`documentation/WEEK_5_ANALYTICS_REPORT.md`**: Historic Week 5 exploratory report mapping out travel distance, notification channel, and scheduling lag insights.
*   **`documentation/Initial_Analysis_Document.txt`**: Foundational Week 4 document logging missing data counts and raw database quality flaws before cleaning.
*   **`documentation/Week_4_Project_Summary.txt`**: Plaintext milestone report documenting Week 4 execution maps.
*   **`documentation/distance_barrier_chart.png`**: Week 5 geographic proximity chart proving distance limits affect clinic attendance.
*   **`documentation/lead_time_attrition_chart.png`**: Week 5 temporal chart tracing show-rate drops against advance booking windows.
*   **`documentation/reminder_effectiveness_chart.png`**: Week 5 outreach chart mapping final conversion yield variations across text alerts.

### 📂 3. Data & Automation Frameworks (`/data/` and `/src/`)
*   **`data/HealthConnect_Cleaned_Data_Week5.csv`**: Our heavily scrubbed master analytics database file used as the backend for all dynamic calculations.
*   **`data/HealthConnect_Appointment_Data.csv`**: Raw, unedited clinic cohort database containing 5,000 anonymized transactional logs.
*   **`data/HealthConnect_Data_Dictionary.xlsx`**: Master reference matrix mapping out target column classifications and variables.
*   **`src/verify_data.py`**: Automated pipeline validation scripts developed during Week 6 engineering to check schema boundaries.

---

## 🔬 Week 7 Root Core Testing Insights
*   **The Pipeline Glitch Discovered:** Groupby aggregation matrices on extreme lead-time filters originally truncated deep decimals, creating an underlying **2.4% baseline calculation discrepancy**.
*   **The Optimization Fix Applied:** Refactored explicit array rounding constraints directly into the system processing scripts (`app.py`), syncing Analytics aggregates perfectly with raw database rows. Coordinates data vectors with the Machine Learning engineering track to adjust predictive feature scales—compressing downstream prediction variance down to a verified **1.34% target threshold (PASS)**.

## 🚀 Week 8: Final Deployment & Cross-Track Integration
**Status:** ARCHIVED & COMPLETED (September 27, 2026)

### 📊 Final Integration Summary
During this final phase, the HealthConnect Data Analytics pipeline was successfully audited and verified for multidisciplinary deployment. The interactive metrics engine (`app.py`) has been fully cross-referenced against the raw dataset to achieve absolute reporting integrity.

### 🔌 Verified Pipeline Connections
*   **Inbound Data Sync:** Integrated feature weights from the Data Science candidate models to back up our lead-time attrition thresholds (>14 days).
*   **Outbound Data Hand-off:** Exported the multi-channel notification effectiveness matrices (`reminder_effectiveness_chart.png`) to the Generative AI track to calibrate prompt rules for the live Clinic Assistant.
*   **Management Layer Hand-off:** Forwarded the final metrics engine data to the Project Management track to generate ROI tracking metrics.

### 🛠️ Local Code Maintenance Logs
*   Resolved the 2.4% floating-point truncation anomaly inside the Pandas `.groupby()` aggregation strings. 
*   Enforced explicit string and float rounding arrays inside `app.py`, dropping cross-track data alignment variance to a verified 1.34% threshold.
