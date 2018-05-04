#!/usr/bin/env python

import picamera
import time

# AstroHackers Pi Camera launch
# instantiating PiCamera
print ('BOOTED UP')
print ('Starting to use camera')
print ('File saved as test.h264')

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
   camera.start_recording('test2-q23-%d.h264' % i, format='h264', quality=23)
   camera.wait_recording(600)
   camera.stop_recording()
   print ('Captured test-q23-%d.h264' % i)

   camera.resolution = (3280,2462)
   camera.start_preview()
   time.sleep(2)
   camera.capture ('test-%d.jpg' % i)
   print ('Captured test-%d.jpg' % i)

camera.close()
