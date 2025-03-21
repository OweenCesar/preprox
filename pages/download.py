import streamlit as st

def show():
    # Title and Description
    st.markdown("<h1 style='text-align: center;'>📂 Download Your Updated Data</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Your processed dataset is ready! Click below to download.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Check if DataFrame is available
    if "df" in st.session_state and st.session_state.df is not None:
        data = st.session_state.df

        # Convert DataFrame to CSV
        csv = data.to_csv(index=False)

        # Add custom CSS for button styling (shadow, color, size)
        st.markdown("""
            <style>
                .download-btn {
                    display: inline-block;
                    padding: 15px 30px;
                    font-size: 20px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 8px;
                    text-align: center;
                    cursor: pointer;
                    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
                    transition: all 0.3s ease;
                    font-weight: bold;
                }
                .download-btn:hover {
                    background-color: #45a049;
                    box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2);
                }
            </style>
        """, unsafe_allow_html=True)

        # Centered Download Button with Shadow and Styling
        col1, col2, col3 = st.columns(3)
        with col2:
            # Create the download button
            st.download_button(
                label="⬇️ Download Updated Data",
                data=csv,
                file_name="updated_dataset.csv",
                mime="text/csv",
                use_container_width=True
            )

    else:
        st.warning("⚠️ No data available. Please process your data first.")
