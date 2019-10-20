from twilio.rest import Client
import cgi
import cgitb #found this but isn't used?

inputs = cgi.FieldStorage()

first_name = inputs.getvalue('first_name').capitalize()
last_name  = inputs.getvalue('last_name').capitalize()

# Your Account SID from twilio.com/console
account_sid = "ACa3ee54b5030f3a2b427107e4ff8517af"
# Your Auth Token from twilio.com/console
auth_token  = "5f5479d1ea747a53454b61d812376cc4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14074373965",
    from_="+12052930681",
    body="your name is", first_name, last_name)

print(message.sid)





print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Your name is {}. {} {}</h2>".format(last_name, first_name, last_name))
print ("</body>")
print ("</html>")
