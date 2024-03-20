#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os

def image_callback(msg):

    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")

    except CvBridgeError as e:
        print(e)

    else:

        seq = str(msg.header.seq)
        secs = str(msg.header.stamp.secs)
        nsecs = str(msg.header.stamp.nsecs).zfill(9)
        frame_id = str(msg.header.frame_id)

        save_directory = 'saved_images'

        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        filename = os.path.join(save_directory, f"{secs}.{nsecs}.{frame_id}.{seq}.jpeg")
        
        if not os.path.exists(filename):
            cv2.imwrite(filename, cv2_img)
            print(f"Saved image {filename}")

if __name__ == '__main__':

    try:
        rospy.init_node('image_saver', anonymous=True)
        bridge = CvBridge()
        image_sub = rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
