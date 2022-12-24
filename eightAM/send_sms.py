import os
from twilio.rest import Client


def sendSMS(SMSmessage, toNum, purpose, ip):

  account_sid = "AC24e65831e5442b1e1b3d3bb183d98c96"
  auth_token = "ee95d9e62ffc51de47fc6058b6eaf3ed"
  client = Client(account_sid, auth_token)

  message = client.messages.create(
  body = SMSmessage,
  from_ = "+13854692391",
  to = toNum
  )

  if purpose == "Send Authintication Code":
      log = f"Sent to {toNum} for Authintication Code from {ip}, mSID -> {message.sid}"
  elif purpose == "Logged in Successfully":
      log = f"Sent to {toNum} for Logged In from {ip}, mSID -> {message.sid}"
  elif purpose == "Account Locked":
      log = f"Sent to {toNum} for Account Locked from {ip}, mSID -> {message.sid}"

  if not os.path.exists("mSID Log.txt"):
      with open("mSID Log.txt", "w") as l:
          l.write("")
  with open("mSID Log.txt", "a") as l:
      l.write(f"{log}\n")
