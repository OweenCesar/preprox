import streamlit as st
import pandas as pd
import io
import time
from operations.functions import zscore_outliers

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")




def show():
    st.title("Let's Get Started: CSV Data Preprocessing")
    to_select = ["Check basic statistics" , "Shape", "Search for duplicates","Delete Columns","Change Column Names", "Missing Values", "Find Outliers",  "Create New Features"]
    
    #Before the file uploader, I have to check if df is already in st.session_state
    #If not , we initialize it to None

    if "df" not in st.session_state:
            st.session_state.df = None
         
    
    # Handling the uploaded file and storing it into a Dataframe
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"]) # File uploader widget


   



    if uploaded_file is not None and st.session_state.df is None:
        # after uploading the file, store it in the session state
        st.session_state.df = pd.read_csv(uploaded_file)
        st.write("Filename:", uploaded_file.name)
    
    # access the data from the session state
    data = st.session_state.df 


    if data is not None:
        st.write("Data preprocessing and analysis will go here.")
        st.write(f"Thanks for uploading your CSV file! Your dataset has **{data.shape[0]} rows** and **{data.shape[1]} columns**. Here are the column names:") 
        st.write(list(data.columns))
        
        categorical_cols = data.select_dtypes(include=['object']).columns
        numerical_cols = data.select_dtypes(include= np.number ).columns

        
        user_selection = st.selectbox("What would you like to do? ", to_select, index=None) 
        all_col_names = data.columns


        if user_selection == "Check basic statistics":
            col1, col2  = st.columns(2)
            with col1:
                st.header("Basic Statistics")
                st.write(data.describe(include=['number']))
            with col2:
                st.subheader("We have found the following features of 'object' data type:")
                if categorical_cols.any():
                    st.write("Object columns:", list(categorical_cols))
                    st.write(data.describe(include=['object']))

                else:
                    st.write("No categorical columns found in the dataset.")


            st.subheader("This is how the first ten rows of your dataset looks like: ")    

            st.dataframe(data.head(10).style.set_properties(
    **{'font-weight': 'bold', 'color': '#374151', 'background-color': '#F3F4F6'}  # Light gray background
))
            buffer = io.StringIO() #Create an in memory text stream
            data.info(buf=buffer)   # buf=buffer, we tell Pandas "send the output to buffer instead."
            info_str = buffer.getvalue() # get the output as string
            st.subheader("Dataset Information:")
            st.code(info_str, language="python")



            st.success(
        "Basic statistics are displayed! 🎉\n\n"
        "To explore more, simply select a new option from the dropdown above! 😎"
    )


        if user_selection == "Search for duplicates":
            st.info("Removing duplicate data in machine learning is crucial because it prevents models from being biased toward repeated instances, ensuring fair and accurate learning. It also reduces computational costs by eliminating redundant data, improving efficiency in training and prediction.  Additionally, removing duplicates helps maintain data integrity, leading to better generalization and more reliable model performance.")
            duplicates = st.session_state.df[st.session_state.df.duplicated(keep=False)]
            st.write(duplicates)
            if duplicates.empty:
                st.success("No duplicates found! ✅ One less data headache to worry about! 😌")    
            else:
                st.warning("Duplicates found! ⚠️, take a look to some of them: ")
                st.dataframe(duplicates.head(15))
        # Delete button
                if st.button("Delete Duplicates"):
                    st.session_state.df = st.session_state.df.drop_duplicates()
                    st.rerun()
                    st.success(
                    "Duplicates deleted! ✅\n\n"
                    "After your action, the duplicates have been deleted and the changes have been applied. "
                    "If you want to continue preparing your data, select an option from the dropdown above. "
                    "If you don't need more actions, go to the **'Get my new dataset'** page  **download your new dataset**. 🚀"
                    )
            st.write(st.session_state.df.head(20))  # Show updated DataFrame


        if user_selection == "Shape":
            rows, columns = st.session_state.df.shape
            st.info("""
    **Why Knowing the Shape of Your Dataset is Important:**

    Understanding the shape of your dataset (rows and columns) gives you an idea of its size and structure. This is crucial for deciding on the appropriate preprocessing steps and ensuring your data fits the model’s requirements.
    """)
            st.write(f"Your dataset contains currently {rows} rows and {columns} columns.")

        if user_selection == "Delete Columns":
            st.info("""
    **Why Deleting Irrelevant Columns is Important:**

    Removing unnecessary or irrelevant columns helps reduce the complexity of the dataset, improves the performance of machine learning models, and ensures that the model only learns from the relevant features.
    """)
            delete_col = st.selectbox("Please select the column that you want to delete from your dataset: ", data.columns, index=None)
            if delete_col:
                progress_bar = st.progress(0)
                for percent in range(100):
                    time.sleep(0.02)
                    progress_bar.progress(percent + 1)
                
                data.drop(columns= delete_col,  inplace=True)
                st.session_state.df = data 

                st.success(f"✅ The column {delete_col} have been successfully. \n\n"  
                        "🔹 Your changes are now **final**."  
                    " 📥 You can go to the **'Get My New Data'** page to download your updated dataset with the applied changes. " 
                    " 📊 Or, continue refining your dataset by selecting another option from the dropdown above. Happy data prepping! 🚀")
                st.subheader(f"Current Overview of your uploaded dataset after deleting the column {delete_col} ")
                st.write(data.head(10))
        
        if user_selection == "Change Column Names":
            st.info("""
    **Why Changing Column Names is Important for Machine Learning:**

    Clear and descriptive column names make it easier to understand the data and improve the readability of your code. Proper naming also helps when building models, ensuring that the features are easily identifiable and interpretable.
    """)
            change_name = st.selectbox("Please select the column name that you want to modify: ", data.columns, index=None)
            if change_name:
                new_name = st.text_input("New column name here", max_chars= 55,
                                placeholder= "Write here the new column name")
                if new_name:
                    data.rename( columns={change_name:new_name},  inplace=True)
                    st.subheader(f"Current Overview of your dataset after renaming the column: {change_name} ")
                    st.write(data.head(10))

        if user_selection == 'Missing Values':
                st.info("""
    **Why Handling Missing Values is Important for Machine Learning:**

    Missing values can introduce bias and reduce the quality of the model. Handling them properly (e.g., by imputing or removing) ensures the model has complete and accurate data, leading to better predictions and model performance.
    """)
                missing_values = data.isnull().sum()   #shows the number by column
                missing_columns = missing_values[missing_values > 0] #selecting only the columns that have missing values.
                if missing_columns.empty:
                    st.success("Fantastic! Your dataset has not missing values! ")
                    st.write(missing_values)
                else:
                    st.subheader('Missing Values in your dataset')
                    st.write(missing_values)
                    user_do = st.selectbox("How would you like to handle missing values?", ("Enter a specific value", "Fill with median",
                                        "Fill with mean"), index=None)
                    if user_do == "Enter a specific value":
                        user_value = st.text_input("Enter a value to fill missing data: ")
                        if user_value:
                            data.fillna(user_value, inplace=True)
                            st.success("Missing values have been filled with your entered value")
                            st.rerun()

                    elif user_do == "Fill with median":
                        st.button("Apply median")
                        data.fillna(data.median(numeric_only=True), inplace=True)
                        st.success("Missing values have been filled with the median ")
                        st.rerun()

                    elif user_do == "Fill with mean":
                        if st.button("Apply mean"):
                            data.fillna(data.mean(numeric_only=True), inplace=True)
                            st.success("Missing values have been filled with the mean")
                            st.rerun()


        if user_selection == "Find Outliers":
            st.info("""
    **Why Finding Outliers is Important for Machine Learning:**

    Outliers can distort statistical measures like the mean and variance, negatively affecting model performance. Identifying and handling them helps improve model accuracy and generalization by ensuring the model is trained on clean, reliable data.
    """)            
            column_name = st.selectbox("Select the column to check:", numerical_cols)
            if column_name:
                outlier_indices, outliers_data = zscore_outliers(data, column_name, threshold=3)
                fig, ax = plt.subplots(figsize=(6, 4))
                sns.boxplot(y=data[column_name], ax=ax, color="lightblue")
                if isinstance(outlier_indices, list) and outlier_indices:  # If outliers exist
                    ax.scatter(y=outliers_data, x=[0]*len(outliers_data), color="red", label="Outliers", zorder=3)
                    ax.legend()


                ax.set_title(f"Original Data - Outliers in {column_name}")
                st.pyplot(fig)

                if isinstance(outlier_indices, list) and outlier_indices:  # If outliers exist
                    remove_outliers = st.radio("Do you want to remove these outliers?", ["No", "Yes"])
            
                    if remove_outliers == "Yes":
                        st.session_state.df = data.drop(index=[i for i in outlier_indices if i in data.index])
                        st.success("Outliers removed! Updated dataset stored.")

                # 3️⃣ Re-Visualize the cleaned dataset
                        fig, ax = plt.subplots(figsize=(6, 4))
                        sns.boxplot(y=st.session_state.df[column_name], ax=ax, color="lightgreen")
                        ax.set_title(f"Cleaned Data - {column_name} (No Outliers)")
                        st.pyplot(fig)

                         

              
                
                else:
                    st.write(outlier_indices)  # Show message "No outliers detected"


        if user_selection == "Create New Features":
            st.subheader("🚧 This feature is currently being developed. Stay tuned for updates! 🚧")
            st.markdown("Our developer is actively working on this, and we will keep you updated. Please check back soon.")

        


    

                
    
 
    else:
        st.write("Please upload a CSV file to get started.")



   
