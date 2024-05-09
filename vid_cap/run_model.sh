#Uncomment the test argument if you don't want to train the model (only for testing)
#Set demo to True to test the model on individual samples
TF_XLA_FLAGS=--tf_xla_cpu_global_jit \
XLA_FLAGS=--xla_hlo_profile \
CUDA_VISIBLE_DEVICES=1 \
python train_model.py \
    --corpus vid_cap/Files/ucfc-vd_Corpus.pkl \
    --ecores vid_cap/ResnetFeatures/Scaled_ResNeXt \
    --tag    vid_cap/ucfcvd_e1000_tag_feats.npy \
    --ref    vid_cap/Files/ucfc-vd_ref.pkl \
    --demo   True
    --test   vid_cap/saves/UCF-CAP-best.ckpt \
    > test.log
