import streamlit as st
import pandas as pd


def get_user_prompt():
    st.write("Specify a prompt with placeholders (e.g., {company}) that will be replaced by values from your selected column.")
    prompt_template = st.text_input(
        "Enter your custom prompt", 
        "Get me the (requirement) of {main_column}"
    )
    return prompt_template

def main():
    st.title("Prompt Generator Test App")

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded CSV Data Preview:", data.head())

        column_options = list(data.columns)
        main_column = st.selectbox("Select the main column to use in the prompt", column_options)

        prompt_template = get_user_prompt()

        if st.button("Generate Prompts"):
            final_prompts = [
                prompt_template.replace("{main_column}", str(row))
                for row in data[main_column]
            ]
            
            st.write("Generated Prompts:")
            for prompt in final_prompts:
                st.write(prompt)

if __name__ == "__main__":
    main()