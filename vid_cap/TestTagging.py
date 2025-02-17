import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#import tensorflow as tf
import numpy as np
from Tag_Net import TagNet
import os

def main():
    tagnet = TagNet()
    with tagnet.graph.as_default():
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        sess = tf.Session(config=config, graph=tagnet.graph)
        saver = tf.train.Saver()
        saver.restore(sess, 'vid_cap/saves/ucfcvd_tag_model_1000_resnext.ckpt')

        data = np.load('vid_cap/ResnetFeatures/Scaled_ResNeXt.npy')

        batch_size = 10
        # no_of_videos = len(os.listdir("vid_cap/AnomalyFrames/"))
        semantic = np.zeros([1, 300], np.float32)
        for idx in range(95):
            wanted_ops = [tagnet.pred]
            feed_dict = {tagnet.z: data[idx*batch_size:(idx+1)*batch_size], 
                         tagnet.rate: 1}

            res = sess.run(wanted_ops, feed_dict)   
            semantic[idx*batch_size:(idx+1)*batch_size] = res[0]

        np.save('vid_cap/ucfcvd_e1000_tag_feats', semantic)
        print("Successfully generated tagging vector")


if __name__ == "__main__":
    main()
