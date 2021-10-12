# Program to convert speech to text
# Author @inforkgodara

import speech_recognition as speech
read = speech.Recognizer()

audio_in = speech.Microphone()

print('start')
with audio_in as source:
    text = read.listen(source)
print('end')
print(read.recognize_google(text))