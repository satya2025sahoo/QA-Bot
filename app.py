import streamlit as st
import tempfile
import os

# Import the QAChatbot class from your backend
from Backend import QAChatbot

# Function to save uploaded file temporarily
def save_uploaded_file(uploadedfile):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploadedfile.name.split('.')[-1])
    temp_file.write(uploadedfile.getbuffer())
    return temp_file.name

# Initialize session state to store chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Streamlit app layout
st.set_page_config(page_title="Chat-style QA Bot", layout="wide", page_icon="💬")

# App header
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>💬 Chat-style QA Bot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Upload your document and start chatting!</h4>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload your document (TXT or PDF only)", type=["txt", "pdf"], help="Drag and drop file here or click to browse.")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    temp_file_path = save_uploaded_file(uploaded_file)

    # Initialize the QA bot with the document path
    chatbot = QAChatbot(temp_file_path)

    st.success("File uploaded successfully! You can now chat with the bot.")

    # Display chat
    st.markdown("### Chat History")

    # Chat history display
    for message in st.session_state['messages']:
        if message['role'] == 'user':
            st.markdown(f'<div style="background-color: #e1ffc7; color: #000; border-radius: 10px; padding: 10px; margin-bottom: 5px;"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="background-color: #dbe6f4; color: #000; border-radius: 10px; padding: 10px; margin-bottom: 5px;"><strong>Bot:</strong> {message["content"]}</div>', unsafe_allow_html=True)
            if 'segments' in message:
                st.markdown('<div style="background-color: #f4f4f4; color: #000; border-radius: 10px; padding: 10px; margin-top: 5px;"><strong>Retrieved Segments:</strong></div>', unsafe_allow_html=True)
                for segment in message['segments']:
                    st.markdown(f'<div style="background-color: #f9f9f9; color: #000; border-radius: 5px; padding: 5px; margin-bottom: 3px;">- {segment}</div>', unsafe_allow_html=True)

    # User input for chat
    with st.form(key='input_form', clear_on_submit=True):
        user_query = st.text_input("Type your message:", key="user_input_form")
        submit_button = st.form_submit_button("Send")

        if submit_button and user_query:
            # Store the user query in chat history
            st.session_state['messages'].append({'role': 'user', 'content': user_query})

            # Get the response from the chatbot
            response, retrieved_segments = chatbot.interact_with_llm(user_query)

            # Store the bot's response and retrieved segments in chat history
            st.session_state['messages'].append({'role': 'bot', 'content': response, 'segments': retrieved_segments})

            # Rerun the app to update the chat history
            st.experimental_rerun()

else:
    st.warning("Please upload a TXT or PDF file to start.")
