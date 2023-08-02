import os
from twilio.rest import Client

TWILIO_NUMBER = "+18665083998"
MY_NUMBER = "+17742402535"
account_sid = os.environ.get('TWILIO_ACC_ID')
auth_token = os.environ.get('AUTH_TOKEN')


class NotificationManager:

    def send_text(self, message):
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_NUMBER)

        print(message.sid)
