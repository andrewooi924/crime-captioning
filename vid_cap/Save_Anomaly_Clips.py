# -*- coding: utf-8 -*-
# Author: Adit Goyal
# Date: 2021-06-18

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor
import os
import json
from os import listdir
from os.path import isfile, join

#Path of Directory containing the videos (.mp4) for anomaly detection
test_videoClips_path = 'vid_cap/input/'
#Path of Directory containing anomaly score files (.txt) for each video used in anomaly detection
eval_res_path = 'vid_cap/Eval_Res/'
#Path of Directory to store the clipped videos
Results_Path = "vid_cap/AnomalyClips/"

if not os.path.exists(Results_Path):
    os.makedirs(Results_Path)

All_eval_files = listdir(eval_res_path)
All_test_videoClips = listdir(test_videoClips_path)

All_eval_files.sort()
All_test_videoClips.sort()

#Threshold Value above which we consider the score as anomalous
threshold = 0.5

for i in range(len(All_eval_files)):
  eval_file_path = os.path.join(eval_res_path, All_eval_files[i])
  video_file_path = os.path.join(test_videoClips_path, All_test_videoClips[i])
  eval_file = open(eval_file_path, 'r')
  video_file = moviepy.editor.VideoFileClip(video_file_path)
  aa=All_eval_files[i]
  aa=aa[0:-4]
  video_duration = int(video_file.duration)
  Each_segment_length = video_duration//32

  j = 1
  highest = 0
  highest_j = 0
  Anomaly_startTime = 0
  Anomaly_endTime = 0
  scoreList = []
  for each in eval_file:
    Seg_score = float(each)
    scoreList.append(Seg_score)
    if Seg_score > highest:
      highest = Seg_score
      highest_j = j
    j = j + 1

  if highest_j == 1:
    Anomaly_startTime = 0
  else:
    Anomaly_startTime = Each_segment_length * (highest_j - 1.15)
        
  if highest_j == 32:
    Anomaly_endTime = video_duration
  else:
    Anomaly_endTime = Each_segment_length * (highest_j + 0.15)
  print(highest)
  print(Anomaly_endTime)
  print(Anomaly_startTime)
    
  
  ffmpeg_extract_subclip(video_file_path, Anomaly_startTime, Anomaly_endTime, targetname= Results_Path + aa + "_" + str(j) + ".mp4")

caption_json = {
    "data": {
        "anomaly_start": Anomaly_startTime,
        "anomaly_end": Anomaly_endTime
    }
}

# file_name = All_test_videoClips[0].split(".")[0] + ".json"
# file_path = os.path.join("captions", file_name)
file_path = "caption.json"

with open(file_path, "w") as json_file:
  json.dump(caption_json, json_file)

print("JSON file created, anomaly timestamps added")