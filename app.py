import streamlit as st
from traffic import generate_traffic

st.title("Zscaler Synthetic Traffic Generator")

st.markdown("Simulate network traffic to test ZIA policies")

use_case = st.selectbox("Select Use Case", [
    "URL Filtering", "SSL Inspection", "App Control", "Threat Prevention", "CASB Trigger", "DLP Violation"
])

num_requests = st.slider("Number of Requests", 1, 50, 10)

if st.button("Generate Traffic"):
    results = generate_traffic(use_case, num_requests)
    st.success("Traffic generation complete!")
    st.write(results)
