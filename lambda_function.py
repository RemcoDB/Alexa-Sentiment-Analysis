import logging
from flask import Flask
from flask_ask import Ask, request, session, question, statement
from aylienapiclient import textapi
import urllib2

MyApp = Flask(__name__)
ask = Ask(MyApp, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_text = 'Welcome to the Alexa Bringer of Light Project. Please say analyze, followed by a sentence you want analyzed.'
    return question(speech_text).reprompt(speech_text).simple_card('Github', speech_text)


@ask.intent('GetSentiment', convert={'Subject': str})
def hello_world(Subject):
    c = textapi.Client("##", "####")
    sentimentscore = c.Sentiment({'text': Subject})
    list_values = [v for v in sentimentscore.values()]
    polarity = list_values[0]
    polarity_confidence = int(list_values[2] * 100)
    subjectivity_confidence = int(list_values[3] * 100)
    #commence if statements:
    if Subject == 'christmas':
        #add easter egg      
        urllib2.urlopen("https://maker.ifttt.com/trigger#####").read()
        speech_text = "Merry Christmas " + \
                      "This is an easter egg"      
    elif Subject == 'reset' or Subject == 'reset the lights' or Subject == 'normal' or Subject == 'back to normal':
        #Reset the HUE lights      
        urllib2.urlopen("https://maker.ifttt.com/trigger#####").read()
        speech_text = "HUE Lights have been reset "                                             
    elif polarity == "neutral":
        # commence neutral lights
        urllib2.urlopen("https://maker.ifttt.com/trigger#####").read()
        urllib2.urlopen("https://maker.ifttt.com/trigger#####").read()
        reprompt_text = 'neutral!'
        speech_text = "We found a neutral sentiment for " + \
                         Subject + ", with a polarity confidence of " + \
                         str(polarity_confidence) + " %"
    elif polarity == 'positive':
        # commence positive lights
        urllib2.urlopen("https://maker.ifttt.com/trigger#####").read()
        speech_text = "We found a positive sentiment for " + \
                         Subject + ". With a subjectivity confidence of " + \
                         str(subjectivity_confidence) + " %"
        reprompt_text = "Positive!"
    elif polarity == 'negative': 
        # commence negative lights
        urllib2.urlopen("https://maker.ifttt.com/trigger#####").read()
        speech_text = "We found a negative sentiment for " + \
                         Subject + ", with a subjectivity confidence of " + \
                         str(subjectivity_confidence) + " %"
             
    
    should_end_session = False  
    return question(speech_text).reprompt(speech_text).simple_card('Github', speech_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say analyze, then some sentence to me. Then I will analyze it.'
    return question(speech_text).reprompt(speech_text).simple_card('Github', speech_text)


@ask.session_ended
def session_ended():
    return statement("")


if __name__ == '__main__':
    MyApp.run(debug=True)