# -*- coding: utf-8 -*-

import os
import shutil
from tqdm import tqdm

kp_base = r'/mllab/codehub/SpeechDrivesTemplates/datasets/speakers/luo/tmp/cleaned_pose_2d/demo'
img_base = r'/mllab/codehub/SpeechDrivesTemplates/datasets/speakers/luo/frames/demo'
copy_dir = r'/mnt/chongqinggeminiceph1fs/geminicephfs/security-others-common/doodleliang/Pose2Img/data/luo'

for file in tqdm(os.listdir(kp_base)):
    cur_path = os.path.join(kp_base, file)
    name, ext = os.path.splitext(file)
    img_path = os.path.join(img_base, name + '.jpg')
    kp_dst = os.path.join(copy_dir, 'keypoints', file)
    img_dst = os.path.join(copy_dir, 'imgs', name + '.jpg')
    shutil.copy(cur_path, kp_dst)
    shutil.copy(img_path, img_dst)
