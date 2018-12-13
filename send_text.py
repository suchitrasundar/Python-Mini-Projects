from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC59d98e2db0be9a6524d944653d164305"
# Your Auth Token from twilio.com/console
auth_token  = "57d27e968c81f8e23fc508c3af8ea652"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19375030912", 
    from_="+13344686658",
    body="Suchitra Sundar")

print(message.sid)
