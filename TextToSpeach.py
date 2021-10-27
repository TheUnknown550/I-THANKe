import pyaudio
import speech_recognition as sr
mic = sr.Microphone(1)
mic
recog = sr.Recognizer()
recog
with mic as source:
 while True:
  print("listening")
  audio = recog.listen(source)
  print("Calibrating")
  try:
   print("you said: ",recog.recognize_google(audio,language='th'))   
  except:
   continue