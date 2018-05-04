#!/usr/bin/env python

import picamera
import time
import os

# AstroHackers Pi Camera launch
# instantiating PiCamera
print ('Starting camera recording')

rootpath = os.path.dirname(os.path.abspath(__file__))
mainpath = os.path.join(rootpath,'videos')

if not os.path.isdir(mainpath):
   os.mkdir(mainpath)

print ('Files save in "videos" subdirectory')

folder_count = len(next(os.walk(mainpath))[1])
video_path = os.path.join(mainpath,str(folder_count))

if not os.path.isdir(video_path):
   os.mkdir(video_path)

camera = picamera.PiCamera()

# camera setting
#camera.exposure_mode = 'sports'
camera.awb_mode = 'auto'

#sleep time is in sec so need to record 6 files per hr.
#30 files of 10 min (600sec) each. 5 hrs total. 1.2GB used per video file
# High Resolution still images being taken at the end of each video period.
# some video will be lost due to transition time

# Full HD video
for i in range(1,60):
   camera.resolution = (1640,1232)
   camera.framerate = 30
   time.sleep(2)
   camera.start_recording(os.path.join(video_path,'vid%d.h264' % i), format='h264', quality=23)
   camera.wait_recording(600)
   camera.stop_recording()
   print ('Captured vid%d.h264' % i)

   camera.resolution = (3280,2462)
   camera.start_preview()
   time.sleep(2)
   camera.capture(os.path.join(video_path,'pic%d.jpg' % i))
   print ('Captured pic%d.jpg' % i)

camera.close()
