"""
Web App for Customer Churn Analysis
A Streamlit app that displays analysis results and visualizations in the browser
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPClassifier
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Customer Churn Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure matplotlib to use non-interactive backend
import matplotlib
matplotlib.use('Agg')

# Custom CSS
st.markdown("""
<style>
    .main {
        padding-top: 0rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("📊 Customer Churn Analysis Dashboard")
st.markdown("Interactive web-based analysis tool for customer churn data")
st.markdown("---")

# Info box
with st.info("📌 **How to use:** Select 'Upload CSV' or 'Upload Excel' in the sidebar, then choose a file from your PC. The dashboard will analyze it automatically!", icon="ℹ️"):
    pass

st.markdown("---")

# Sidebar for data input
st.sidebar.title("📁 Data Input")
st.sidebar.markdown("**Choose how to load your data:**")

# Data loading options
data_source = st.sidebar.radio(
    "Select data source:",
    ["Upload CSV", "Upload Excel", "Sample Data"]
)

df = None
error_msg = None

# Load data based on selection
if data_source == "Upload CSV":
    st.sidebar.markdown("**Upload a CSV file from your computer:**")
    st.sidebar.markdown("*Required: Must contain a 'Churn' column*")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success(f"✓ Loaded: {uploaded_file.name} ({len(df)} rows)")
        except Exception as e:
            error_msg = f"Error reading CSV: {str(e)}"

elif data_source == "Upload Excel":
    st.sidebar.markdown("**Upload an Excel file from your computer:**")
    st.sidebar.markdown("*Required: Must contain a 'Churn' column*")
    uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.sidebar.success(f"✓ Loaded: {uploaded_file.name} ({len(df)} rows)")
        except Exception as e:
            error_msg = f"Error reading Excel: {str(e)}"

elif data_source == "Sample Data":
    st.sidebar.markdown("**Using sample data for demonstration:**")
    sample_files = ['sample_churn_dataset.xlsx', 'sample_churn_dataset.csv']
    sample_found = False
    for sample_file in sample_files:
        if os.path.exists(sample_file):
            try:
                if sample_file.endswith('.xlsx'):
                    df = pd.read_excel(sample_file)
                else:
                    df = pd.read_csv(sample_file)
                st.sidebar.success(f"✓ Loaded: {sample_file}")
                sample_found = True
                break
            except Exception as e:
                error_msg = f"Error loading {sample_file}: {str(e)}"
    
    if not sample_found:
        st.sidebar.warning("⚠️ No sample file found. Please upload your own CSV or Excel file.")

# Display error message if any
if error_msg:
    st.error(error_msg)

# Process data if loaded
if df is not None:
    # Clean column names
    df.columns = df.columns.str.strip()
    
    # Check for Churn column
    if 'Churn' not in df.columns:
        st.error("❌ Error: Dataset must contain a 'Churn' column")
        st.stop()
    
    # Convert TotalCharges to numeric if exists
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
    
    # Drop customerID if present
    if 'customerID' in df.columns:
        df = df.drop(columns=['customerID'])
    
    # ==================== TABS ====================
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "🔍 Analysis", "📊 Visualizations", "🤖 Models"])
    
    # TAB 1: OVERVIEW
    with tab1:
        st.header("Dataset Overview")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Records", len(df))
        with col2:
            st.metric("Total Features", len(df.columns))
        with col3:
            churn_rate = (df['Churn'].value_counts().get('Yes', 0) / len(df) * 100) if 'Yes' in df['Churn'].values else 0
            st.metric("Churn Rate (%)", f"{churn_rate:.1f}%")
        
        st.subheader("First Few Records")
        st.dataframe(df.head(10), use_container_width=True)
        
        st.subheader("Dataset Info")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Columns:**")
            st.write(", ".join(df.columns.tolist()))
        with col2:
            st.write("**Data Types:**")
            st.write(df.dtypes.to_string())
    
    # TAB 2: DATA ANALYSIS
    with tab2:
        st.header("Data Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Male customers
            if 'gender' in df.columns:
                male_count = len(df[df['gender'] == 'Male'])
                st.metric("Male Customers", male_count)
            
            # DSL customers
            if 'InternetService' in df.columns:
                dsl_count = len(df[df['InternetService'] == 'DSL'])
                st.metric("Customers with DSL", dsl_count)
        
        with col2:
            # Female senior citizens
            if all(col in df.columns for col in ['gender', 'SeniorCitizen', 'PaymentMethod']):
                senior_female = len(df[
                    (df['gender'] == 'Female') & 
                    (df['SeniorCitizen'] == 1) & 
                    (df['PaymentMethod'] == 'Mailed check')
                ])
                st.metric("Female Senior Citizens (Mailed Check)", senior_female)
            
            # Low tenure or low charges
            if all(col in df.columns for col in ['tenure', 'TotalCharges']):
                low_tenure_charges = len(df[(df['tenure'] < 10) | (df['TotalCharges'] < 500)])
                st.metric("Tenure<10 or TotalCharges<$500", low_tenure_charges)
        
        # Summary statistics
        st.subheader("Summary Statistics")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        st.dataframe(df[numeric_cols].describe(), use_container_width=True)
    
    # TAB 3: VISUALIZATIONS
    with tab3:
        st.header("Data Visualizations")
        
        col1, col2 = st.columns(2)
        
        # Churn distribution
        with col1:
            st.subheader("Churn Distribution")
            churn_counts = df['Churn'].value_counts()
            fig, ax = plt.subplots(figsize=(6, 5))
            colors = ['#90EE90', '#FF6B6B']
            ax.pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%',
                   colors=colors, startangle=90)
            ax.set_title('Customer Churn Distribution')
            st.pyplot(fig, use_container_width=True)
        
        # Internet Service distribution (if available)
        if 'InternetService' in df.columns:
            with col2:
                st.subheader("Internet Service Distribution")
                internet_counts = df['InternetService'].value_counts()
                fig, ax = plt.subplots(figsize=(6, 5))
                internet_counts.plot(kind='bar', ax=ax, color='steelblue')
                ax.set_title('Internet Service Distribution')
                ax.set_xlabel('Internet Service')
                ax.set_ylabel('Count')
                plt.xticks(rotation=45)
                st.pyplot(fig, use_container_width=True)
    
    # TAB 4: MACHINE LEARNING MODELS
    with tab4:
        st.header("Model Training & Evaluation")
        
        # Data preprocessing
        df_model = df.copy()
        le = LabelEncoder()
        df_model['Churn_enc'] = le.fit_transform(df_model['Churn'])
        
        # Select numeric features
        numeric_cols = df_model.select_dtypes(include=[np.number]).columns.tolist()
        if 'Churn_enc' in numeric_cols:
            numeric_cols.remove('Churn_enc')
        
        if not numeric_cols:
            st.warning("No numeric features found for modeling")
        else:
            # Scale features
            scaler = StandardScaler()
            df_model[numeric_cols] = scaler.fit_transform(df_model[numeric_cols])
            
            st.info(f"✓ Using {len(numeric_cols)} features: {numeric_cols}")
            
            # Create train/test split helper
            def build_split(features):
                X = df_model[features].values
                y = df_model['Churn_enc'].values
                return train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Model 1: Single feature
            if len(numeric_cols) >= 1:
                st.subheader(f"Model 1: {numeric_cols[0]}")
                feature_1 = numeric_cols[0]
                X_train, X_test, y_train, y_test = build_split([feature_1])
                
                model1 = MLPClassifier(hidden_layer_sizes=(12, 8), activation='relu',
                                      solver='adam', max_iter=150, random_state=42, verbose=0)
                model1.fit(X_train, y_train)
                
                train_acc1 = model1.score(X_train, y_train)
                val_acc1 = model1.score(X_test, y_test)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Train Accuracy", f"{train_acc1:.1%}")
                with col2:
                    st.metric("Validation Accuracy", f"{val_acc1:.1%}")
                with col3:
                    st.metric("Feature(s)", 1)
                
                # Confusion matrix
                y_pred1 = model1.predict(X_test)
                cm1 = confusion_matrix(y_test, y_pred1)
                fig, ax = plt.subplots(figsize=(5, 4))
                sns.heatmap(cm1, annot=True, fmt='d', cmap='Blues', ax=ax, cbar=False)
                ax.set_title('Confusion Matrix - Model 1')
                ax.set_ylabel('True')
                ax.set_xlabel('Predicted')
                st.pyplot(fig, use_container_width=True)
            
            # Model 2: Regularized
            if len(numeric_cols) >= 1:
                st.subheader(f"Model 2: {numeric_cols[0]} (Regularized)")
                feature_2 = numeric_cols[0]
                X_train2, X_test2, y_train2, y_test2 = build_split([feature_2])
                
                model2 = MLPClassifier(hidden_layer_sizes=(12, 8), activation='relu',
                                      solver='adam', alpha=0.01, max_iter=150,
                                      random_state=42, verbose=0)
                model2.fit(X_train2, y_train2)
                
                train_acc2 = model2.score(X_train2, y_train2)
                val_acc2 = model2.score(X_test2, y_test2)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Train Accuracy", f"{train_acc2:.1%}")
                with col2:
                    st.metric("Validation Accuracy", f"{val_acc2:.1%}")
                with col3:
                    st.metric("Regularization", "L2")
                
                # Confusion matrix
                y_pred2 = model2.predict(X_test2)
                cm2 = confusion_matrix(y_test2, y_pred2)
                fig, ax = plt.subplots(figsize=(5, 4))
                sns.heatmap(cm2, annot=True, fmt='d', cmap='Blues', ax=ax, cbar=False)
                ax.set_title('Confusion Matrix - Model 2')
                ax.set_ylabel('True')
                ax.set_xlabel('Predicted')
                st.pyplot(fig, use_container_width=True)
            
            # Model 3: Multiple features
            if len(numeric_cols) >= 2:
                st.subheader(f"Model 3: Multiple Features ({min(3, len(numeric_cols))} features)")
                features_3 = numeric_cols[:3]
                X_train3, X_test3, y_train3, y_test3 = build_split(features_3)
                
                model3 = MLPClassifier(hidden_layer_sizes=(12, 8), activation='relu',
                                      solver='adam', max_iter=150, random_state=42, verbose=0)
                model3.fit(X_train3, y_train3)
                
                train_acc3 = model3.score(X_train3, y_train3)
                val_acc3 = model3.score(X_test3, y_test3)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Train Accuracy", f"{train_acc3:.1%}")
                with col2:
                    st.metric("Validation Accuracy", f"{val_acc3:.1%}")
                with col3:
                    st.metric("Feature(s)", len(features_3))
                
                st.write(f"**Features used:** {', '.join(features_3)}")
                
                # Confusion matrix
                y_pred3 = model3.predict(X_test3)
                cm3 = confusion_matrix(y_test3, y_pred3)
                fig, ax = plt.subplots(figsize=(5, 4))
                sns.heatmap(cm3, annot=True, fmt='d', cmap='Blues', ax=ax, cbar=False)
                ax.set_title('Confusion Matrix - Model 3')
                ax.set_ylabel('True')
                ax.set_xlabel('Predicted')
                st.pyplot(fig, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px;'>
        Customer Churn Analysis Dashboard | Data-driven insights for customer retention
    </div>
    """, unsafe_allow_html=True)

else:
    st.info("👈 Please load data from the sidebar to begin analysis")
