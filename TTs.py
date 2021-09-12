# pip install speechrecognition
# pip install gTTs
# pip install playsound

import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import uuid

voice_speak = 0
from pygame.mixer import Sound


# 음성 출력
def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = str(uuid.uuid4()) + ".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    # Sound.read(filename)
    # Sound.play()

#speak('안녕하세요 이로드 입니다.')

'''
# pip install speechrecognition
# pip install gTTs
# pip install playsound

import subprocess
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import uuid

voice_speak = 0
from pygame.mixer import Sound


def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = str(uuid.uuid4()) + ".mp3"
    tts.save(filename)
    #playsound.playsound(filename)
    subprocess.Popen(['omxplayer','-b',filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    #Sound.read(filename)
    #Sound.play()
speak('안녕하세요 이로드 입니다. 이기기는 시청각장애인분들의 길이 되어주기 위하여 제작하였습니다.')


'''
