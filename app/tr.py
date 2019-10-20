from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa3ee54b5030f3a2b427107e4ff8517af"
# Your Auth Token from twilio.com/console
auth_token  = "5f5479d1ea747a53454b61d812376cc4"

client = Client(account_sid, auth_token)

def addnumber(num):
    validation_request = client.validation_requests \
                           .create(
                                friendly_name='Contact Number',
                                phone_number=str(num)
                            )
    print(validation_request.friendly_name)

def sendsms(message, number):
    message = client.messages.create(
        to=str(number),
        from_="+12052930681",
        body=str(message))
    print(message.sid)
