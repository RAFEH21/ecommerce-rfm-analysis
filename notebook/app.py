import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# 1. Page Configuration
st.set_page_config(page_title="Olist Customer Analysis", layout="wide", initial_sidebar_state="expanded")

# 2. Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 12px; border: 1px solid #3b82f6; }
    h1, h2, h3 { color: #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

# 3. Data Loading
@st.cache_data
def load_data():
    if os.path.exists('rfm_data.csv'):
        df = pd.read_csv('rfm_data.csv')
    else:
        df = pd.read_csv('notebook/rfm_data.csv')
    return df

# 4. Try block start
try:
    rfm = load_data()

    # Sidebar
    logo_path = "https://raw.githubusercontent.com/RaoMueez/ecommerce_rfm_analysis/main/visual_insights/ss(2).png"
    st.sidebar.image(logo_path, use_container_width=True)
    st.sidebar.title("Filters")
    segments = st.sidebar.multiselect("Select Segments:", options=sorted(rfm['Segment'].unique()), default=rfm['Segment'].unique())

    filtered_df = rfm[rfm['Segment'].isin(segments)]

    # Main Header
    st.title("🛍️ Olist E-commerce Customer Segmentation")
    st.markdown("Interactive Dashboard for RFM Analysis")
    st.divider()

    # KPI Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Customers", f"{len(filtered_df):,}")
    m2.metric("Avg Recency", f"{int(filtered_df['Recency'].mean())} Days")
    m3.metric("Avg Frequency", f"{filtered_df['Frequency'].mean():.2f}")
    m4.metric("Total Revenue", f"R$ {filtered_df['Monetary'].sum():,.0f}")

    # Charts
    row1_col1, row1_col2 = st.columns([1.2, 1])
    with row1_col1:
        fig_bar = px.bar(filtered_df['Segment'].value_counts().reset_index(), x='Segment', y='count', color='Segment', template="plotly_dark")
        st.plotly_chart(fig_bar, use_container_width=True)
    with row1_col2:
        fig_pie = px.pie(filtered_df, names='Segment', values='Monetary', hole=0.5, template="plotly_dark")
        st.plotly_chart(fig_pie, use_container_width=True)

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        fig_scatter = px.scatter(filtered_df, x="Recency", y="Monetary", color="Segment", size="Monetary", log_y=True, template="plotly_dark")
        st.plotly_chart(fig_scatter, use_container_width=True)
    with row2_col2:
        st.dataframe(filtered_df[['customer_unique_id', 'Recency', 'Frequency', 'Monetary', 'Segment']].head(50), use_container_width=True, hide_index=True)

except FileNotFoundError:
    st.error("Error: 'rfm_data.csv' not found.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")