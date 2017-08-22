#!/bin/bash

# reference(Rpi village) = http://www.rasplay.org/?p=7174
# * https://sourceforge.net/projects/mjpg-streamer/
# * https://github.com/codewithpassion/mjpg-streamer
# * https://github.com/liamfraser/mjpg-streamer

# i: delay.............: 200
# i: resolution........: 640 x 480
# i: camera parameters..............:
#        Sharpness 0, Contrast 0, Brightness 50
#        Saturation 0, ISO 400, Video Stabilisation No, Exposure compensation 0
#        Exposure Mode 'auto', AWB Mode 'auto', Image Effect 'none'
#        Metering Mode 'average', Colour Effect Enabled No with U = 128, V = 128
#        Rotation 0, hflip No, vflip No
#
# o: www-folder-path...: /home/pi/mjpg-streamer/mjpg-streamer-experimental/www/
# o: HTTP TCP port.....: 8080
# o: username:password.: disabled
# o: commands..........: enabled
# i: Starting Camera

# command:  lxterminal --command=/home/pi/streamer.sh


export STREAMER_PATH=$HOME/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=$STREAMER_PATH

$STREAMER_PATH/mjpg_streamer -i "input_raspicam.so -d 200" -o "output_http.so -w $STREAMER_PATH/www"
