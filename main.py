import sys
import os
import numpy as np
import cv2
import argparse
import torch
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

root = './'
ckpt_dir = os.path.join(root, 'ckpt')
log_dir = os.path.join(root, 'log')


''' Step 2. Train the network '''
parser = argparse.ArgumentParser()
parser.add_argument('--nepoch', type=int, default=20, help='number of epochs to train for')
parser.add_argument('--batch_size', type=int, default=1, help='batch size')
parser.add_argument('--num_workers', type=int, default=16, help='number of frames extracted from each video')
parser.add_argument('--lr', type=float, default=0.00001, help='')

parser.add_argument('--name', type=str, default='test',  help='experiment name for log')
parser.add_argument('--config_path', type=str, default='configs/yaml/oliver.yaml')


parser.add_argument('--ckpt_dir', type=str, default=ckpt_dir)
parser.add_argument('--log_dir', type=str, default=log_dir)


parser.add_argument('--ckpt_epoch_freq', type=int, default=1, help='')

parser.add_argument('--load_ckpt_path', type=str, default='')



if __name__=="__main__":
    root_dir = r'/mnt/chongqinggeminiceph1fs/geminicephfs/security-others-common'
    if not os.path.exists(root_dir):
        root_dir = '/mnt/cephfs'
    os.environ['ROOT_DIR'] = root_dir
    from trainer import Trainer
    opt_parser = parser.parse_args()
    model = Trainer(opt_parser)
    model.run()
