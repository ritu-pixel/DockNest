import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

def run_training():
    if 'df' not in st.session_state or st.session_state.df is None:
        st.warning("Please upload data first from the Data Upload page")
        return
    
    st.header("Model Training")
    
    df = st.session_state.df
    
    # Feature selection
    st.subheader("Feature Selection")
    target = st.selectbox("Select Target Column", df.columns)
    
    features = st.multiselect("Select Features", 
                            [col for col in df.columns if col != target],
                            default=[col for col in df.columns if col != target])
    
    if not features:
        st.error("Please select at least one feature")
        return
    
    # Model parameters
    st.subheader("Model Parameters")
    n_estimators = st.slider("Number of trees", 10, 200, 100)
    max_depth = st.slider("Max depth", 2, 20, 5)
    
    if st.button("Train Model"):
        try:
            # Prepare data
            X = df[features]
            y = df[target]
            
            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42)
            
            # Train model
            model = RandomForestClassifier(
                n_estimators=n_estimators,
                max_depth=max_depth,
                random_state=42)
            
            model.fit(X_train, y_train)
            
            # Evaluate
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            # Save to session state
            st.session_state.model = model
            st.session_state.X_test = X_test
            st.session_state.y_test = y_test
            
            # Display results
            st.success(f"Model trained with accuracy: {accuracy:.2f}")
            st.subheader("Classification Report")
            st.text(classification_report(y_test, y_pred))
            
            # Feature importance
            st.subheader("Feature Importance")
            importance = pd.DataFrame({
                'Feature': features,
                'Importance': model.feature_importances_
            }).sort_values('Importance', ascending=False)
            
            fig, ax = plt.subplots()
            ax.barh(importance['Feature'], importance['Importance'])
            ax.set_xlabel('Importance')
            st.pyplot(fig)
            
        except Exception as e:
            st.error(f"Error during training: {str(e)}")