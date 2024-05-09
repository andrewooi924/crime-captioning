import os
from c3d import *
from classifier import *
from utils.visualization_util import *



def run_demo():

    video_folder = os.listdir(cfg.input_folder)
    for i in range(len(video_folder)):
        video_name = os.path.basename(video_folder[i]).split('.')[0]
        video_path = os.path.join(cfg.input_folder, video_name + '.mp4')
        # read video
        video_clips, num_frames = get_video_clips(video_path)

        print("Now processing: ", video_name)   
        print("Number of clips in the video : ", len(video_clips))

        # build models
        feature_extractor = c3d_feature_extractor()
        classifier_model = build_classifier_model()

        print("Models initialized")

        # extract features
        rgb_features = []
        for i, clip in enumerate(video_clips):
            clip = np.array(clip)
            if len(clip) < params.frame_count:
                continue

            clip = preprocess_input(clip)
            rgb_feature = feature_extractor.predict(clip)[0]
            rgb_features.append(rgb_feature)

            print("Processed clip : ", i)

        rgb_features = np.array(rgb_features)

        # bag features
        rgb_feature_bag = interpolate(rgb_features, params.features_per_bag)
        save_path = os.path.join(cfg.output_folder, video_name + '.txt')
        np.savetxt(save_path, rgb_feature_bag.squeeze())
        print("Finished processing: ", video_name)
        print("\n")


if __name__ == '__main__':
    run_demo()