import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

def run_etl():
    if 'df' not in st.session_state or st.session_state.df is None:
        st.warning("Please upload data first from the Data Upload page")
        return
    
    st.header("ETL Process")
    
    # Access the dataset from session state
    df = st.session_state.df
    
    # Basic transformations (customize these)
    st.subheader("Data Transformations")
    
    # Example: Show missing values
    st.write("Missing Values:")
    st.write(df.isna().sum())
    
    # Example transformation - normalization
    if st.checkbox("Normalize numeric columns"):
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std()
        st.session_state.df = df  # Update session state
        st.success("Data normalized!")
    
    # Visualization
    st.subheader("Data Visualization")
    viz_type = st.selectbox("Select visualization type", 
                          ["Histogram", "Scatter Plot", "Correlation Heatmap"])
    
    if viz_type == "Histogram":
        column = st.selectbox("Select column", df.columns)
        fig, ax = plt.subplots()
        ax.hist(df[column].dropna(), bins=20)
        st.pyplot(fig)
    
    elif viz_type == "Scatter Plot":
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("X-axis", df.columns)
        with col2:
            y_axis = st.selectbox("Y-axis", df.columns)
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis])
        st.pyplot(fig)
    
    elif viz_type == "Correlation Heatmap":
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        if not numeric_df.empty:
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(numeric_df.corr(), annot=True, ax=ax)
            st.pyplot(fig)