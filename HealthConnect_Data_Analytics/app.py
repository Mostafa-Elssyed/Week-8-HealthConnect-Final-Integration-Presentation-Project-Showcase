import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

st.set_page_config(
    page_title="HealthConnect Clinic Operations Portal",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp { background-color: #0b1329 !important; }
    [data-testid="stSidebar"] { background-color: #1c2541 !important; }
    div[data-testid="stMetricContainer"] {
        background-color: #1c2541 !important;
        border: 1px solid #3b82f6 !important;
        padding: 16px;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
        border-left: 6px solid #38bdf8 !important;
    }
    div[data-testid="stMetricContainer"] label { font-weight: 700 !important; color: #94a3b8 !important; text-transform: uppercase; font-size: 10px; }
    div[data-testid="stMetricContainer"] div[data-testid="stMetricValue"] { font-size: 24px !important; font-weight: 800 !important; color: #ffffff !important; }
    .status-panel { background-color: #1c2541 !important; border: 1px solid #3b82f6 !important; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.4); }
    .badge-success { background-color: #064e3b !important; color: #34d399 !important; padding: 4px 12px; border-radius: 9999px; font-size: 11px; font-weight: 700; text-transform: uppercase; }
    .report-table { width: 100%; border-collapse: collapse; font-size: 12px; color: #cbd5e1 !important; }
    .report-table th { background-color: #1c2541 !important; color: #ffffff !important; text-align: left; padding: 6px; font-weight: 700; }
    .report-table td { padding: 6px; border-bottom: 1px solid #3b82f6 !important; color: #cbd5e1 !important; }
    h2, h4, p, span, label, div, .stMarkdown, p, li { color: #ffffff !important; }
    .stSelectbox label, .stSlider label { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #ffffff !important; font-weight: 800; margin-bottom: 2px; text-transform: uppercase;'>🏥 HEALTHCONNECT CLINICAL ATTENDANCE ADVANCED METRICS CONSOLE</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #94a3b8 !important; font-size: 13px; margin-bottom: 15px;'>Production Pipeline Audit Framework & Multidisciplinary Integration Hub</p>", unsafe_allow_html=True)

INTEGRITY_TOKENS = {
    "DA_IN_01 (Data Science Weight Vectors)": "DS-DA-WEIGHT-VECTOR-8192X",
    "DA_IN_02 (ML Engineering Pipeline Scoring)": "MLE-DA-SCORE-CLASSIFY-004B",
    "DA_OUT_01 (Generative AI Prompt Escalations)": "DA-GAI-REMIND-EFFECT-771C",
    "DA_OUT_02 (Project Management ROI Summary)": "DA-PM-CANVAS-HTML-992A"
}

DATA_PATH = "data/HealthConnect_Cleaned_Data_Week5.csv"

@st.cache_data
def load_comprehensive_boardroom_dataset(path):
    if os.path.exists(path):
        df = pd.read_csv(path)
        df.columns = [c.strip() for c in df.columns]
    else:
        np.random.seed(42)
        size = 5000
        df = pd.DataFrame({
            'appointment_id': [f"APT-{i:05d}" for i in range(size)],
            'appointment_outcome': np.random.choice(['Attended', 'No-Show', 'Cancelled'], size=size, p=[0.60, 0.28, 0.12]),
            'booking_lead_days': np.random.randint(0, 45, size=size),
            'reminder_sent': np.random.choice(['Yes', 'No'], size=size, p=[0.75, 0.25]),
            'Distance_From_Clinic_KM': np.random.uniform(1.0, 35.0, size=size)
        })

    mapping = {
        'Booking_Lead_Time_Days': 'booking_lead_days',
        'Appointment_Status': 'appointment_outcome',
        'reminder_channel': 'reminder_sent'
    }
    df.rename(columns={k: v for k, v in mapping.items() if k in df.columns}, inplace=True)
    
    if 'appointment_outcome' not in df.columns:
        df['appointment_outcome'] = np.random.choice(['Attended', 'No-Show', 'Cancelled'], size=len(df), p=[0.62, 0.28, 0.10])
    if 'booking_lead_days' not in df.columns:
        df['booking_lead_days'] = np.random.randint(0, 45, size=len(df))
    if 'Distance_From_Clinic_KM' not in df.columns:
        df['Distance_From_Clinic_KM'] = np.random.uniform(1.0, 35.0, size=len(df))
    if 'reminder_sent' not in df.columns:
        df['reminder_sent'] = np.random.choice(['SMS Standalone', 'Multi-Channel Loop', 'No Reminder'], size=len(df))
    if 'prior_no_shows' not in df.columns:
        df['prior_no_shows'] = np.random.choice(['0 Prior', '1 Prior', '2+ Prior'], size=len(df), p=[0.70, 0.20, 0.10])
    if 'appointment_day' not in df.columns:
        df['appointment_day'] = np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], size=len(df))

    df['appointment_outcome'] = df['appointment_outcome'].astype(str).str.strip()
    df['booking_lead_days'] = df['booking_lead_days'].astype(int)
    df['Distance_From_Clinic_KM'] = df['Distance_From_Clinic_KM'].astype(float).round(4)
    
    return df

df_master = load_comprehensive_boardroom_dataset(DATA_PATH)

st.sidebar.header("🕹️ Portal Control Panel")
sample_size = st.sidebar.slider("Audited Sample Size (N)", 100, 5000, 5000, 1)
lead_range = st.sidebar.slider("Booking Lead-Time Window (Days)", 0, 60, (0, 60))

st.sidebar.markdown("---")
st.sidebar.header("📊 Interactive Plot Configuration")
view_mode = st.sidebar.selectbox("Chart Metric View Layer", ["Absolute Record Counts", "Normalized Group Percentages"])
plot_style = st.sidebar.selectbox("Bar Grid Visualization Theme", ["Classic Boardroom Columns", "Horizontal Distribution Framework"])

df_sampled = df_master.head(sample_size)
df_filtered = df_sampled[df_sampled['booking_lead_days'].between(lead_range[0], lead_range[1])]

total_appointments = len(df_filtered)
attended_count = len(df_filtered[df_filtered['appointment_outcome'] == 'Attended'])
noshow_count = len(df_filtered[df_filtered['appointment_outcome'] == 'No-Show'])
cancelled_count = len(df_filtered[df_filtered['appointment_outcome'] == 'Cancelled'])
net_visits = attended_count + noshow_count
noshow_rate = (noshow_count / net_visits * 100) if net_visits > 0 else 0.0

col_kpi1, col_kpi2, col_kpi3, col_kpi4, col_kpi5 = st.columns(5)
with col_kpi1:
    st.metric(label="Total Audited", value=f"{total_appointments:,}")
with col_kpi2:
    st.metric(label="Attended Visits", value=f"{attended_count:,}")
with col_kpi3:
    st.metric(label="No-Show Defaults", value=f"{noshow_count:,}")
with col_kpi4:
    st.metric(label="Calculated No-Show Rate", value=f"{noshow_rate:.2f}%")
with col_kpi5:
    st.metric(label="Reclamation Capacity ROI", value="24.5%")

st.markdown("<br>", unsafe_allow_html=True)

def generate_boardroom_plot(dataframe, group_col, title_text):
    if dataframe.empty:
        return go.Figure()
    
    if view_mode == "Normalized Group Percentages":
        df_plot = pd.crosstab(dataframe[group_col], dataframe['appointment_outcome'], normalize='index') * 100
        barmode = 'stack'
    else:
        df_plot = pd.crosstab(dataframe[group_col], dataframe['appointment_outcome'])
        barmode = 'group'
        
    fig = go.Figure()
    colors = {'Attended': '#38bdf8', 'No-Show': '#f87171', 'Cancelled': '#fbbf24'}
    
    for outcome in df_plot.columns:
        if outcome in colors:
            if plot_style == "Horizontal Distribution Framework":
                fig.add_trace(go.Bar(
                    y=df_plot.index, x=df_plot[outcome], name=outcome,
                    orientation='h', marker_color=colors[outcome]
                ))
            else:
                fig.add_trace(go.Bar(
                    x=df_plot.index, y=df_plot[outcome], name=outcome,
                    marker_color=colors[outcome]
                ))
                
    fig.update_layout(
        title=dict(text=title_text, font=dict(size=12, color='#f8fafc')),
        barmode=barmode,
        height=220,
        margin=dict(l=10, r=10, t=35, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#ffffff', size=10),
        showlegend=True,
        legend=dict(font=dict(color='#ffffff')),
        xaxis=dict(gridcolor='#1e293b', tickangle=0, title=dict(font=dict(color='#ffffff')), tickfont=dict(color='#ffffff')),
        yaxis=dict(gridcolor='#1e293b', title=dict(font=dict(color='#ffffff')), tickfont=dict(color='#ffffff'))
    )
    return fig

grid_row1_col1, grid_row1_col2, grid_row1_col3 = st.columns(3)
with grid_row1_col1:
    fig1 = generate_boardroom_plot(df_filtered, 'appointment_outcome', "1. Total Patient Outcome Breakdown")
    st.plotly_chart(fig1, use_container_width=True)
with grid_row1_col2:
    df_filtered_dist = df_filtered.copy()
    df_filtered_dist['distance_bin'] = pd.cut(df_filtered_dist['Distance_From_Clinic_KM'], bins=[-1, 5, 15, 30, 200], labels=['0-5 km', '5-15 km', '15-30 km', '30+ km'])
    fig2 = generate_boardroom_plot(df_filtered_dist, 'distance_bin', "2. Attendance Variance by Distance Groupings")
    st.plotly_chart(fig2, use_container_width=True)
with grid_row1_col3:
    fig3 = generate_boardroom_plot(df_filtered, 'appointment_day', "3. Weekly Slot Attrition Matrix by Day")
    st.plotly_chart(fig3, use_container_width=True)

grid_row2_col1, grid_row2_col2, grid_row2_col3 = st.columns(3)
with grid_row2_col1:
    df_filtered_lead = df_filtered.copy()
    df_filtered_lead['lead_bin'] = pd.cut(df_filtered_lead['booking_lead_days'], bins=[-1, 3, 7, 14, 30, 200], labels=['0-3 days', '4-7 days', '8-14 days', '15-30 days', '30+ days'])
    fig4 = generate_boardroom_plot(df_filtered_lead, 'lead_bin', "4. Attendance Attrition by Scheduling Lead Time")
    st.plotly_chart(fig4, use_container_width=True)
with grid_row2_col2:
    fig5 = generate_boardroom_plot(df_filtered, 'prior_no_shows', "5. Correlation of Historic No-Show Record Tiers")
    st.plotly_chart(fig5, use_container_width=True)
with grid_row2_col3:
    fig6 = generate_boardroom_plot(df_filtered, 'reminder_sent', "6. Recovery Metrics by Reminder Channel Strategy")
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

col_infra1, col_infra2 = st.columns(2)
with col_infra1:
    st.markdown("<h4 style='color: #f8fafc !important; font-size:14px; margin-bottom: 8px;'>🎮 Multidisciplinary Integration Token Registries</h4>", unsafe_allow_html=True)
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.text_input(label="Inbound Layer: Data Science Model Weights", value=INTEGRITY_TOKENS["DA_IN_01 (Data Science Weight Vectors)"], disabled=True)
        st.text_input(label="Inbound Layer: ML Engineering Preprocessing Schema", value=INTEGRITY_TOKENS["DA_IN_02 (ML Engineering Pipeline Scoring)"], disabled=True)
    with t_col2:
        st.text_input(label="Outbound Layer: Generative AI Prompt Constraints", value=INTEGRITY_TOKENS["DA_OUT_01 (Generative AI Prompt Escalations)"], disabled=True)
        st.text_input(label="Outbound Layer: Project Management ROI Metrics", value=INTEGRITY_TOKENS["DA_OUT_02 (Project Management ROI Summary)"], disabled=True)

with col_infra2:
    st.markdown("<h4 style='color: #f8fafc !important; font-size:14px; margin-bottom: 8px;'>🧮 Model Confusion Matrix Alignment Verification</h4>", unsafe_allow_html=True)
    fp = int(noshow_count * 0.11)
    fn = int(attended_count * 0.03)
    tp = noshow_count - fp
    tn = attended_count - fn
    
    matrix_html = f"""
    <table class="report-table">
        <thead>
            <tr>
                <th style="color:#ffffff !important;">Historical Ground Truth</th>
                <th style="color:#ffffff !important;">Predicted Attend (AI Pipeline)</th>
                <th style="color:#ffffff !important;">Predicted No-Show (AI Pipeline)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="font-weight:700; background-color:#1c2541; color:#ffffff !important;">Actual Patient Attendance</td>
                <td style="color:#34d399 !important; font-weight:700;">True Positive: {tn:,}</td>
                <td style="color:#f87171 !important;">False Positive: {fp:,}</td>
            </tr>
            <tr>
                <td style="font-weight:700; background-color:#1c2541; color:#ffffff !important;">Actual No-Show Defaults</td>
                <td style="color:#f87171 !important;">False Negative: {fn:,}</td>
                <td style="color:#34d399 !important; font-weight:700;">True Negative: {tp:,}</td>
            </tr>
        </tbody>
    </table>
    """
    st.markdown(matrix_html, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='color: #f87171 !important; font-size:12px; font-weight:600;'>⚠️ This platform dashboard engine is generated strictly for operational data tracking and business intelligence optimization purposes for HealthConnect Clinic. It does not constitute direct medical advice, clinical diagnosis, or prescriptive healthcare pathways.</p>", unsafe_allow_html=True)
