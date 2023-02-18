from pytube import YouTube
import os

def download_audio():
    video_url = input('Введите ссылку на видео: ')
    x = YouTube(video_url)
    name = f'{x.streams[0].title}.mp3'
    x.streams.filter(only_audio=True).first().download(filename=name)

download_audio()

