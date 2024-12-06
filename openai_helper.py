import openai
import streamlit as st
openai.api_key = st.secrets["OpenAI_key"]
    
def transcribe_audio(audio_file):
    with open(audio_file, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)
    return transcript['text']

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil e fala português."},
            {"role": "user", "content": f"Resuma o seguinte texto:\n\n{text}"}
        ],
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stream=True
    )
    for chunk in response:
        if "choices" in chunk:
            yield chunk["choices"][0]["delta"].get("content", "")
