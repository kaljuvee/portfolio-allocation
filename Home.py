import streamlit as st

st.set_page_config(
    page_title="Portfolio Allocator",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Portfolio Allocator")
st.markdown("### Understanding Different Portfolio Allocation Strategies")

st.markdown("""
Welcome to Portfolio Allocator! This tool helps you understand and compare different portfolio allocation strategies.

### Common Portfolio Allocation Strategies

#### 1. Strategic Asset Allocation
- Long-term, static mix of assets
- Based on investor's risk tolerance and time horizon
- Regular rebalancing to maintain target allocations

#### 2. Tactical Asset Allocation
- Active portfolio management approach
- Short to medium-term deviations from strategic allocation
- Takes advantage of market opportunities

#### 3. Modern Portfolio Theory (MPT)
- Developed by Harry Markowitz
- Focus on portfolio diversification
- Optimizes expected return vs risk
- Uses correlation between assets

#### 4. Risk Parity
- Allocates based on risk contribution
- Aims to balance risk across asset classes
- Often uses leverage for lower-risk assets

#### 5. Traditional Portfolio Splits
- **60/40 Portfolio**: Classic split between stocks (60%) and bonds (40%)
- **Three-Fund Portfolio**: Domestic stocks, international stocks, and bonds
- **All-Weather Portfolio**: Designed to perform in any economic environment

### Key Considerations for Portfolio Allocation

1. **Risk Tolerance**
   - Conservative
   - Moderate
   - Aggressive

2. **Investment Horizon**
   - Short-term (<3 years)
   - Medium-term (3-10 years)
   - Long-term (>10 years)

3. **Investment Goals**
   - Capital preservation
   - Income generation
   - Capital appreciation
   - Total return

### Benefits of Proper Portfolio Allocation

- Risk management through diversification
- Potential for better risk-adjusted returns
- Alignment with investment goals
- Systematic approach to investing
""")

st.markdown("---")
st.markdown("""
#### Getting Started

Explore different allocation strategies using the sidebar navigation. Each section provides detailed information and interactive tools to help you understand and implement various portfolio allocation approaches.
""") 