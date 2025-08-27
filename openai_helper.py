from openai import OpenAI
import streamlit as st

# Initialize the client once
client = OpenAI(api_key=st.secrets["OpenAI_key"])

def transcribe_audio(audio_file: str) -> str:
    """Transcribe audio file to text using Whisper."""
    with open(audio_file, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text

def summarize_text(text: str):
    """Summarize text in Portuguese using GPT with streaming output."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil e fala português."},
            {"role": "user", "content": f"Resuma o seguinte texto:\n\n{text}"}
        ],
        temperature=0.7,
        max_tokens=200,
        stream=True
    )

    # Streaming response handling
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content
