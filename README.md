# Drone-3D
Drone 3D Detection Repository for the CVPR UG2+ Challenge 2024.

Terminal 1
```
roscore
```
Terminal 2
```
rosbag play dataset/2023-08-24-11-14-34.bag

# alternatively
rosbag decompress dataset/2023-08-24-11-14-34.bag
rosbag play dataset/2023-08-24-11-14-34.bag # update to new decompressed file
```
Terminal 3
```
python3 rosbag-image-saver.py
```
