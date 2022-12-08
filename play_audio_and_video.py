import cv2
from playsound import playsound
from multiprocessing import Process
import time
import os
import sys
from moviepy.editor import VideoFileClip

def play_audio_video(curr_path, iteration, name, unblurred=False):
    # path to files, then concat with file names
    if not unblurred:
        blur_val, brightness_val, turn_length = 501-(100*iteration), 0+(40*iteration), 83*(2**iteration)
    else:
        blur_val, brightness_val, turn_length = 1, 200, 83*(6)

    video = cv2.VideoCapture(curr_path)
    p = Process(target=playsound, args=(f"audio_clips/{name}.mp3",))

    if f"{name}.mp3" not in os.listdir('audio_clips'):
        convert_video_to_audio_moviepy(curr_path, name)

    if (video.isOpened() == False):
        print('An Error occurred while opening! Kindly check again.')

    p.start()
    # little delay because multiprocessing module takes half a second to actually play audio
    time.sleep(0.5)
    for _ in range(turn_length):
        ret, frame = video.read()
        if ret == True:
            frame = cv2.blur(frame, (blur_val, blur_val))
            frame = cv2.normalize(frame, frame, brightness_val, 0, cv2.NORM_MINMAX)

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        else:
            break
        time.sleep(0.01)
    # terminate the process for audio and destroy video window
    p.terminate()
    video.release()
    cv2.destroyWindow('Video')

def convert_video_to_audio_moviepy(video_file, name, output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"audio_clips/{name}.{output_ext}")


if __name__ == '__main__':
    play_audio_video('songs\Easy\Attack on Titan-Guren no Yumiya.mp4', 1, "aot")