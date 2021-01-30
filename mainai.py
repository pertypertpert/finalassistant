import pyttsx3
import speech_recognition as sr
import datetime
import random
import re
import webbrowser
import json
import speedtest
import notetaker
import os
# installing PyAudio is also necessary with 'pip install pyaudio'
def open_documentation(tech):
    print("Opening documentation for {}".format(tech))
    speak("Opening documentation for {}".format(tech))
    webbrowser.open_new_tab("https://devdocs.io/{}/".format(tech.lower()))


def wikipedia_search(query):
    try:
        underscorer=query.replace(' ', '_')
        summary_result = webbrowser.open_new_tab(f'https://en.wikipedia.org/wiki/{underscorer}')
        print(f'opening wikipedia page for {query}')
        speak(f'opening wikipedia page for {query}')
    except:
        print("Unfortunately I wasn't able to retrieve this information.")
        speak("Unfortunately I wasn't able to retrieve this information.")
def tell_wifi_speed():
    speak("Testing speed")

    st = speedtest.Speedtest()

    # Dividing by 1e+6 to convert to megabytes
    download_speed = int(st.download() / 1000000)
    upload_speed = int(st.upload() / 1000000)

    servers = []
    st.get_servers(servers)
    ping = st.results.ping

    print("Download speed: ", download_speed)
    print("Upload speed: ", upload_speed)
    print("Ping: ", ping)

    speak("Your download speed is about {} megabytes. Upload speed is about {} megabytes. Ping is {}".format(
        download_speed, upload_speed, ping))


def tell_time():
    # Return will be as such: 2021-01-05 14:26:17.705949
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    print(time)
    speak("The time is " + hour + "Hours and" + min + "Minutes")
def tell_date():
    # Return will be as such: 2021-01-05 14:26:17.705949
    date = str(datetime.datetime.now())

    month_number = int(date[5:7].lstrip('0'))
    day_number = int(date[8:10].lstrip('0'))
    year = date[:4]

    date_speech = "Today is the {} of {} of {}.".format(data["days"][str(day_number)],
                                                        data["months"][str(month_number)], year)
    print(date_speech)
    speak(date_speech)


from mathOperations import math_speech
f = open('storage files\\repliesdata.json')
data = json.load(f)


def open_page(page):
    try:
        print("Opening {}".format(page))
        speak("Opening {}".format(page))
        webbrowser.open_new_tab(data.pages[page])
    except:
        print("Unfortunately I can't open {} yet. Open command references for available options.".format(page))
        speak("Unfortunately I can't open {} yet. Open command references for available options.".format(page))

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


