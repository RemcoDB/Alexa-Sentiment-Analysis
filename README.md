# Alexa-Sentiment-Analysis
--Project by Oxyma B.V. in Rotterdam

This is one of many methods to connect a Sentiment analysis to your Amazon Echo. This project uses a local server with Phusion Passenger and the script was written in Python. 

For Passenger specific servers you must add a passenger_wsgi.py, which connects to your main python script (lamdba_function.py).
A useful debugging trick when using Passenger is adding an empty textfile tmp/always_restart.txt to constantly update your edits to the script.
For Python users: Install Pip, flask, flask-ask and your favorite sentiment API. I used aylienapiclient and afterwards the IBM Watson API with Bluemix. The latter is payed. 

Flask-ask is a core-module for Alexa projects. Split your script into intents, launchrequests, endrequests etc. as what AWS Lambda does for you. 

Configure your program on the Amazon developer website. I have included the interation model. Don't forget to convert your certificate to X.509 for the SSL certificate form. This is server-specific of course, but I needed to convert mine before anything worked (405 errors). 

The script connects to the Philips HUE lights through an IFTTT link created by the Maker, this creates a trigger which responds to simple 'get' commands from the server. Associate each colour to a specific colour for example. 

This is a basic script. Once the connection between Alexa and your server works, the world is your oyster. 

I started with AWS Lambda, but there was some confusion with the VPC's. Because of this, I couldn't perform HTTPS 'get' calls. 

Good luck scripting.

Remco de Bruijn
Data Scientist Oxyma B.V.

