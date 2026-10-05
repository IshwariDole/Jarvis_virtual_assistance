import speech_recognition as sr
import webbrowser
import pyttsx3


# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processs_command(command):
    print(command)

if __name__ == "__main__":
    speak("Initializing Jarvis.........")
    while True:
        # Listen for wake word jarvis
        r = sr.Recognizer()
       


        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source,timeout=2,phrase_time_limit=1)
            command = r.recognize_google(audio)
            if (command.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("JArvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processs_command(command)
            print(command)
        except Exception as e:
            print("Error; {0}".format(e))
