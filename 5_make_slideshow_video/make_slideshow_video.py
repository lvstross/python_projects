#!/usr/bin/env python
import time
from os import listdir
from os.path import isfile, join
from moviepy.editor import VideoFileClip, concatenate_videoclips


path = "./clips/"
clipFilePaths = [path + f for f in listdir(path) if isfile(join(path, f))]

videoClips = []
for clip in clipFilePaths:
    videoObject = VideoFileClip(clip).resize(newsize=(1280,720))
    videoClips.append(videoObject)

timeStamp = repr(time.time())
finalClip = concatenate_videoclips(videoClips)
fileName = "video-" + timeStamp + ".mp4"
finalClip.write_videofile(
    "./videos/" + fileName,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True, codec="libx264",
    audio_codec="aac"
)
