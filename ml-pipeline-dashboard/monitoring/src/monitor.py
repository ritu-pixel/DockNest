import streamlit as st
import pandas as pd
from evidently.report import Report
from evidently.metrics import DataDriftTable, DatasetDriftMetric, ClassificationQualityMetric
import matplotlib.pyplot as plt

def run_monitoring():
    if 'df' not in st.session_state or st.session_state.df is None:
        st.warning("Please upload data first from the Data Upload page")
        return
    if 'model' not in st.session_state:
        st.warning("Please train a model first from the Model Training page")
        return
    
    st.header("Data & Model Monitoring")
    
    df = st.session_state.df
    model = st.session_state.model
    
    # Create reference and current data
    st.subheader("Data Drift Analysis")
    ref_size = st.slider("Reference dataset size", 10, len(df)//2, min(100, len(df)//2))
    current_size = st.slider("Current dataset size", 10, len(df)//2, min(100, len(df)//2))
    
    reference_data = df.iloc[:ref_size]
    current_data = df.iloc[ref_size:ref_size+current_size]
    
    # Data Drift Report
    if st.button("Run Data Drift Analysis"):
        data_drift_report = Report(metrics=[
            DataDriftTable(),
            DatasetDriftMetric()
        ])
        
        data_drift_report.run(
            reference_data=reference_data,
            current_data=current_data
        )
        
        st.subheader("Data Drift Results")
        st.write(data_drift_report.as_dict()['metrics'][0]['result']['drift_table'])
        
        # Visualize drift
        drift_metrics = data_drift_report.as_dict()['metrics'][1]['result']
        st.metric("Dataset Drift Score", f"{drift_metrics['dataset_drift']} (Drift detected)" if drift_metrics['dataset_drift'] else "(No drift detected)")
    
    # Model Performance Report
    st.subheader("Model Performance Monitoring")
    if st.button("Run Model Performance Analysis"):
        try:
            X_test = st.session_state.X_test
            y_test = st.session_state.y_test
            y_pred = model.predict(X_test)
            
            performance_report = Report(metrics=[
                ClassificationQualityMetric()
            ])
            
            performance_report.run(
                reference_data=reference_data,
                current_data=current_data
            )
            
            st.write(performance_report.as_dict())
            
        except Exception as e:
            st.error(f"Error in performance analysis: {str(e)}")