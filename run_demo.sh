SPEAKER=luo
python inference.py \
   --cfg_path configs/yaml/$SPEAKER.yaml \
   --name ${SPEAKER}_demo \
   --npz_path target_pose/$SPEAKER/epoch0-DEMO-step1.npz \
   --wav_path target_pose/$SPEAKER/epoch0-DEMO-step1.wav