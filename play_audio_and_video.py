import cv2
from playsound import playsound
from multiprocessing import Process
import time

def play_audio_video(curr_path, iteration):
    # path to files, then concat with file names
    blur_val, brightness_val, turn_length = 501-(100*iteration), 0+(40*iteration), 83*(2**iteration)

    # while(guessing):
        # start a new video each loop, create a process of playing the audio
    video = cv2.VideoCapture(curr_path)
    p = Process(target=playsound, args=(curr_path,))

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

    # terminate the process for audio and destroy video window
    p.terminate()
    video.release()
    cv2.destroyWindow('Video')