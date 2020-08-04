import speech_recognition as sr

     r = sr.Recognizer()
     with sr.Microphone() as source:
     audio = r.listen(source)
     text = r.recognize_google(audio, language='bn-BD')
     text2 = r.recognize_google(audio)


 while True:

     print("English: " + text2)
     print("Bangla: " + text)