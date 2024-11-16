import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_csv(uploaded_file):
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        return df
    return None

def display_columns(df):
    st.dataframe(df.head())
    main_column = st.selectbox("Select main column", df.columns)
    return main_column
def load_google_sheet(sheet_url):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    try:
        sheet = client.open_by_url(sheet_url)
        worksheet = sheet.get_worksheet(0)  
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        st.error(f"Error loading Google Sheet: {e}")
        return None



    
def add_data_to_google_sheet(sheet_url, new_data, column_name="New Data"):
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
            client = gspread.authorize(creds)
        
            sheet = client.open_by_url(sheet_url)
            worksheet = sheet.get_worksheet(0)  
            headers = worksheet.row_values(1)  
            if column_name not in headers:
                next_column = len(headers) + 1
                worksheet.update_cell(1, next_column, column_name)
                st.info(f"Added new column '{column_name}' at position {next_column}.")
            else:
                next_column = headers.index(column_name) + 1
            
            column_values = worksheet.col_values(next_column)
            next_row = len(column_values) + 1

            for i, data in enumerate(new_data):
                if isinstance(data, dict) and "extracted_info" in data:
                    extracted_value = data["extracted_info"]  
                    worksheet.update_cell(next_row + i, next_column, extracted_value)
                else:
                    st.warning(f"Invalid data format at index {i}: {data}")

            st.success("Data added to Google Sheet successfully.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    

def add_data_to_csv(df1, new_data, column_name="Extracted Info", key_to_extract="extracted_info"):
    try:
        df = df1.copy()
    except (pd.errors.EmptyDataError, FileNotFoundError):
        print("CSV is empty or not found. Creating a new DataFrame with the specified column.")
        extracted_data = [data.get(key_to_extract, "") for data in new_data]
        df = pd.DataFrame({column_name: extracted_data})   
    else:
        original_column_name = column_name
        counter = 1
        while column_name in df.columns:
            column_name = f"{original_column_name} ({counter})"
            counter += 1

        extracted_data = [data.get(key_to_extract, "") for data in new_data]

        if len(extracted_data) > len(df):
            df = df.reindex(range(len(extracted_data)))

        df[column_name] = extracted_data

    return df.to_csv(index=False).encode('utf-8')
