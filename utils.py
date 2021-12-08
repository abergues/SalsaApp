
import os
from datetime import date
from sys import exit
import time
# from  ipywidgets import
from config import root_path
from IPython.display import Video

def label_a_video(clip_name):
    start_coding_time = time.ctime()
    print(start_coding)
    clip_name = clip_name
    video_path = os.path.join(root_path, clip_name)
    os.chdir(video_path)
    if os.path.isfile(clip_name):
        print("You can now label ", clip_name, "that is in \n",
               video_path)

        Video(clip_name)

        labeled_video_data =[ ]

        while key not x:
            key = input("Basic, Right turn, Side, Cuban, suzieQ, Other, eXit")
            present_time = time.ctime()
            video_time = start_coding_time - present_time
            labeled_video_point = {"clip_name": clip_name ,
                                  "video_time": video_time,
                                  "label"     : key}
                        labeled_video_data = pd.Series(labeled_video_point)
            labeled_video_df = labeled_video_df(labeled_video_data, ignore_index=True)
            time.sleep(0.1)

        print(labeled_video_df)

    else:
        print("There is something wrong with the video file or path")

    return labeled_video_df