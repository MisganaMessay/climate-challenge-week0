import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page configuration
st.set_page_config(page_title="EthioClimate Analytics Dashboard", layout="wide")

st.title("🌍 African Climate Trend Dashboard (COP32)")
st.markdown("### Decision-Support Tool for the Ethiopian Ministry of Planning and Development")

# 1. Data Loading Function
@st.cache_data
def load_all_cleaned_data():
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    data_list = []
    for c in countries:
        file_path = f"data/{c}_clean.csv"
        if os.path.exists(file_path):
            temp_df = pd.read_csv(file_path)
            temp_df['Country'] = c.capitalize()
            temp_df['Date'] = pd.to_datetime(temp_df['Date'])
            data_list.append(temp_df)
    
    if not data_list:
        return pd.DataFrame()
    return pd.concat(data_list, ignore_index=True)

df = load_all_cleaned_data()

if df.empty:
    st.error("Error: No cleaned data found in the 'data/' folder. Please run your notebooks first!")
else:
    # 2. Sidebar Filters (The Interactivity)
    st.sidebar.header("Dashboard Filters")
    
    # Country Selector
    selected_countries = st.sidebar.multiselect(
        "Select Countries to Compare", 
        options=df['Country'].unique(), 
        default=df['Country'].unique()
    )
    
    # Year Range Slider
    min_year = int(df['Date'].dt.year.min())
    max_year = int(df['Date'].dt.year.max())
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

    # Apply Filters
    mask = (df['Country'].isin(selected_countries)) & \
           (df['Date'].dt.year.between(year_range[0], year_range[1]))
    filtered_df = df[mask]

    # 3. Visualization Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌡️ Temperature Trends")
        # Aggregating to monthly for smoother plotly rendering
        monthly_df = filtered_df.set_index('Date').groupby('Country').resample('ME').agg({'T2M':'mean'}).reset_index()
        fig_temp = px.line(monthly_df, x='Date', y='T2M', color='Country', 
                           title="Monthly Mean Temperature Comparison")
        st.plotly_chart(fig_temp, use_container_width=True)

    with col2:
        st.subheader("🌧️ Precipitation Variability")
        fig_precip = px.box(filtered_df, x='Country', y='PRECTOTCORR', color='Country',
                            title="Daily Rainfall Distribution (Outliers identified)")
        st.plotly_chart(fig_precip, use_container_width=True)

    # 4. Impact Insight Section
    st.divider()
    st.subheader("Strategic Insights for COP32")
    
    selected_stats = filtered_df.groupby('Country')['T2M'].mean().reset_index()
    hottest_country = selected_stats.loc[selected_stats['T2M'].idxmax(), 'Country']
    
    st.info(f"Analysis indicates that **{hottest_country}** is currently experiencing the highest baseline temperature among the selected group for the chosen period.")