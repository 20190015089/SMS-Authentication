import random

class Authenticator:

    def generate(self):
        secret = random.randint(100000, 999999)
        return secret

    def verify(self, usr_input, secret_number):
        if usr_input == secret_number:
            print("Access Granted")
            loggedin = True
            return loggedin