#!/bin/bash

echo "src"
vlc -vvv ~/Desktop/720p.mp4 --sout '#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=11025}:rtp{sdp=rtsp://:8554/test}'
