import os
import streamlit as st
from youtube_audio import download_youtube_audio
from openai_helper import transcribe_audio, summarize_text
import time

# Configure the Streamlit page
st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎥")

# Function to handle video analysis
def analyze_video(youtube_url):
    """
    Analyzes a YouTube video by downloading its audio, transcribing it, and summarizing the transcript.

    Args:
        youtube_url (str): URL of the YouTube video.

    Returns:
        str: Summary of the video.
    """
    try:
        with st.spinner("Processando..."):
            # Initialize OpenAI client

            # Download and process YouTube audio
            audio_file = download_youtube_audio(youtube_url)
            transcript = transcribe_audio(audio_file)
            summary = summarize_text(transcript)

            # Clean up temporary audio file
            if os.path.exists(audio_file):
                os.remove(audio_file)

        return summary

    except Exception as e:
        st.error(f"Erro: {str(e)}")
        return None

# Sidebar login and OpenAI key input
def sidebar():
    """
    Displays the login and OpenAI API key input in the sidebar.
    """
    st.sidebar.title("🔑 Acesso")
    
    # Login form
    with st.sidebar.expander("Login com credenciais"):
        if st.session_state.get("logged_in", False):
            st.sidebar.success("Você está logado!")
            if st.sidebar.button("Sair"):
                st.session_state["logged_in"] = False
                st.session_state["openai_key"] = None
                st.sidebar.info("Você saiu da conta. Faça login novamente, se necessário.")
                st.rerun()
        else:
            username = st.text_input("Usuário:", placeholder="Digite seu usuário", key="username")
            password = st.text_input("Senha:", placeholder="Digite sua senha", type="password", key="password")
            if st.button("Entrar", key="login_button"):
                if username == st.secrets["Login"] and password == st.secrets["Password"]:
                    st.session_state["logged_in"] = True
                    st.session_state["openai_key"] = st.secrets["OpenAI_key"]
                    st.sidebar.success("Login realizado com sucesso!")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.sidebar.error("Usuário ou senha incorretos.")
                    
    st.sidebar.subheader('Details')
    st.sidebar.write("***Why this page has a login requirement?***")
    st.sidebar.markdown("This page was created to work as a personal youtube video summarizer.")


# Main app interface
def main():
    """
    Main interface for the video summarizer app.
    """
    st.title("📹 YouTube Video Summarizer")
    st.markdown(
        "Insira a URL de um vídeo do YouTube e obtenha um resumo do conteúdo falado no vídeo."
    )
    # Input field for YouTube URL
    youtube_url = st.text_input("🔗 URL do YouTube:", placeholder="Cole o link aqui...")

    # Button to start analysis
    if st.button("Analisar vídeo"):
        if not youtube_url:
            st.error("Por favor, insira uma URL válida.")
        elif "openai_key" not in st.session_state or not st.session_state["openai_key"]:
            st.error("Por favor, insira uma chave API válida no menu lateral.")
        else:
            summary = analyze_video(youtube_url)
            if summary:
                # Display the results
                st.subheader("Resumo do Vídeo")
                st.write(summary)

# Run the app
if __name__ == "__main__":
    # Sidebar with login and API key input
    sidebar()

    # Display the main interface only if an API key is available
    if "openai_key" in st.session_state and st.session_state["openai_key"]:
        main()
    else:
        st.warning("Por favor, faça login no menu lateral.")
