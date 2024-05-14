ssh -X tiziran@192.168.1.106

conda activate py39
cd farshid/depthai-python/depthai-experiments/gen2-gaze-estimation/
python main.py


ffmpeg -f video4linux2 -i /dev/video0 -f mpegts -codec:v mpeg1video -s 640x480 -b:v 800k -bf 0 - | ssh tiziran@192.168.1.106 "cat - | ffplay -"


https://qengineering.eu/install-opencv-on-jetson-nano.html#:~:text=To%20install%20OpenCV%2C%20you%20give,the%20core%20opencv%2Dpython%20library.

 