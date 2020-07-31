#Pranav Bollineni

#7/25/20

#Made during Hack Cupertino 2020

#Importing modules
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json


#Parsing data from the Covid 19 API.
#Credit to Kyle Redelinghuys for building this API
r = requests.get('https://api.covid19api.com/summary')

data = r.text

parseData = json.loads(data)



#Recieves the text message from the user and decides what to respond with
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None).strip()

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    for c in parseData["Countries"]:
        if body in c["Country"]:
            a = "Country: {0}\n\nNew Cases: {1}\nTotal Cases: {2}\n\n\nNew Deaths: {3}\nTotal Deaths: {4}\n\n\nNew Recovered: {5}\nTotal Recovered: {6}".format(
                c["Country"], c["NewConfirmed"], c["TotalConfirmed"], c["NewDeaths"], c["TotalDeaths"], c["NewRecovered"], c["TotalRecovered"])
            resp.message(a)
    
    resp.message("Hi! Type the name of the country you want to see the stats of.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
