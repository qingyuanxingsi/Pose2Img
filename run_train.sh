cd /mnt/cephfs/doodleliang/Pose2Img && \
python main.py \
--name xiang \
--config_path configs/yaml/xiang.yaml \
--batch_size 2
--load_ckpt_path ckpt/xiang/ckpt_last.pth