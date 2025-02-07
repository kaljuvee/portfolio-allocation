import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

def generate_performance_data(start_date, periods=36, seed=42):
    """Generate mock performance data for fund and index"""
    np.random.seed(seed)
    
    # Generate monthly dates
    dates = pd.date_range(start=start_date, periods=periods, freq='M')
    
    # Generate random returns with some correlation
    index_returns = np.random.normal(0.005, 0.02, periods)  # mean 0.5%, std 2%
    fund_returns = index_returns + np.random.normal(0.002, 0.01, periods)  # slightly higher returns
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Fund': fund_returns,
        'Index': index_returns
    })
    
    return df

def plot_performance_comparison(df):
    """Create a bar chart comparing fund vs index performance"""
    fig = go.Figure()
    
    # Add Fund performance bars
    fig.add_trace(go.Bar(
        x=df['Date'],
        y=df['Fund'] * 100,  # Convert to percentage
        name='Fund',
        marker_color='rgb(26, 118, 255)'
    ))
    
    # Add Index performance bars
    fig.add_trace(go.Bar(
        x=df['Date'],
        y=df['Index'] * 100,  # Convert to percentage
        name='Index',
        marker_color='rgb(58, 200, 225)'
    ))
    
    # Update layout
    fig.update_layout(
        title='Fund vs Index Performance',
        yaxis_title='Monthly Return (%)',
        barmode='group',
        height=600,
        showlegend=True,
        plot_bgcolor='white',
        yaxis=dict(
            gridcolor='lightgrey',
            zerolinecolor='lightgrey',
            tickformat='.1f',
            ticksuffix='%'
        ),
        xaxis=dict(
            gridcolor='lightgrey',
            tickangle=45
        )
    )
    
    return fig

# Page title
st.title("Index Performance")

# Sidebar controls
st.sidebar.header("Settings")

# Date range selector
start_date = st.sidebar.date_input(
    "Select Start Date",
    value=datetime.now() - timedelta(days=3*365),  # 3 years ago
    max_value=datetime.now()
)

# Generate data
df = generate_performance_data(start_date)

# Display the chart
fig = plot_performance_comparison(df)
st.plotly_chart(fig, use_container_width=True)

# Optional: Display the data
if st.checkbox("Show raw data"):
    st.dataframe(df)
