import speech_recognition as sr
import pyttsx3

instruction=''
def speak(audio):
    # getting a reference to a pyttsx3.Engine instance.
    engine = pyttsx3.init()
    # retrieving  the current value of engine property
    voices = engine.getProperty('voices')

    # setting voice to male
    engine.setProperty('voice', voices[0].id)

    # Method speaks the audio
    engine.say(audio)

    # Blocks while processing queued commands, necessary for hearing audio
    engine.runAndWait()

def takespeech():

    # This class is responsible for converting audio into text
    r = sr.Recognizer()

    # using the Microphone module from sr that will listen for a query
    with sr.Microphone() as source:
        # Energy threshold of 300 is recommended by SpeechRecognition's documentation (loudness of the file)
        r.energy_threshold = 300

        # How long it will wait after the user stops talking to consider the end of a sentence
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now trying to use Google Recognizer function that uses Google’s free web search API
        # This try except block will check if the words are recognized, else an exception will be handled
        try:
            print("Processing...")

            instruction = r.recognize_google(audio, language="en-in")
            return instruction
        except:
            speak('did not catch that')
            return

def Notetaker():
    speak("what is the heading")
    text =takespeech()
    heading = text
    with open('storage files\\newnote.txt', 'w')as file:
        file.write(heading)
    f = open(f"note files\\{heading}.note", "a")
    speak("any sub topic")
    text = takespeech()

    Nea = 0
    y = 90
    x = 0
    Neb = 0

    subtopic = text
    speak("what is the content")
    text = takespeech()
    content = text
    f.write("\n")
    f.write("Heading-")
    f.write(heading)
    f.write("\n")
    f.write("Subtopic-")
    f.write(subtopic)
    f.write(f'\n content-{content}')
    speak("anything else")
    els = takespeech()
    if els == "yes":
       speak("okay")
       content = takespeech()
       f.write(f'\n{content}')
    else:
        return

