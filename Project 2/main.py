import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice (0 for male, 1 for female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    """Process the spoken command"""
    print(f"Processing command: {command}")
    command = command.lower()
    if "open google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in command:
        speak("Opening Facebook...")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in command:
        speak("Opening Twitter...")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in command:
        speak("Opening Instagram...")
        webbrowser.open("https://www.instagram.com")
    elif "open github" in command:
        speak("Opening GitHub...")
        webbrowser.open("https://www.github.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn...")
        webbrowser.open("https://www.linkedin.com")
    elif "open stackoverflow" in command:
        speak("Opening Stack Overflow...")
        webbrowser.open("https://www.stackoverflow.com")
    elif "open chatgpt" in command:
        speak("Opening ChatGPT...")
        webbrowser.open("https://www.openai.com/chatgpt")
    elif "open grok" in command:
        speak("Opening Grok...")
        webbrowser.open("https://www.grok.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        speak(f"Playing {song} on YouTube...")
        webbrowser.open(link)
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == '__main__':
    speak("Initializing Friday....")
    
    while True:
        print("\nRecognizing wake word...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
                print("Listening for 'Friday'...")
                audio = recognizer.listen(source, timeout=8, phrase_time_limit=5)  # Increased time limits
            
            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")

            if "friday" in word.lower():
                speak("Yes, I am here sir! How can I help you?")
                
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Friday Active... Listening for command.")
                    audio = recognizer.listen(source, timeout=8, phrase_time_limit=5)

                # Recognize the command
                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")

                processCommand(command)  # Process the command

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
        except sr.RequestError:
            print("API unavailable. Check your internet connection.")
        except Exception as e:
            print(f"Error: {e}")
