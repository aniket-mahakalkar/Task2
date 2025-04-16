import streamlit as st
from chains.llm_chain import get_spec_chain
import yaml
import os
from dotenv import load_dotenv
from io import StringIO
load_dotenv()

st.set_page_config(page_title="Spec Generator", layout="wide")
st.title("🧠 High-Level to Low-Level Spec Generator")

requirement = st.text_area("Enter a high-level business requirement:", height=200)

if st.button("Generate"):
    if not requirement.strip():
        st.warning("Please enter a requirement.")
    else:
        with st.spinner("Thinking..."):
            chain = get_spec_chain()
            result = chain.invoke(requirement)

            # Display result
            st.code(result, language="yaml")

            # Export: YAML
            yaml_bytes = result.encode("utf-8")
            st.download_button(
                label="📥 Download YAML",
                data=yaml_bytes,
                file_name="specification.yaml",
                mime="text/yaml",
            )

            # Export: Markdown
            md_content = f"```yaml\n{result}\n```"
            md_bytes = md_content.encode("utf-8")
            st.download_button(
                label="📥 Download Markdown",
                data=md_bytes,
                file_name="specification.md",
                mime="text/markdown",
            )
