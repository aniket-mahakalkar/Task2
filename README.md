# 🧠 AI Architecture Assistant

A Streamlit-based tool powered by OpenAI's GPT-4 that helps you convert high-level business requirements into a detailed technical architecture. Perfect for software engineers, solution architects, or tech founders looking to bridge the gap between idea and implementation.

---

## 🚀 Features

- **🔹 Functional Module Breakdown**  
  Extracts and lists the key functional components of the system.

- **🗃️ Database Schema (SQL)**  
  Suggests an appropriate relational database structure in SQL format.

- **🤖 Pseudocode Generation**  
  Generates pseudocode for main logic components, offering a foundation for implementation.

---

## 🛠️ How It Works

1. **Enter a High-Level Requirement**  
   Input your business or product requirement in natural language.

2. **Click "Generate Architecture"**  
   The app sends your input to OpenAI's GPT-4 model using a carefully crafted prompt.

3. **Get Detailed Output**  
   The response is broken down into:
   - Functional Modules
   - Suggested Database Schema
   - Key Pseudocode Functions

---

## 🖥️ Tech Stack

- [Streamlit](https://streamlit.io/) – For building the interactive UI.
- [OpenAI GPT-4](https://platform.openai.com/docs/guides/gpt) – For generating architecture suggestions.
- [Python](https://www.python.org/) – Core programming language.
- [python-dotenv](https://pypi.org/project/python-dotenv/) – To load environment variables securely.

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/aniket-mahakalkar/Task3-AI-Architecture.git
cd Task3-AI-Architecture.git

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env

# Run the Streamlit app
streamlit run ai_hld-lld.py
