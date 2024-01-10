import pyttsx3

with open('file.txt', 'r') as instasamka_file:
    samka = instasamka_file.read()

print(samka)

speaker = pyttsx3.init()
speaker.setProperty('rate', 250)
speaker.say(samka)
speaker.runAndWait()
speaker.stop()