import speech_recognition as sr
import webbrowser
import pyttsx3

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
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == '__main__':
    speak("Initializing Optimus....")
    
    while True:
        print("\nRecognizing wake word...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
                print("Listening for 'Optimus'...")
                audio = recognizer.listen(source, timeout=8, phrase_time_limit=5)  # Increased time limits
            
            word = recognizer.recognize_google(audio)
            print(f"You said: {word}")

            if "optimus" in word.lower():
                speak("Yes, I am here. How can I help you?")
                
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Optimus Active... Listening for command.")
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
