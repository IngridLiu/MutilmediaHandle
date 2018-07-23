# 将视频的每一帧提取并保存

import os

import cv2
import cv2.cv as cv

from cfg import data_root, save_root


def get_videos_in_dir(dir_path, video_type):

    videos = os.listdir(dir_path)
    videos = filter(lambda x: x.endswith(video_type), videos)

    for video in videos:
        video = dir_path + video

    return videos

def handle_single_video(data_root, save_root, video):

    video_path = data_root + video

    video_name, video_type = video.split('.')
    os.mkdir(save_root + video_name)

    video_save_path = os.path.join(save_root, video_name) + '/'

    cap = cv2.VideoCapture(video_path)
    frame_count = 1
    success = True
    while (success):
        success, frame = cap.read()
        print('Read a new frame: ', success)

        params = []
        params.append(cv.CV_IMWRITE_PXM_BINARY)
        params.append(1)
        cv2.imwrite(video_save_path + video_name + "%s_%s_%d.ppm" % [video_save_path, video_name, frame_count], frame,
                    params)

        frame_count = frame_count + 1

    cap.release()


if __name__ == "name":
    video = ""
    handle_single_video(data_root, save_root, video)


