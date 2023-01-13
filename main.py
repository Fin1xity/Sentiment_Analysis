import speech_recognition 
import pyttsx3
import pyaudio
from textblob import TextBlob

def getPolarity(text):
   return TextBlob(text).sentiment.polarity



recognizer = speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text =  text.lower()
            break

    except speech_recognition.UnknownValueError():
        continue

polarity_score = getPolarity(text)
if polarity_score == 0:
    print("Neutral")
elif polarity_score == 1:
    print("Very much positive")
elif polarity_score == -1:
    print("Very much negative")
elif polarity_score > 0 and polarity_score < 1:
    print("Pretty much positive")
elif polarity_score < 0 and polarity_score > -1:
    print("Pretty much negative")
