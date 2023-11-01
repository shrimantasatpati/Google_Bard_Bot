from bardapi import Bard 
import os 
from dotenv import load_dotenv 
import gradio as gr
import pyttsx3
import threading
from gtts import gTTS
from io import BytesIO
import pygame
import time


pygame.init()
pygame.mixer.init()
# sound.seek(0)

# engine = pyttsx3.init()
# engine.startLoop(False)

load_dotenv() 
token = os.getenv("BARD_API_KEY") 
bard = Bard(token=token) 
# result = bard.get_answer("what is the current stock price of NvDA?") 
# print(result) 


def speak(text, language='en'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    return mp3_fo

# def text_to_speech(message):
#     sound = speak("Python is cool always")
#     pygame.mixer.music.load(sound, 'mp3')
#     pygame.mixer.music.play()
#     time.sleep(5)


def bard_response(message, history):
    result = bard.get_answer(message) 
    print(result)
    sound = speak(result['content'])
    pygame.mixer.music.load(sound, 'mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    # t1 = threading.Thread(target=text_to_speech, args=(message,))
    # t1.start()
    return result['content']

demo = gr.ChatInterface(bard_response)

if __name__ == "__main__":
    demo.launch()
    print("hello")
