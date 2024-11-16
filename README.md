# SheetQueryAI

## Project Description
**SheetQueryAI** is a powerful dashboard application designed as a part of BreakoutAI assignment to enhance productivity by integrating search queries and Google Sheets. With this tool, users can:
- Extract valuable data using APIs like SerpAPI and Groq.
- Seamlessly integrate Google Sheets.
- Perform operations such as CSV uploads and data updates with ease.
  
Additional Features:-
- write back the extracted data directly to the Google Sheet.
- Robust error-handling mechanisms for failed API calls or unsuccessful LLM queries, with user notifications.
---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
1. **Python 3.8+**
2. **pip** (Python package manager)

### Installation

Clone the repository:
   ```bash
   git clone https://github.com/phani69015/SheetQueryAI.git
   cd SheetQueryAI
   ```
Create a Virtual Environment and Activate It
   For Linux/Windows/Mac:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
This application includes functionality to handle  **API keys directly within the app interface** . You can enter and save your API keys for services like SerpAPI and GroqAPI using the provided dashboard.

Install the requirements
   ```bash
   pip install -r req.txt
   ```
Run the application using streamlit
  ```bash
  streamlit run main.py
  ```

You can access the application at  Local URL: http://localhost:8501

**Here is the Loom video for demonstration**

[![Watch the video](https://github.com/phani69015/SheetQueryAI/blob/main/Demo.png)](https://www.loom.com/embed/7b19b95f523f4c9090f79e4c15da424e?sid=8117dae4-d89c-46b3-8344-b728fd05fc4d)

