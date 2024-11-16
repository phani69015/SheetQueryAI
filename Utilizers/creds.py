from dotenv import set_key
import streamlit as st
import json  

def save_to_env(api_name, api_key):
    try:
        set_key("Utilizers/.env", api_name, api_key)
        st.info(f"{api_name} saved successfully.")
    except Exception as e:
        st.error(f"Error saving {api_name}: {str(e)}")

def collect_credentials():
    st.title("Credential Input for Data Extraction")
    st.markdown("Please provide your API credentials and click Submit.")

    serpapi_key = st.text_input("Enter your SerpApi Key")
    
    groqapi_key = st.text_input("Enter your GroqAPI Key")
    
    gcp_credentials = st.text_area("Enter your GCP Sheets Credentials (JSON format)")
    
    if gcp_credentials:
        try:
            gcp_credentials_dict = json.loads(gcp_credentials)
        except json.JSONDecodeError:
            st.error("Invalid JSON format. Please ensure you provide the correct JSON structure.")

    # Add a Submit Button
    if st.button("Submit"):
        if serpapi_key and groqapi_key and gcp_credentials_dict:
            with open("Utilizers/credentials.json", "w") as json_file:
                json.dump(gcp_credentials_dict, json_file, indent=4)
            st.success("GCP credentials saved to json file.")
            save_to_env("SERPAPI_KEY", serpapi_key)
            save_to_env("GROQAPI_KEY", groqapi_key)
            st.success("All credentials have been successfully saved. Please Refresh the page")
        else:
            st.warning("Please fill in all fields before submitting.")
