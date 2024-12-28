import streamlit as st
import json
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime

# Function to fetch test results from a remote URL (like GitHub)
def get_test_results():
    url = "https://raw.githubusercontent.com/Smith-S-S/test_script_cicd/main/test_results.json"  # Change URL to your raw GitHub link
    response = requests.get(url)
    
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        st.error(f"Failed to fetch test results. Status code: {response.status_code}")
        return pd.DataFrame()

def main():
    st.title("Test Results Dashboard")
    
    df = get_test_results()  # Use the get_test_results function to fetch the data
    
    if df.empty:
        st.warning("No test results found")
        return
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Overall stats
    col1, col2, col3 = st.columns(3)
    with col1:
        total_tests = len(df)
        st.metric("Total Tests Run", total_tests)
    
    with col2:
        pass_rate = (df['status'] == 'PASS').mean() * 100
        st.metric("Pass Rate", f"{pass_rate:.1f}%")
    
    with col3:
        avg_duration = df['duration'].mean()
        st.metric("Avg Duration", f"{avg_duration:.2f}s")
    
    # Test results over time
    st.subheader("Test Results Over Time")
    fig = px.scatter(df, x='timestamp', y='duration', color='status',
                    hover_data=['test_name', 'error_message'])
    st.plotly_chart(fig)
    
    # Test results by test name
    st.subheader("Results by Test Name")
    test_summary = df.groupby('test_name')['status'].value_counts().unstack()
    fig2 = px.bar(test_summary, barmode='group')
    st.plotly_chart(fig2)
    
    # Recent failures
    st.subheader("Recent Failures")
    failures = df[df['status'] == 'FAIL'].sort_values('timestamp', ascending=False)
    if not failures.empty:
        st.dataframe(failures[['timestamp', 'test_name', 'error_message', 'duration']])
    else:
        st.success("No recent failures!")

if __name__ == "__main__":
    main()
