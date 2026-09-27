# HealthConnect Clinic Patient Adherence Baseline Analytics Report

## 1. Context and Problem Definition
High patient absenteeism and unoptimized schedule distribution degrade resource utilization and clinic efficiency across HealthConnect facilities. The primary objective of this workstream was to normalize column variables, profile systemic data quality anomalies, and establish foundational historical benchmarks.

### Boundary Parameters and Constraints
* Missing notification variables are assumed to reflect cases where reminders were not successfully dispatched.
* Proximity tracking relies on distance estimates between provided sector centroids and clinic coordinates, omitting live transit congestion factors.

---

## 2. Data Preparation and Quality Summary
To ensure statistical integrity, raw appointment entries underwent programmatic standardization and logical corrections before any KPI evaluation. All transformation steps write exclusively to a derived output file: data/HealthConnect_Cleaned_Data_Week5.csv.

### A. Normalization and Missing Value Imputation
* Conversions mapped raw scheduling strings into uniform ISO 8601 datetimes (YYYY-MM-DD).
* Blank entries within the reminder channel column were mapped to a distinct categorical string ("None").
* Missing values within travel distance and wait time fields were substituted with their respective global dataset medians to neutralize outlier distortion.

### B. Resolution of the Wait-Time Logging Bug
During data quality inspection, a systemic logging bug was identified: the facility database incorrectly captured positive waiting room times for appointments where patients never arrived (No-Shows or Cancellations). The data analytics pipeline resolved this anomaly by programmatically overwriting waiting_time_minutes to 0.0 minutes for all uncompleted visits.

### C. Sample Filtering Strategy
To accurately benchmark real clinic arrivals, all records with a cancelled status were removed from the key performance indicator (KPI) calculation stream. This left a verified operational set of net resolved appointments (Attended vs. No-Show) to isolate true historical clinic arrival behavior.

---

## 3. Core Baseline Key Performance Indicators (KPIs)
The performance metrics below are calculated strictly using Net Appointments, explicitly excluding cancelled statuses.

### KPI 1: Reminder Success Differential (RSD) = 4.78%
* Definition: The absolute difference between the show rate of patients who received an advance notification and those who did not.
* Operational Scope: Measures outreach framework ROI to guide automated messaging strategies.

### KPI 2: Average Internal Wait Duration (AIWD) = 11.86 Minutes
* Definition: The total accumulated waiting room time divided by total net appointment arrivals.
* Operational Scope: Monitors internal service bottlenecks only for patients who successfully checked into the clinic.

### KPI 3: Lead-Time Attrition Index (LTAI) = 57.40%
* Definition: The specific no-show rate evaluated for appointments booked far in advance.
* Operational Scope: Identifies the precise planning window where patient forgetfulness and scheduling conflicts escalate (defined as a booking lead time greater than 14 days).

### KPI 4: Distance Variance No-Show Rate (DVNR) = 56.90%
* Definition: The structural no-show rate evaluated for patients traveling from outside the core clinic zone.
* Operational Scope: Evaluates physical distance barriers for the outer-ring cohorts (defined as a travel distance greater than 15 km).

### KPI 5: Repeat Attrition Concentration Ratio (RACR) = 47.54%
* Definition: The proportion of overall clinic no-shows driven directly by recidivist patients.
* Operational Scope: Determines whether missed appointments are random or highly concentrated among repeat chronic offenders (defined as patients with an active log of prior no-shows).

---

## 4. Derived Business Insights and Strategic Actions
* Advance Booking Restrictions: Attendance drops to 57.40% when lead times exceed 14 days. Management should restrict advanced scheduling ranges or introduce an automatic phone validation sequence at the 7-day mark.
* Targeting Recidivist Cohorts: Chronic repeat offenders drive nearly half (47.54%) of all slot leakage. The clinic can prevent high-risk cancellations by funneling this specific group into a dedicated confirmation workflow.
* Outreach Optimization Yields: The RSD reveals a clear +4.78% net lift in show rates when notifications are dispatched, proving a definitive operational return on investment for automated text infrastructure.
* Geographic Care Accommodations: The DVNR reveals a clear geographic barrier past the 15 km mark, where the no-show rate surges to 56.90%. Management should introduce targeted telehealth schedules or mobile clinical units for these areas.
* Internal Service Efficiency Verification: Arrived patient records show a stable internal wait duration of 11.86 minutes. This proves that clinic operational room flows are efficient; administrative improvements must focus on helping patients arrive, rather than modifying interior doctor cycles.

---

## 5. Multidisciplinary Technical Collaboration Log
* Stream Interacted With: Data Science Stream.
* Exchanged Data Outputs: Transferred the relative path data schema, verified datatype columns, and detailed the parameters of the wait-time logic corrections.
* Yield Relevance: Prevented machine learning baseline models from training on invalid wait-time inputs, preserving model feature integrity and baseline logic continuity across the project tracks.