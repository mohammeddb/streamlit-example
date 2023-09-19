import openai
import streamlit as st

# Set your ChatGPT API key
openai.api_key = "YOUR_API_KEY"

# Define a function to generate a response from ChatGPT
def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    reply = response.choices[0].text.strip()
    return reply

# Create a Streamlit app
st.title("ChatGPT App")

# Create a text box for the user to input their prompt
prompt = st.text_input("Enter your prompt:")

# Generate a response from ChatGPT
response = get_response(prompt)

# Display the response to the user
st.write(response)
