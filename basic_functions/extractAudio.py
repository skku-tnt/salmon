import sys
import os
import moviepy
import moviepy.editor

# curPath = os.getcwd()
# print(curPath)
# os.chdir('gdrive/My Drive/Colab Notebooks/extract-script/testfile')
# curPath = os.getcwd()
# print(curPath)

video = moviepy.editor.VideoFileClip("test_video.mp4")

audio = video.audio

audio.write_audiofile("test_audio.wav")