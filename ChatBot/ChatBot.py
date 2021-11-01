import pyaudio
import speech_recognition as sr
import ITHANKe as IT
mic = sr.Microphone(1)
mic
recog = sr.Recognizer()
recog
with mic as source:
    while True:
        print("listening",end='\r')
        audio = recog.listen(source)
        print('Calibrating', end='\r')
        try:
            Speech=recog.recognize_google(audio,language='th')
            print("you said: ",Speech)
            if 'จบ' in Speech or 'หยุด' in Speech:
                print('รับทราบครับ')
                break
            IT.ChatBot(Speech)
            input('continue? ')
        except:
            pass