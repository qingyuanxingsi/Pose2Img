# -*- coding: utf-8 -*-

import numpy as np
import os

def compute_root_node(npy_base):
    cnt = 0
    sum_result = np.zeros(2)
    for npy_file in os.listdir(npy_base):
        kp_137 = np.load(os.path.join(npy_base,npy_file))
        sum_result += kp_137[:2,1]
        cnt +=1
        # print(cnt)
        if cnt == 200:
            break
    return sum_result/cnt

if __name__ == "__main__":
    npy_base = "data/luo/keypoints"
    print(compute_root_node(npy_base))

