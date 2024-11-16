import streamlit as st
import os
from dotenv import load_dotenv
from Utilizers.data_loader import load_csv, display_columns,load_google_sheet,add_data_to_csv,add_data_to_google_sheet
from Utilizers.prompt_template import get_user_prompt
from Utilizers.serp_handler import search_entity_info
from Utilizers.groq_handler import extract_with_groq
from Utilizers.display import display_extracted_data
from Utilizers.creds import collect_credentials

load_dotenv()
CREDENTIALS_FILE_PATH = "Utilizers/credentials.json"

st.set_page_config(page_title="Data Extraction Dashboard", page_icon="📊", layout="wide")
def main():
    if not os.path.exists("Utilizers/.env") or not os.path.exists(CREDENTIALS_FILE_PATH):
        if not collect_credentials():
            st.stop() 
    st.title("Data Extraction Dashboard")
    upload_option = st.radio("Choose your data source:", ("Upload CSV", "Google Sheet"))

    df = None
    main_column = None
    


    if upload_option == "Upload CSV":
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file:
            df = load_csv(uploaded_file)

            if df is not None:
                main_column = display_columns(df)
            else:
                st.warning("Uploaded file could not be read as CSV.")
    else:
        sheet_url = st.text_input("Enter Google Sheet URL")
        if sheet_url:
            df = load_google_sheet(sheet_url)
            if df is not None:
                main_column = display_columns(df)

    prompt_template = get_user_prompt()

    if st.button("Fetch Data") and df is not None and main_column:
        search_results = []
        for entity in df[main_column]:
            query = prompt_template.replace("{main_column}", entity)
            serpapi_results = search_entity_info(query)
            print(query)
            if 'organic_results' in serpapi_results:
                search_text = "\n".join([result.get('snippet', '') for result in serpapi_results['organic_results']])
            else:
                search_text = "No organic results found for this query."
            print(search_text)
            extracted_info = extract_with_groq(prompt_template.replace("{main_column}", entity), search_text)
            
            search_results.append({"entity": entity, "extracted_info": extracted_info})
            print(extracted_info)

        display_extracted_data(search_results)
    
        if search_results:
            if upload_option == "Upload CSV":
                updated_csv = add_data_to_csv(df, search_results)
                if updated_csv:  
                    st.download_button(
                        label="Download Updated CSV",
                        data=updated_csv,
                        file_name="updated_data.csv",
                        mime="text/csv"
                    )
                else:
                    st.error("Failed to generate updated CSV data.")
            elif upload_option == "Google Sheet":
                add_data_to_google_sheet(sheet_url, search_results)

    else:
        if df is None:
            st.warning("Please upload a CSV file.")
        elif main_column is None:
            st.warning("Please select the main column for data extraction.")

main()
