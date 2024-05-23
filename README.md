# CVPR 2024 UG2+ Challenge Track 5: UAV Tracking and Pose Estimation 
This is the official repository for the CVPR UG2+ Challenge 2024 Track 5- [UAV Tracking and Pose Estimation](https://cvpr2024ug2challenge.github.io/rules24_t5.html). 

If you are interested in our work, please consider giving us a star.

## Leading Board 
![image](https://github.com/NTU-ICG/Drone-3D/assets/19664995/85ed5cdf-69c6-4ebf-b453-a31c248b5bc6)


## Methodology
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
