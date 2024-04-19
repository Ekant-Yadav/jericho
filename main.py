import pandas as pd
from make_video import generate_video
import ffmpeg
import os


input_audio = ffmpeg.input('templates/audio_template.mp3')






filepath = "Data/1.csv"
df = pd.read_csv(filepath)

for i,row in df.iterrows():
    generate_video(i,row)
    print(i)
    input_video = ffmpeg.input("result/output" + str(i)+"na.mp4")
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output("result/output" + str(i)+".mp4", loglevel="quiet" ).run(overwrite_output=True)
    os.remove("result/output" + str(i)+"na.mp4")
    print("done",i)