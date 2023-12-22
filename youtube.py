from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension = "mp4")
        highest_resolution = streams.get_highest_resolution()
        highest_resolution.download(output_path=save_path)
        print("Downloaded Successfully")
    
    except Exception as e:
        print(e)

url ="https://www.youtube.com/watch?v=mWaMSGwiSB0"
save_path="C:/Users/Mara/Downloads"
download_video(url, save_path)
