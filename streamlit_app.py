import streamlit as st
import sys
from io import StringIO
from score_analysis import compare_two_averages

# Page configuration
st.set_page_config(
    page_title="What Difference Does It Make?",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 What Difference Does It Make?")
st.markdown("""
This application compares the expected distribution of scores (1-5 scale) between two different average ratings.
This shows what the real difference is between these average scores.
""")

st.divider()

# Input section
st.subheader("Inputs")

# Number of respondents input
n_respondents = st.number_input(
    "Number of Respondents",
    min_value=1,
    max_value=100,
    value=10,
    step=1,
    help="Total number of people providing ratings"
)

st.write("")  # Add spacing

# Create three columns for the average score inputs with arrow
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    avg1 = st.number_input(
        "From Average Score",
        min_value=1.0,
        max_value=5.0,
        value=3.0,
        step=0.01,
        format="%.2f",
        help="Starting average score (1.0 to 5.0)"
    )

with col2:
    st.markdown("<div style='text-align: center; padding-top: 30px; font-size: 24px;'>→</div>", 
                unsafe_allow_html=True)

with col3:
    avg2 = st.number_input(
        "To Average Score",
        min_value=1.0,
        max_value=5.0,
        value=3.5,
        step=0.01,
        format="%.2f",
        help="Target average score (1.0 to 5.0)"
    )

st.divider()

# Run analysis button
if st.button("🔍 Quantify the Difference", type="primary", use_container_width=True):
    
    st.subheader("Results")
    
    # Capture the output from the compare_two_averages function
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    try:
        # Call the function
        compare_two_averages(int(n_respondents), avg1, avg2)
        
        # Get the output
        output = captured_output.getvalue()
        
        # Restore stdout
        sys.stdout = old_stdout
        
        # Display the output in a code block for proper formatting
        st.code(output, language=None)
        
    except Exception as e:
        sys.stdout = old_stdout
        st.error(f"An error occurred: {str(e)}")

else:
    # Show instructions when button hasn't been clicked
    st.info("👆 Enter your parameters above and click 'Quantify the Difference' to see results")

# Add footer with additional information
st.divider()
st.markdown("""
### How to interpret the results:
- **Average counts**: Expected number of each score (1-5) across all possible distributions
- **Percentage (%)**: Each count as a percentage of total respondents
- **Difference**: Change in count when moving from first to second average
- **Diff %**: Change expressed as a percentage of total respondents

### Notes:
- Not all averages are possible with a given number of respondents (the sum must be an integer)
- When an average is impossible, the application suggests the closest valid alternatives
- Results are weighted by the number of permutations each distribution can generate
""")
