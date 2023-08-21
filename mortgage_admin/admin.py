from datetime import datetime, date 
import streamlit as st
from PIL import Image
from data_process import read_api_df_filter_year, create_payment



st.title("Mortgage Repayment Admin")

tab1, tab2, tab3 = st.tabs(["Create New Mortgage Repayment", "Mortgage Repayment Data", "Stimulation"])

with tab1:
    # with st.expander("Create New Mortgage Repayment using Form"):
    st.subheader("Create New Mortgage Repayment")
    uploaded_file = st.file_uploader("**:green[Upload Recept]**")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        # Image.open(bytes_data)
        # st.write(type(bytes_data))
        st.image(uploaded_file)
        
    with st.form(key="my_form"):
        rate = st.slider("Interest Rate", 0.0, 1.0, 0.15)
        log_date = st.date_input("Enter date", date.today())
        exchange = st.number_input("Enter exchange value", min_value=465)
        repayment = st.number_input("Enter repayment value", min_value=2300)


        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            st.write(f"Interest Rate: {rate}")
            st.write(f"Date: {log_date}")
            st.write(f"Exchange: {exchange}")
            st.write(f"Repayment: {repayment}")

            payload = {
                'amount': repayment,
                "exchange": exchange,
                "interest_rate": rate,
            }
            create_payment(payload)




with tab2:
    st.subheader("Download Mortgages Payment Data")
    years = ['All', 2021, 2022, 2023, 2024, 2025]
    selected = st.selectbox("Select What Year", years)

    df = read_api_df_filter_year(selected)

    st.download_button(
        label="Download Data",
        data=df.to_csv().encode("utf-8"),
        file_name=f"mortages_{selected}.csv",
        mime="text/csv",
    )