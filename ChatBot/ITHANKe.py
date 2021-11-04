import youtube_dl

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

def ChatBot(Speech):
    if 'สวัสดี' in Speech:
        print("สวัสดีครับ มีอะไรให้ช่วยไหมครับ")
    elif 'หมอ' in Speech and 'กี่โมง' in Speech:
        print('กำลังสอบถามคุณหมอให้นะครับ')
        time=input('หมอว่างกี่โมง: ')
        print('คุณหมอจะว่างตอน ', time)                  
    elif 'หมอ' in Speech and 'ว่าง' in Speech:
        print("กำลังติดต่อกับคุณหมอให้นะครับ")
        avi=input("คุณหมอว่างไหม")
        if avi=='yes' or avi=='Y'or avi=='y':
            print("คุณหมอว่างครับ")
        else:
            print("คุณหมอยังไม่ว่างครับ")
    elif 'เพลง' in Speech:
        URL=input("สามารถเลือกได้ครับ อยากจะฟังเพลงอะไรครับ(URL): ")
        ytDownload(URL)
    elif 'App' in Speech and 'ยังไง' in Speech:
        print("ให้ผู้ป่วยทำท่าตามแอนิเมชัน จากนั้นแอปจะแสดงจำนวนครั้งที่ทำ และเวลาที่ใช้ในการบำบัด เพื่อที่จะปรึกษากับนักบำบัด")
    elif 'บำบัด' in Speech and 'ยังไง' in Speech:
        print('เดียวแอปบอกขณะการบำบัดครับ')
    else:
        print("ขอโทษด้วยฉันไม่เข้าใจ")

