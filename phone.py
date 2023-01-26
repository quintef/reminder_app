from twilio.rest import Client
import schedule
import time
import datetime
# Account SID and Auth Token from twilio.com/console
account_sid = 'AC70a74706fc4f2a4b34355cf9a91a928e'
auth_token = '3cef55d3d7ec5a73e1425e9a8f8d5c5d'

    # Your phone number and the number you want to send the message to
from_number = '+18885271437'
to_number = '+18328009212'
info = []
def send_message():
    account_sid = info[0]
    auth_token= info[1]
    from_number = info[2]
    to_number = info[3]

    print ("saddssddddddddddddddddddddddddddddddddddddddddddddd")
    client = Client(account_sid, auth_token)
    message = 'Hello, this is a test message from Python'
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number)
    print(message.sid)

def phoneSetup(information):   

    global info 
    info = information
    print(info)
    # Get the current time
    now = datetime.datetime.now()

    # Set the scheduled time
    scheduled_time = datetime.datetime(now.year, now.month, now.day, 0, 10, 0)
    # Wait until the scheduled time

    print(scheduled_time,now)
    print((scheduled_time - now).total_seconds())
    time.sleep((scheduled_time - now).total_seconds())

    

    # Call the function
    send_message()




