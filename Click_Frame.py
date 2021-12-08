import cv2
import pandas as pd
import os

PATH_VIDEO = "./h920/"

video_id = "1p_Dirk_choreo1_04.12.2021"
video_name = "1p_Dirk_choreo1_04.12.2021_h920.mp4"
PATH_ANNOT = os.path.join(PATH_VIDEO, video_id)
if not os.path.isdir(PATH_ANNOT):
    os.mkdir(PATH_ANNOT)
FILE_ANNOT = os.path.join(PATH_ANNOT, "Data_steps.csv")
FILE = os.path.join(PATH_VIDEO, video_name)

print(PATH_ANNOT)
print(FILE)

def check_path(x):
  if os.path.isdir(x):
    print("Using", x )
  else:
    print("Problem: There was no ", x)  # No error keeps running

check_path(PATH_ANNOT)
check_path(PATH_VIDEO)

# Functions to get the state of the mouse
def print_frame(event, x, y, flags, *userdata):
    if event == cv2.EVENT_LBUTTONDOWN:
        time_list.append(cap.get(cv2.CAP_PROP_POS_MSEC))
        frame_list.append(cap.get(cv2.CAP_PROP_POS_FRAMES))
        print(cap.get(cv2.CAP_PROP_POS_FRAMES))

# Extracting the frames of a video to feed MediaPipe
cap = cv2.VideoCapture(FILE)
time_list = []
frame_list = []

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        cv2.setMouseCallback("frame", print_frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

time_list = [round(x, 2) for x in time_list]
data_annot = pd.DataFrame(
    {"Time_ms": time_list,
     "Frame": frame_list}
)

data_annot.to_csv(FILE_ANNOT, index=False)


