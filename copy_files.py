# -*- coding: utf-8 -*-

import os
import shutil

kp_base = r'/mllab/codehub/SpeechDrivesTemplates/datasets/speakers/xiang/tmp/rescaled_pose_2d/xiang'
img_base = r'/mllab/codehub/SpeechDrivesTemplates/datasets/speakers/xiang/frames/xiang'
copy_dir = r'/mllab/codehub/Pose2Img/data/xiang'

for file in os.listdir(kp_base):
    cur_path = os.path.join(kp_base, file)
    name, ext = os.path.splitext(file)
    img_path = os.path.join(img_base, name + '.jpg')
    kp_dst = os.path.join(copy_dir, 'keypoints', file)
    img_dst = os.path.join(copy_dir, 'imgs', name + '.jpg')
    shutil.copy(cur_path, kp_dst)
    shutil.copy(img_path, img_dst)
