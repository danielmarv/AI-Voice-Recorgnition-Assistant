from datetime import datetime
from logging.config import listen
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# Speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) # 0 = male, 1 = female
activationWord = 'computer' # single word

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listner = sr.Recognizer()
    print('Listning for a command')
    
    with sr.Microphone() as source:
        listner.pause_threshold = 2
        input_speech = listner.listen(source)
             
    try:
        print('Recognizing speech...')
        query = listner.recognize_google(input_speech, language='en_gb') 
        print(f'The input speech was:{query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that ')
        print(exception)   
        return 'None'
    
    return query 

def search_wikipedia(query = ''):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print(exception)
        return 'No results received'
    try:
        wikipedia = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.option[0])
    print(wikiPage.title)        
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

# Main loop
if __name__ == '__main__':
    speak('All systems nominal.')
    
    while True:
        # Parse as a list
        query = parseCommand().lower().split()
        
        if query[0] == activationWord:
            query.pop(0)
            
            # List commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, all.')
                else:
                    query.pop(0) # Remove say
                    speech = ' '.join(query)
                    speak(speech)  
                    
            # Navigation
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening....')
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)
                
            # Wikipedia
            if query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Querying the universal databank.')