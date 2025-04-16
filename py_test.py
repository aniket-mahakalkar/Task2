import streamlit as st
import openai
import os

from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI API key here or via environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Architecture Assistant", layout="wide")
st.title("🔧 High-Level to Low-Level Architecture Generator")

st.markdown("""
This tool helps you convert high-level business requirements into:
- Functional modules
- Database schema (SQL)
- Pseudocode
""")

# Input
high_level_req = st.text_area("Enter your high-level business requirement:", height=200)

if st.button("Generate Architecture") and high_level_req:
    
    with st.spinner("Analyzing and generating output..."):
        # Prompt template
        prompt = f"""
You are an expert software architect. Given the following high-level business requirement, break it down into:
1. A list of functional modules
2. Suggested database schema (in SQL format)
3. Key pseudocode functions for main logic

High-Level Requirement:
{high_level_req}

Output:
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful software architect assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4
            )

            output_text = response['choices'][0]['message']['content']

            # Attempt to split output into sections
            modules_section = ""
            schema_section = ""
            pseudocode_section = ""

            if "Suggested database schema" in output_text:
                parts = output_text.split("Suggested database schema")
                modules_section = parts[0].strip()
                if "Key pseudocode functions" in parts[1]:
                    schema_parts = parts[1].split("Key pseudocode functions")
                    schema_section = schema_parts[0].strip()
                    pseudocode_section = schema_parts[1].strip()
                else:
                    schema_section = parts[1].strip()
            else:
                modules_section = output_text.strip()

            # Display sections
            if modules_section:
                st.markdown("### 🧩 Functional Modules")
                st.code(modules_section, language="markdown")

            if schema_section:
                st.markdown("### 🗃️ Database Schema")
                st.code(schema_section, language="sql")

            if pseudocode_section:
                st.markdown("### 🤖 Pseudocode")
                st.code(pseudocode_section, language="python")

        except Exception as e:
            st.error(f"Error: {e}")