
This README is meant for developers

Requirements:
Twilio Account/Number
Twilio Installed
Python Installed
ngrok Installed
Flask Installed


This chatbot is able to provide the covid 19 statistics on all countries.


To use it you need to run the code in the terminal. You will recieve a link from that, and you need to paste that link after typing 'ngrok http' into the ngrok terminal.
The ngrok terminal will give you an ngrok ".io" link. You need to paste that link into the "A message comes in" webhook url spot of your twilio number and then add a "/sms" to the end.
That's it! Now it will work with your own twilio number.
Now you need to text the name of a country to your Twilio phone number.