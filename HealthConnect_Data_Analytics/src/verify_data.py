import pandas as pd
import numpy as np

# Absolute relative path check
file_path = "data/HealthConnect_Appointment_Data.csv"

try:
    df = pd.read_csv(file_path)
    print("==================================================")
    print("📋 HEALTHCONNECT DATA ACCURACY AUDIT REPORT")
    print("==================================================")
    
    # 1. Structural Verification
    print(f"✅ Ingestion Check: Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
    
    # 2. Variable Name Audit
    required_columns = ['reminder_channel', 'distance_to_clinic_km', 'waiting_time_minutes', 'appointment_outcome', 'previous_no_shows']
    missing_cols = [col for col in required_columns if col not in df.columns]
    print(f"📋 Missing Schema Columns: {missing_cols if missing_cols else 'None. Schema names match perfectly.'}")

    # 3. Structural Logic Audit (The No-Show Wait Time Bug)
    invalid_logistics = df[(df['appointment_outcome'].isin(['No-Show', 'Cancelled'])) & (df['waiting_time_minutes'] > 0)].shape[0]
    print("--------------------------------------------------")
    print(f"⚠️ Logical Anomalies Found: {invalid_logistics} records")
    if invalid_logistics > 0:
        print("   -> ALERT: 'No-Show' or 'Cancelled' patients have active wait times recorded!")
        print("   -> IMPACT: If you don't isolate these next week, your AIWD KPI will be inaccurate.")
    
    # 4. Reminder Tracking Audit
    mismatched_reminders = df[(df['reminder_sent'] == 'No') & (df['reminder_channel'].notnull()) & (df['reminder_channel'] != 'None')].shape[0]
    print(f"⚠️ Mismatched Reminder Channel Flags: {mismatched_reminders}")
    if mismatched_reminders > 0:
        print("   -> ALERT: Found records marked as 'No reminder sent' but they have a channel listed.")
    else:
        print("   -> OK: Missing reminder channels match unsent notifications correctly.")

    print("==================================================")

except FileNotFoundError:
    print("❌ CRITICAL ACCURACY ALERT: Dataset file not found.")
    print("   -> Ensure you run this from the parent folder path directory.")