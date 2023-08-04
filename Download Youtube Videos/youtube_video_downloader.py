# import package
from pytube import YouTube

url = input("Enter video Link here: ")

try:
    vid = YouTube(url)
except:
    print("Connection Error!")

print("************* VIDEO TILE ***************")
# get video title
print(vid.title)

print("******* THUMBNAIL IMAGE ********")
# get thumbnail image
print(vid.thumbnail_url)

print("***** VIDEO *****")
# set stream resolution
video = vid.streams.get_highest_resolution()

# or video = vid.streams.first()
# for stream in video.streams:
#       print(stream)

# download video in mp4

try:
    video.download("video.mp4")
except:
    print("Task Cannot be Completed Due to some Error!")

print("Task Completed!")

