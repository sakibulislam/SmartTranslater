import speech_recognition as sr


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something!')
        audio = r.listen(source)
        print("processing....")
        text2 = r.recognize_google(audio)
        print("processing....compt")
        print("English: " + text2)
        print('Done!')









