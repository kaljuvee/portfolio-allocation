import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Portfolio Heatmap", page_icon="🗺️", layout="wide")

# Initialize session state for the dataframe
if 'portfolio_df' not in st.session_state:
    st.session_state.portfolio_df = None

st.title("🗺️ Portfolio Allocation Heatmap")
st.markdown("### Sector and Fund Analysis")

# Step 1: Generate Data Button
if st.button("1️⃣ Generate Sample Data"):
    # Sample data structure
    data = {
        'Sector': [
            # Technology
            'Technology', 'Technology', 'Technology', 'Technology',
            # Financial
            'Financial', 'Financial', 'Financial',
            # Healthcare
            'Healthcare', 'Healthcare', 'Healthcare',
            # Consumer
            'Consumer', 'Consumer', 'Consumer',
            # Energy
            'Energy', 'Energy',
            # Real Estate
            'Real Estate', 'Real Estate'
        ],
        'Fund': [
            # Technology funds
            'Tech Growth ETF', 'Digital Innovation Fund', 'Semiconductor Index', 'Cloud Computing ETF',
            # Financial funds
            'Global Finance ETF', 'Fintech Leaders', 'Banking Index Fund',
            # Healthcare funds
            'Healthcare Innovation', 'Biotech Index', 'Medical Devices ETF',
            # Consumer funds
            'Consumer Staples ETF', 'E-commerce Leaders', 'Retail Index',
            # Energy funds
            'Clean Energy ETF', 'Global Energy Fund',
            # Real Estate funds
            'REIT Index', 'Property Securities'
        ],
        'Market_Value': [
            # Technology values
            2500000, 1800000, 1500000, 1200000,
            # Financial values
            1600000, 1400000, 1100000,
            # Healthcare values
            1900000, 1300000, 1000000,
            # Consumer values
            1400000, 1200000, 900000,
            # Energy values
            1100000, 900000,
            # Real Estate values
            800000, 700000
        ],
        'Daily_Return': [
            # Technology returns
            2.3, -1.5, 1.8, 3.2,
            # Financial returns
            0.8, 1.5, -0.7,
            # Healthcare returns
            -0.5, 2.1, 1.3,
            # Consumer returns
            0.3, 1.7, -0.9,
            # Energy returns
            2.8, -1.2,
            # Real Estate returns
            0.5, -0.8
        ]
    }
    
    st.session_state.portfolio_df = pd.DataFrame(data)
    
    # Calculate total value for percentages
    total_value = st.session_state.portfolio_df['Market_Value'].sum()
    st.session_state.portfolio_df['Percentage'] = st.session_state.portfolio_df['Market_Value'] / total_value * 100
    
    # Display the dataframe with formatted values
    st.markdown("### Generated Portfolio Data")
    formatted_df = st.session_state.portfolio_df.copy()
    formatted_df['Market_Value'] = formatted_df['Market_Value'].apply(lambda x: f"${x:,.0f}")
    formatted_df['Daily_Return'] = formatted_df['Daily_Return'].apply(lambda x: f"{x:.1f}%")
    formatted_df['Percentage'] = formatted_df['Percentage'].apply(lambda x: f"{x:.1f}%")
    st.dataframe(formatted_df, use_container_width=True)

# Step 2: Visualize Data Button
if st.session_state.portfolio_df is not None:
    if st.button("2️⃣ Visualize as Heatmap"):
        # Create figure
        fig = go.Figure(go.Treemap(
            labels=st.session_state.portfolio_df['Fund'],
            parents=st.session_state.portfolio_df['Sector'],
            values=st.session_state.portfolio_df['Market_Value'],
            textinfo="label+percent parent+value",
            texttemplate="<b>%{label}</b><br>%{percentParent:.1f}% of %{parent}<br>$%{value:,.0f}",
            hovertemplate="<b>%{label}</b><br>" +
                         "Sector: %{parent}<br>" +
                         "Value: $%{value:,.0f}<br>" +
                         "Daily Return: %{customdata:.1f}%<br>" +
                         "<extra></extra>",
            customdata=st.session_state.portfolio_df['Daily_Return'],
            marker=dict(
                colors=st.session_state.portfolio_df['Daily_Return'],
                colorscale='RdYlGn',  # Red for negative, Yellow for neutral, Green for positive
                cmid=0  # Set the middle of the color scale to 0
            )
        ))

        # Update layout
        fig.update_layout(
            title={
                'text': "Portfolio Allocation by Sector and Fund<br><sup>Color indicates daily performance</sup>",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            height=700,
        )

        # Display the plot
        st.plotly_chart(fig, use_container_width=True)

        # Add explanation
        st.markdown("""
        ### Understanding the Heatmap

        This treemap visualization shows your portfolio allocation across different sectors and individual funds:

        - **Size of boxes**: Represents the market value of each holding
        - **Color coding**: 
            - 🟢 Green: Positive daily return
            - 🟨 Yellow: Neutral performance
            - 🔴 Red: Negative daily return
        - **Hierarchy**: 
            - First level: Sector allocation
            - Second level: Individual funds within each sector
        """)

# Sidebar controls
st.sidebar.markdown("### Visualization Controls")
view_type = st.sidebar.selectbox(
    "View By",
    ["Market Value", "Daily Return", "Both"]
)

time_period = st.sidebar.selectbox(
    "Time Period",
    ["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"]
)

min_value = st.sidebar.number_input(
    "Minimum Position Size ($)",
    min_value=0,
    max_value=1000000,
    value=500000,
    step=100000
)

st.sidebar.markdown(f"""
### Current View Settings
- Showing positions larger than ${min_value:,.0f}
- Performance over {time_period.lower()} period
- Colored by {view_type.lower()}

*Note: This is sample data for demonstration purposes.*
""") 