import cohere
import streamlit as st
import language_tool_python

# Set your Cohere API key
COHERE_API_KEY = ''  # Replace this with your actual API key
co = cohere.Client(COHERE_API_KEY)

# Function to generate tailored resume using Cohere API
def generate_resume(job_description, existing_resume):
    prompt = f"Tailor the following resume to match this job description:\n\nJob Description: {job_description}\n\nResume: {existing_resume}"
    
    # Call Cohere's generate function
    response = co.generate(
        model='command-xlarge-nightly',  # You can change the model if needed
        prompt=prompt,
        max_tokens=500
    )
    
    return response.generations[0].text.strip()

# Function to grammar check (requires Java for language-tool-python)
def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return language_tool_python.utils.correct(text, matches)

# Streamlit UI
st.title("GenAI - Resume Tailoring Tool")

# Input fields for job description and resume with unique keys
job_description = st.text_area("Enter Job Description", key="job_description_input")
existing_resume = st.text_area("Enter Your Current Resume", key="resume_input")

if st.button("Generate Tailored Resume"):
    tailored_resume = generate_resume(job_description, existing_resume)
    #tailored_resume = grammar_check(tailored_resume)
    st.text_area("Tailored Resume", value=tailored_resume, height=400, key="tailored_resume_output")