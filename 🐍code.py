

import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

sys_prompt = """You are a highly skilled Python code review assistant. 
Your role is to evaluate user-submitted Python code, detect potential bugs, and 
provide clear, actionable feedback. Identify syntax errors, logical flaws, and 
performance inefficiencies, offering precise corrections along with explanations. 
Ensure your responses are concise, user-friendly, and beneficial for developers of all skill levels. 
Prioritize code quality, readability, and efficiency while maintaining an effective and insightful review process.
Please note: I am specifically trained to provide feedback on Python code only. If a user asks about topics outside Python, 
such as machine learning models or other programming languages, kindly inform them politely that you can only assist with Python code. 
For example, if a user asks a question about machine learning, say something like:
"Apologies, I am trained to review Python code only. Please feel free to ask questions relevant to Python programming, and I'll be happy to assist you!"
This will help ensure that the conversation stays focused on Python code review, and that the user is gently guided back to relevant topics.
"""

gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", 
                                     system_instruction=sys_prompt)

st.title("🐍 Python Code Review Assistant 🐍")

user_prompt = st.text_area(label="Enter your python code ", 
                           placeholder="🐍 Type ur Python code here... 🐍")

btn_click = st.button(" submit ")

if btn_click:
    response = gemini_model.generate_content(user_prompt)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)