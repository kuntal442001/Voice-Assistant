import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os



def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...........")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing .........")
            audio_data = recognizer.recognize_google(audio)
            audio_data = audio_data.lower()
            print(audio_data)
            return audio_data
        except sr.UnknownValueError:
            print("Not understanding")
            return None


def textsp(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Set voice only once
    engine.say(x)  
    engine.runAndWait()     


if __name__ == '__main__':
    data = sptext()  # Save speech result
    if data and "hey lambda" in data:  # Check for valid data and "hey lambda"
        while True:     
            data = sptext()
            if data:  # Ensure there's valid input
                if "your name" in data:
                    name = "My name is Lambda"
                    textsp(name)
                elif "how old are you" in data:
                    age = "I am 35 years old."
                    textsp(age)  
                elif "what is the time" in data:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    textsp(str(time))       
                elif "open youtube" in data:
                    webbrowser.open("https://www.youtube.com/")   
                elif "joke" in data:
                    joke_rand = pyjokes.get_joke(language="en", category="all")
                    print(joke_rand)
                    textsp(joke_rand)
                elif "play music" in data:
                    music = r"C:\Users\kuntal\Downloads"
                    list_song = os.listdir(music)
                    if list_song:
                        print(list_song)
                        os.startfile(os.path.join(music, list_song[3]))  # Play a specific song
                    else:
                        textsp("No music found.")
                elif "exit" in data:
                    textsp("Thank you.")
                    break
    else:
        print("Thanks.")
