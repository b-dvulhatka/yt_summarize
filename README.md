
# YouTube Video Summarizer

This application is a web-based tool designed to summarize the spoken content of YouTube videos. It leverages the capabilities of OpenAI's language models to transcribe and summarize audio content from videos. The application is built using Streamlit, providing an interactive user interface.

## Features

- **YouTube Audio Download**: The application downloads the audio from a given YouTube video URL using the `download_youtube_audio` function.
- **Audio Transcription**: The downloaded audio is transcribed into text using the `transcribe_audio` function, which utilizes OpenAI's Whisper model.
- **Text Summarization**: The transcribed text is summarized using the `summarize_text` function, which employs OpenAI's GPT-3.5-turbo model.
- **User Authentication**: The application includes a login system to ensure secure access. Users must provide valid credentials to access the summarization features.
- **API Key Management**: Users are required to input their OpenAI API key to enable transcription and summarization functionalities.

## Usage

1. **Login**: Enter your username and password in the sidebar to log in. The credentials are checked against the stored secrets.
2. **API Key Input**: After logging in, input your OpenAI API key in the sidebar to activate the transcription and summarization features.
3. **Video Analysis**: Enter the URL of a YouTube video in the main interface and click the "Analisar vídeo" button to start the analysis.
4. **Summary Display**: Once the analysis is complete, the summarized content of the video will be displayed on the page.

## Components

- **`analyze_video(youtube_url)`**: This function orchestrates the process of downloading, transcribing, and summarizing the video content. It handles exceptions and cleans up temporary files.
- **`sidebar()`**: Manages the sidebar interface, including login and API key input.
- **`main()`**: Defines the main user interface for video summarization, including input fields and result display.

## Requirements

- **Streamlit**: Used for building the web interface.
- **OpenAI API**: Required for transcription and summarization services.
- **YouTube Audio Module**: Custom module for downloading audio from YouTube videos.

This application is intended for personal use as a YouTube video summarizer, providing a convenient way to extract and condense spoken content from videos.
