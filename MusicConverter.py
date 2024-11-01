from moviepy.editor import *
from pytube import YouTube
import os
import requests

# def download_Youtube_Videos(url, output_path):
#     yt = YouTube(url) #yt contains all the info on the yt video from the URL
#     stream = yt.streams.filter(file_extension='mp4').first() #gathers all the streams and filters to find only mp4 and picks the first one 
#     video_path = stream.download(output_path) #downloads the mp4 stream to videopath
#     return video_path

def convert_video_to_flac(video_path, flac_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(flac_path, codec='flac')

<<<<<<< HEAD
# url = "https://www.youtube.com/watch?v=5xcvV_dxvvk"
# output_path ="C:\\Users\\fungb\\OneDrive\\Desktop\\MP4 Songs"
# video_path = download_Youtube_Videos(url, output_path)
# video_path = "C:\\Users\\fungb\\Downloads\\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM]\\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM] (1080p_24fps_H264-128kbit_AAC).mp4"
# flac_path = "C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\sleepwalking.flac"
=======
mp4_path = "C:\\Users\\Username\\Downloads\\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM]\Chain Gang of 1974 -  Sleepwalking [OFFICIAL HQ STREAM] (1080p_24fps_H264-128kbit_AAC).mp4" # copy as path the mp4 file
flac_path = "C:\\Users\\username\OneDrive\\Desktop\\Folder to addSongs\\Sleepwalking.flac"  # Specify where you want the file to go and file name
>>>>>>> 74d752971aa36355a22867f750731e90e351eda9

#convert_video_to_flac(video_path, flac_path)

files_to_Convert = [
    ("C:\\Users\\fungb\\OneDrive\\Desktop\MP4 Songs\\Age of Empires Rise of Rome Music 6 (480p_30fps_H264-128kbit_AAC).mp4",
     "C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\Rise of Rome 6.flac"),
     ("C:\\Users\\fungb\\OneDrive\\Desktop\\MP4 Songs\\Age of Empires Rise of Rome Music 2\\Age of Empires Rise of Rome Music 2 (480p_30fps_H264-128kbit_AAC).mp4",
      "C:\\Users\\fungb\\OneDrive\\Desktop\\Converted Songs\\Rise of Rome 2.flac")
]
for video_path, flac_path in files_to_Convert:
    convert_video_to_flac(video_path, flac_path)
    print(f"Converted output from {video_path} to {flac_path} ")
