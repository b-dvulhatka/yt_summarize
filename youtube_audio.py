import pytubefix

def download_youtube_audio(url):
    yt = pytubefix.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    audio_file = stream.download(filename="audio.mp4")
    return audio_file
