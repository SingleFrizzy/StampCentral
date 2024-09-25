import streamlit as st
import os
import google.generativeai as genai

# API key
os.environ["GEMINI_API_KEY"] = "AIzaSyCGIfKLFbZq0KFXXnvkIpUhyqmHvu_XzME"

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# chat session with no initial history
chat_session = model.start_chat(history=[])

def chat_with_ai(message):
    response = chat_session.send_message(message)
    return response.text

# Streamlit app
st.title("StampCentral")

# Initialize session state for conversation history
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []


welcome_message = "Welcome to the Philately Chatbot! I am here to help you with all things related to stamps and philatelic material."
st.write(welcome_message)

user_message = st.text_input("You: ")

context = f"You are a Philately Chatbot. The user is looking for information related to stamps, philatelic material, or postal history. If the query is unrelated to stamps and philately, kindly inform the user that you can only assist with stamp-related inquiries."

# button to submit the user input
if st.button("Submit"):
    if user_message:
        st.session_state['conversation_history'].append(f"You: {user_message}")
        
        ai_response = chat_with_ai(f'{context} {user_message}')
        st.session_state['conversation_history'].append(f"AI: {ai_response}")
        st.write("ChatBot:", ai_response)



if st.button("Clear Chat History"):
    st.session_state['conversation_history'] = []

st.write("### Conversation History")
for message in st.session_state['conversation_history']:
    st.write(message)

