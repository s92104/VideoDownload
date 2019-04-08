from pytube import YouTube
import sys
import os

def complete(stream, file_handle):
    print("下載完成:",title)
def progress(stream, chunk, file_handle, bytes_remaining):
    percent = (100*(file_size-bytes_remaining))/file_size
    print(percent)

while True:
    link=input("link:")
    yt=YouTube(link)
    title=yt.title
    yt.register_on_complete_callback(complete)
    yt.register_on_progress_callback(progress)
    # 可下載
    videoStream=yt.streams.filter(progressive=True)
    video=videoStream.all()
    if len(video)==0:
        print("無法下載")
        sys.exit()
    # MP4
    mp4VideoStream=videoStream.filter(subtype="mp4")
    mp4Video=mp4VideoStream.all()
    if len(mp4Video)==0:
        print("無MP4")
        file_size=videoStream.order_by('resolution').desc().first().filesize
        videoStream.order_by('resolution').desc().first().download()
    else:      
        file_size=mp4VideoStream.order_by('resolution').desc().first().filesize
        mp4VideoStream.order_by('resolution').desc().first().download()
    
         

