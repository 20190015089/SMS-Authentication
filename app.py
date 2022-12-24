from eightAM.utils import Utils
from eightAM.send_sms import sendSMS
from eightAM.auth import Authenticator

secret = Authenticator()
secretNumebr = secret.generate()

ip = Utils.getiP()
city = Utils.getLocation(ip, 'city')
ccc = Utils.getLocation(ip, 'country_calling_code')

usrNum = input(f'Enter your phone number: {ccc}')
toNum = f'{ccc}{usrNum}'

verificationMessage = f"Your Authentication Code is {secretNumebr}"
sendSMS(verificationMessage, toNum, "Send Authintication Code", ip)

usr_tries = 0
tries = 3

while usr_tries < tries:
    usr_tries += 1
    usr_input = int(input('Enter your authentication code: '))

    if secret.verify(usr_input, secretNumebr) == True:
        message = f"Logged in Successfully from {city}"
        sendSMS(message, toNum, "Logged in Successfully", ip)
        break
    elif usr_tries < 3:
        print("Wrong Authentication Code")
    
else:
    print("Account Locked")
    message = f"Account Locked, You've entered the wrong authintication code for {str(tries)} times. Try again later"
    sendSMS(message, toNum, "Account Locked", ip)
