from twilio.rest import Client
import mykeys

# the following line needs your Twilio Account SID and Auth Token
client = Client(mykeys.account_sid, mykeys.token)

client.messages.create(to=mykeys.number, 
                       from_="+18788471492",
                       body="The Playstation5 is on stock")
