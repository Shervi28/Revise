from pytube import YouTube
from pydub import AudioSegment
from os import path
import os

  

yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
video = yt.streams.filter(only_audio=True).first()
  

print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  

out_file = video.download(output_path=destination)
  

base, ext = os.path.splitext(out_file)
new_file = base + '.wav'
os.rename(out_file, new_file)
  

print(yt.title + " has been successfully downloaded.")

src = new_file
dst = "test-{}.wav".format(new_file)
                                                           
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

print("Successfully converted")
