import pyaudio
import speech_recognition as sr
import youtube_dl
mic = sr.Microphone(1)
mic
recog = sr.Recognizer()
recog
def ytDownload(URL):
    video_url = URL
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False, 
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
i=0
with mic as source:
 for i in range(10):
  print("listening")
  audio = recog.listen(source)
  try:
   Speech=recog.recognize_google(audio,language='th')
   print("you said: ",Speech)
   if 'สวัสดี' in Speech:
       print("สวัสดีครับ มีอะไรให้ช่วยไหมครับ")                  
   elif 'ตอนนี้' in Speech and 'หมอ' in Speech:
       print("กำลังติดต่อกับคุณหมอให้นะครับ")
       avi=input("คุณหมอว่างไหม")
       if avi=='yes' or avi=='Y'or avi=='y':
           print("คุณหมอว่างครับ")
       else:
           print("คุณหมอยังไม่ว่างครับ")
   elif 'เพลง' in Speech:
       URL=input("สามารถเลือกได้ครับ อยากจะฟังเพลงอะไรครับ(URL): ")
       ytDownload(URL)
   elif 'ใช้ App ยังไง' in Speech :
       print("ให้ผู้ป่วยทำท่าตามแอนิเมชัน จากนั้นแอปจะแสดงจำนวนครั้งที่ทำ และเวลาที่ใช้ในการบำบัด เพื่อที่จะปรึกษากับนักบำบัด")
   else:
        print("ขอโทษด้วยฉันไม่เข้าใจ")
  except:
   pass