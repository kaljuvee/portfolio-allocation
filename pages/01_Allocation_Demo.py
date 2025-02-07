import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pdfkit
import tempfile
from datetime import datetime
import os

# Set page config
st.set_page_config(page_title="Allocation Demo", page_icon="📈", layout="wide")

# Generate sample data
np.random.seed(42)
dates = pd.date_range(start='2018-01-01', end='2023-12-31', freq='M')

# Generate sample returns for different portfolios
conservative_returns = np.random.normal(0.004, 0.02, len(dates))  # Lower return, lower volatility
aggressive_returns = np.random.normal(0.007, 0.04, len(dates))    # Higher return, higher volatility

# Calculate cumulative returns
conservative_cumulative = (1 + conservative_returns).cumprod()
aggressive_cumulative = (1 + aggressive_returns).cumprod()

# Create DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Conservative Portfolio': conservative_cumulative,
    'Aggressive Portfolio': aggressive_cumulative
})

# Create the plot
st.title("📈 Portfolio Growth Comparison")
st.markdown("### Comparing Different Allocation Strategies")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Conservative Portfolio'],
        name='Conservative Portfolio',
        line=dict(color='#1f77b4', width=2),
    )
)

fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Aggressive Portfolio'],
        name='Aggressive Portfolio',
        line=dict(color='#ff7f0e', width=2),
    )
)

# Update layout
fig.update_layout(
    title='Compounded Growth of $1 Investment',
    xaxis_title='Date',
    yaxis_title='Portfolio Value',
    template='plotly_white',
    hovermode='x unified',
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ),
    height=600,
)

# Add range slider
fig.update_xaxes(rangeslider_visible=True)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Add explanation
st.markdown("""
### Understanding the Growth Comparison

This chart demonstrates the growth of two different portfolio allocation strategies:

1. **Conservative Portfolio**
   - Lower volatility
   - More stable growth
   - Typically higher allocation to bonds and stable assets

2. **Aggressive Portfolio**
   - Higher volatility
   - Potential for higher returns
   - Typically higher allocation to stocks and growth assets

The chart shows how an initial $1 investment would have grown over time under each strategy. Notice how:
- The aggressive portfolio shows more dramatic ups and downs
- The conservative portfolio shows more stable, but generally lower growth
- Different strategies may outperform during different market conditions
""")

# Add interactive elements
st.sidebar.markdown("### Portfolio Settings")
risk_level = st.sidebar.slider("Risk Tolerance", 1, 10, 5)
investment_period = st.sidebar.selectbox(
    "Investment Period",
    ["Short-term (1-3 years)", "Medium-term (3-7 years)", "Long-term (7+ years)"]
)

st.sidebar.markdown(f"""
### Current Settings
- Risk Level: {risk_level}/10
- Time Horizon: {investment_period}

*Note: This is a simplified demonstration using simulated data. Actual investment results may vary significantly.*
""")

# Add PDF generation function after the markdown explanation
def generate_pdf():
    # Create a temporary HTML file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.html') as f:
        # Generate HTML content
        html_content = f"""
        <html>
            <head>
                <title>Portfolio Allocation Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    h1 {{ color: #2e4053; }}
                    .date {{ color: #7f8c8d; margin-bottom: 30px; }}
                </style>
            </head>
            <body>
                <h1>Portfolio Allocation Report</h1>
                <div class="date">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
                <h2>Portfolio Settings</h2>
                <ul>
                    <li>Risk Level: {risk_level}/10</li>
                    <li>Investment Period: {investment_period}</li>
                </ul>
                <h2>Understanding the Growth Comparison</h2>
                <h3>Conservative Portfolio</h3>
                <ul>
                    <li>Lower volatility</li>
                    <li>More stable growth</li>
                    <li>Typically higher allocation to bonds and stable assets</li>
                </ul>
                <h3>Aggressive Portfolio</h3>
                <ul>
                    <li>Higher volatility</li>
                    <li>Potential for higher returns</li>
                    <li>Typically higher allocation to stocks and growth assets</li>
                </ul>
            </body>
        </html>
        """
        f.write(html_content.encode('utf-8'))
        html_path = f.name

    # Generate PDF from HTML
    pdf_path = html_path.replace('.html', '.pdf')
    try:
        pdfkit.from_file(html_path, pdf_path)
        with open(pdf_path, 'rb') as pdf_file:
            pdf_data = pdf_file.read()
        # Clean up temporary files
        os.unlink(html_path)
        os.unlink(pdf_path)
        return pdf_data
    except Exception as e:
        st.error(f"Error generating PDF: {str(e)}")
        return None

# Add download button at the bottom of the page
st.markdown("---")
if st.button("Generate and Download PDF Report"):
    pdf_data = generate_pdf()
    if pdf_data:
        st.download_button(
            label="Download PDF Report",
            data=pdf_data,
            file_name=f"portfolio_allocation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf"
        )