class AI:
    def __init__(self):
        self.name = "AI"
        self.user_name = None

        # reading the content from repliesdata.json into a python dictionary
        
    def take_query(self, typen):
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

                print("You said: ", instruction)

                if typen == 'normal':
                    # Looking for trigger words
                    if "bye" in instruction or "see you later" in instruction or "need to run" in instruction or "got to run" in instruction or "got to go" in instruction or "catch you later" in instruction:
                        goodbye_call = data["goodbyes"][str(random.randint(0, len(data["goodbyes"]) - 1))]
                        print(goodbye_call)
                        speak(goodbye_call)
                        exit()
                    elif "how are you" in instruction or "how's it going" in instruction or "what's up" in instruction:
                        print("I am doing great, and you?")
                        speak("I am doing great, and you?")
                        return
                    elif 'open all notes' in instruction:
                        webbrowser.open('note files')
                    elif "make a note" in instruction:
                        notetaker.Notetaker()
                    elif "time" in instruction:
                        tell_time()
                    elif "date" in instruction or " day" in instruction:
                        tell_date()
                    elif "who are you" in instruction or "what is your" in instruction:
                        print("I'm Cole, your virtual assistant for programming.")
                        speak("I'm Cole, your virtual assistant for programming.")
                    elif "don't" in instruction or "do not" in instruction:
                        print("Okay, I will not do so.")
                        speak("Okay, I will not do so.")
                    elif "marry me" in instruction and 'sudo' not in instruction:
                        speak("I'm sorry, I can only accept such requests from the super user.")
                    elif "sudo" in instruction and "marry me" in instruction:
                        speak("Of course super user! I'll be glad to spend my life with you!")
                    elif "Wi-Fi" in instruction or "internet" in instruction or "ping" in instruction:
                        tell_wifi_speed()
                    elif "how old are you" in instruction:
                        speak(
                            "I may be just a few weeks old, but I certainly do a lot more than others of my age.")
                    elif "documentation for" in instruction:
                        try:
                            technology_doc = re.search("documentation for (.*)", instruction)[1]
                            open_documentation(technology_doc)
                        except:
                            print("Please specify which documentation you need.")
                            speak("Please specify which documentation you need.")
                    elif "hey" in instruction or "hello" in instruction or "hi" in instruction:
                        hello_call = data["hellos"][str(random.randint(0, len(data["hellos"]) - 1))]
                        print(hello_call)
                        speak(hello_call)
                        return
                    elif "prime number" in instruction or "cosine" in instruction or "tangent" in instruction or "sine" in instruction or "√" in instruction or "square root" in instruction or "+" in instruction or "/" in instruction or "*" in instruction or "-" in instruction:
                        try:
                            math_operation = re.search("(what is )?(the )?(.*)", instruction.lower())[3]
                            math_results = math_speech(math_operation)
                            print(str(math_results))
                            speak(str(math_results))
                        except:
                            print("Please tell me what mathematical equation you want to perform.")
                            speak("Please tell me what mathematical equation you want to perform.")
                    elif "git cheat" in instruction:
                        print("Opening git cheat-sheet")
                        speak("Opening git cheat-sheet")
                        webbrowser.open_new_tab("https://training.github.com/downloads/github-git-cheat-sheet.pdf")
                    elif "search stack overflow for" in instruction.lower() or "search stackoverflow for" in instruction.lower():
                        try:
                            search_words = re.search("search stack overflow for (.*)", instruction.lower())[1]
                            print("Searching stackoverflow for ", search_words)
                            speak("Searching stackoverflow for {}".format(search_words))
                            webbrowser.open_new_tab(
                                "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                        except:
                            try:
                                search_words = re.search("search stackoverflow for (.*)", instruction.lower())[1]
                                print("Searching stackoverflow for ", search_words)
                                speak("Searching stackoverflow for {}".format(search_words))
                                webbrowser.open_new_tab(
                                    "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                            except:
                                print("Please tell me what you want to search for.")
                                speak("Please tell me what you want to search for.")
                    elif "search stack overflow" in instruction.lower() or "search stackoverflow" in instruction.lower():
                        try:
                            search_words = re.search("search stack overflow (.*)", instruction.lower())[1]
                            print("Searching Stackoverflow for ", search_words)
                            speak("Searching Stackoverflow for {}".format(search_words))
                            webbrowser.open_new_tab(
                                "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                        except:
                            try:
                                search_words = re.search("search stackoverflow (.*)", instruction.lower())[1]
                                print("Searching Stackoverflow for ", search_words)
                                speak("Searching Stackoverflow for {}".format(search_words))
                                webbrowser.open_new_tab(
                                    "https://stackoverflow.com/search?q={}".format(search_words.replace(' ', '+')))
                            except:
                                print("Please tell me what you want to search for.")
                                speak("Please tell me what you want to search for.")
                    elif "search youtube for" in instruction.lower():
                        try:
                            search_words = re.search("search youtube for (.*)", instruction.lower())[1]
                            print("Searching YouTube for ", search_words)
                            speak("Searching YouTube for {}".format(search_words))
                            webbrowser.open_new_tab(
                                "https://www.youtube.com/results?search_query={}".format(
                                    search_words.replace(' ', '+')))
                        except:
                            print("Please tell me what you want to search for.")
                            speak("Please tell me what you want to search for.")
                    elif "search youtube" in instruction.lower():
                        try:
                            search_words = re.search("search youtube (.*)", instruction.lower())[1]
                            print("Searching YouTube for ", search_words)
                            speak("Searching YouTube for {}".format(search_words))
                            webbrowser.open_new_tab(
                                "https://www.youtube.com/results?search_query={}".format(
                                    search_words.replace(' ', '+')))
                        except:
                            print("Please tell me what you want to search for.")
                            speak("Please tell me what you want to search for.")
                    elif "search for" in instruction:
                        try:
                            search_words = re.search("search for (.*)", instruction)[1].lower()
                            print("Searching for ", search_words)
                            speak("Searching for {}".format(search_words))
                            webbrowser.open_new_tab(
                                "http://www.google.com/search?q={}".format(search_words.replace(' ', '+')))
                        except:
                            print("Please tell me what you want to search for.")
                            speak("Please tell me what you want to search for.")
                    elif "I'm great" in instruction or "I'm okay" in instruction or "I'm good" in instruction:
                        print("Glad to hear!")
                        speak("Glad to hear!")
                    elif "I'm not great" in instruction or "I'm not okay" in instruction or "I'm not good" in instruction:
                        print("I'm sorry to hear.")
                        speak("I'm sorry to hear.")
                        return
                    elif "open" in instruction:
                        page = re.search("open (.*)", instruction)[1]
                        open_page(page.lower())
                        return
                    elif "what is" in instruction:
                        try:
                            search_query = re.search("what is (.*)", instruction)[1]
                            wikipedia_search(search_query)
                            return
                        except:
                            print("Please specify what you want to know about.")
                            speak("Please specify what you want to know about.")
                            return
                    elif "who is" in instruction:
                        try:
                            search_query = re.search("who is (.*)", instruction)[1]
                            wikipedia_search(search_query)
                            return
                        except:
                            print("Please specify who you want to know about.")
                            speak("Please specify who you want to know about.")
                            return
                    elif "what is my name" in instruction:
                        pass
                    else:
                        speak("i don't know how to reply to that yet")


            except Exception as error:
                print(error)
                print("Please repeat.")
                speak('please repeat')
                return "None"
def querytaker():
    AI.take_query(AI,'normal')
