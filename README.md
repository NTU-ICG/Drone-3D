# CVPR 2024 UG2+ Challenge Track 5: UAV Tracking and Pose Estimation 
This is the official repository for the CVPR 2024 UG2+ Challenge Track 5- [UAV Tracking and Pose Estimation](https://cvpr2024ug2challenge.github.io/rules24_t5.html). 

If you are interested in our work, please consider giving us a star and citing our report.
```
@misc{xiao2024clusteringbased,
    title={Clustering-based Learning for UAV Tracking and Pose Estimation},
    author={Jiaping Xiao and Phumrapee Pisutsin and Cheng Wen Tsao and Mir Feroskhan},
    year={2024},
    eprint={2405.16867},
    archivePrefix={arXiv},
    primaryClass={cs.RO}
}
```


## Methodology
![CVPR2024_UG2_Poster(NTU-ICG)](https://github.com/NTU-ICG/Drone-3D/assets/19664995/0c13fe81-ab40-449d-b759-05bb60651d5d)


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
