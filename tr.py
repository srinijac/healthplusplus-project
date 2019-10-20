from twilio.rest import Client
import cgi
import cgitb #found this but isn't used?
cgitb.enable()

form = cgi.FieldStorage()

first = form.getvalue('first_name')
print(first)
last = form.getvalue('last_name')

# Your Account SID from twilio.com/console
account_sid = "ACa3ee54b5030f3a2b427107e4ff8517af"
# Your Auth Token from twilio.com/console
auth_token  = "5f5479d1ea747a53454b61d812376cc4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14074373965",
    from_="+12052930681",
    body=("your name is " + str(type(first))))

print(message.sid)
