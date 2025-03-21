import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def show():
    st.markdown("<h1 style='text-align: center;'>📊 Explore Your Dataset 🔍</h1>", unsafe_allow_html=True)
    
    # Check if dataset exists in session state
    if "df" in st.session_state and st.session_state.df is not None:
        data = st.session_state.df
        
        # Select numeric columns
        numerical_cols = data.select_dtypes(include=np.number).columns
        
        # Select visualization type
        alternatives = ["Correlation Matrix", "Correlation between Specific Columns", "Distribution"]
        to_visual = st.selectbox("What would you like to visualize? 📉", alternatives, index=None)
        
        if to_visual == "Correlation Matrix":
            # Inform the user about the importance of the correlation matrix
            st.info("**Why Correlation Matrix is Important:**\n\nA correlation matrix shows the relationships between variables in your dataset. Visualizing it helps you identify strongly related variables, which can assist in feature selection and improve your machine learning models. 📊")
            if len(numerical_cols) > 0:
                corr_matrix = data[numerical_cols].corr()
                st.write(corr_matrix)
            else:
                st.warning("⚠️ No numeric columns found for correlation matrix.")



            
        if to_visual == "Correlation between Specific Columns":
            st.info("**Why Correlation Between Features is Important:**\n\nAnalyzing the correlation between two specific features helps you understand the relationship between them. This can provide valuable insights for your feature selection and modeling strategies. 📊")
            
            # Select two columns to visualize their correlation
            feature_1 = st.selectbox("Select the first feature:", numerical_cols)
            feature_2 = st.selectbox("Select the second feature:", numerical_cols)
            
            # Scatter plot to visualize the correlation between the two selected features
            if feature_1 and feature_2:
                st.subheader(f"**Correlation between {feature_1} and {feature_2}:**")
                
                # Plot the scatter plot
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.scatterplot(data=data, x=feature_1, y=feature_2, ax=ax)
                st.pyplot(fig)
                
                # Calculate and display the correlation coefficient
                correlation = data[feature_1].corr(data[feature_2])
                st.write(f"Pearson correlation coefficient: {correlation:.2f}")
        
        if to_visual == "Distribution":
            st.info("**Why Visualizing Distributions is Important:**\n\nVisualizing the distribution of your data helps you understand the spread, skewness, and any patterns or anomalies in individual features. This can inform data preprocessing and modeling strategies. 📊")
            
            # Select a column to visualize its distribution
            selected_column = st.selectbox("Select a column to view its distribution:", numerical_cols)
            
            # Select the type of plot (Histogram or KDE)
            plot_type = st.radio("Choose the plot type:", ("Histogram", "KDE"))
            
            # Plot the selected column's distribution
            if selected_column:
                fig, ax = plt.subplots(figsize=(8, 6))
                if plot_type == "Histogram":
                    sns.histplot(data[selected_column], bins=20, kde=False, ax=ax)
                elif plot_type == "KDE":
                    sns.kdeplot(data[selected_column], shade=True, ax=ax)
                
                st.pyplot(fig)
            
        
    else:
        st.warning("⚠️ **No data available!** Please upload a CSV file to get started. 📂")
