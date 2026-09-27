# HealthConnect Clinic Lab - Master Repository & File Navigation Guide
**Track:** Data Analytics Stream  
**Purpose:** Structural Context Bridge & Directory Naming Convention Map for Reviewers

---

## 📖 Chronological Phase Definitions
To assist the grading team in tracking progressive laboratory milestones, files are named strictly according to the phase mandates dictated by the internship syllabus. Because the core focus shifted each week, file types naturally evolved:

1. **Week 4 Phase: Problem Understanding & Ingestion**
   * *Mandate:* Ingest raw assets, define metrics, profile source database anomalies.
   * *Naming Logic:* No analytics report was generated during this phase because no data cleaning or statistical testing had occurred yet. Work was anchored by foundational profiling scripts and problem understanding documents.
2. **Week 5 Phase: Descriptive Analytics & Data Wrangling**
   * *Mandate:* Enforce cleaning rules, bin variables, and map visual trend profiles.
   * *Naming Logic:* Operational reports shifted to formal Markdown (`.md`) files to support complex data tables and exploratory insight summaries.
3. **Week 6 Phase: Feature Engineering & Pipeline Integration**
   * *Mandate:* Compute custom structural flags and integrate code modules into shared architectures.
4. **Week 7 Phase: System Testing, Refinement, & Handshake Validation**
   * *Mandate:* Stress-test local interfaces against raw row counts and calculate cross-track alignment variances.

---

## 🗂️ Complete Directory Mapping Manual (Excruciating Detail)

### 📂 Root Directory Architecture Elements
*   **`/app.py`** (✨ Week 7 Addition): Active interactive Python application running on Streamlit and Plotly. Connected directly to live data frames to serve as the master Week 7 testing terminal.
*   **`/requirements.txt`** (✨ Week 7 Addition): Portability infrastructure layer locking required module versions for cross-device deployment stability.
*   **`/README.md`** (✨ Week 7 Overhaul): The repository landing manual, updated to provide external reviewers with immediate onboarding context.
*   **`/healthconnect_analysis.ipynb`** (Progressive File): Master historical Jupyter Notebook tracking all sequential code sandboxing layers since Week 4.

### 📂 System Source Logic (`/src/`)
*   **`src/verify_data.py`** (Week 6 Asset): Operational feature testing script engineered to automatically validate data file schema boundaries.

### 📂 Workspace Data Ingestion Layer (`/data/`)
*   **`data/HealthConnect_Appointment_Data.csv`** (Week 4 Source): Raw, unedited clinic cohort database containing 5,000 anonymized transactional logs.
*   **`data/HealthConnect_Data_Dictionary.xlsx`** (Week 4 Source): Master reference matrix mapping out target column classifications and variables.
*   **`data/HealthConnect_Cleaned_Data_Week5.csv`** (Week 5 Overhaul): Deeply scrubbed master dataset file used as the mathematical foundation for all subsequent weeks.

### 📂 Historical Documentation Archive (`/documentation/`)
*   **`documentation/REPOSITORY_ROADMAPPING_GUIDE.md`** (✨ Week 7 Addition): *This file.* Explains structural naming pattern shifts to graders.
*   **`documentation/CROSS_TRACK_HANDOFF.txt`** (✨ Week 7 Overhaul): Outlines the **Test ➔ Finding ➔ Fix ➔ Retest** interaction loop that successfully balanced our analytics aggregates with the ML Engineering track.
*   **`documentation/WEEK_7_PROJECT_SUMMARY.md`** (✨ Week 7 Addition): Detailed executive report tracking Week 7 boundary metrics, float rounding corrections, and final deployment status.
*   **`documentation/healthconnect_decision_support_canvas.html`** (Week 6 Asset): Highly visual browser interface mockup built during Week 6 prototyping.
*   **`documentation/WEEK_6_PROJECT_SUMMARY.txt`** (Week 6 Asset): Plaintext context statement summarising Week 6 analytical script modifications.
*   **`documentation/WEEK_6_ANALYTICS_REPORT.md`** (Week 6 Asset): Technical analysis detailing newly engineered column variables.
*   **`documentation/WEEK_5_ANALYTICS_REPORT.md`** (Week 5 Asset): Exploratory report mapping out travel distance, notification channel, and scheduling lag insights.
*   **`documentation/Initial_Analysis_Document.txt`** (Week 4 Asset): Foundational kickoff document logging missing data counts and raw database quality flaws before cleaning.
*   **`documentation/Week_4_Project_Summary.txt`** (Week 4 Asset): Plaintext milestone report documenting Week 4 execution maps.
*   **`documentation/distance_barrier_chart.png`** (Week 5 Visual): Geographic proximity chart proving distance limits affect clinic attendance.
*   **`documentation/lead_time_attrition_chart.png`** (Week 5 Visual): Temporal chart tracing show-rate drops against advance booking windows.
*   **`documentation/reminder_effectiveness_chart.png`** (Week 5 Visual): Outreach chart mapping final conversion yield variations across text alerts.
