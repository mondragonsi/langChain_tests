import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

# load .env file for API key and other environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI()

# Initialize the language model (LLM)
llm = ChatOpenAI(
    model="gpt-4",  # change this to "gpt-4" or another available model
    temperature=0.5,
    max_tokens=1000,
    timeout=10,
    max_retries=3
)

# Function to simulate the interview process with Streamlit interface
def chat_with_avatar():
    st.title("Entrevista Simulada com Avatar")
    st.write("Olá! Eu sou seu entrevistador de hoje para a vaga em Java. Vamos começar a entrevista!")

    # Keep track of the conversation history
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            ("system", "Você é um assistente entrevistador de candidatos para a linguagem Java. Você faz perguntas e avalia as respostas dos candidatos.")
        ]

    # Display conversation history
    for role, message in st.session_state.messages:
        if role == "user":
            st.write(f"Você: {message}")
        elif role == "assistant":
            st.write(f"Avatar: {message}")
    
    # User input field
    user_question = st.text_input("Digite sua resposta ou pergunta:", "")

    if st.button("Enviar"):
        if user_question.lower() in ['exit', 'quit', 'bye']:
            st.write("Avatar: Até logo! Fim da entrevista.")
        else:
            # Add the user's question to the session state
            st.session_state.messages.append(("user", user_question))
            
            # Get the assistant's response
            response = llm.invoke(st.session_state.messages)
            
            # Add the assistant's response to the session state
            st.session_state.messages.append(("assistant", response.content))

# Start the Streamlit app
if __name__ == "__main__":
    chat_with_avatar()
