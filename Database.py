import pyrebase

class Database:
    def __init__(self):
        self.config =  {
        # firebase realtime database configuration
        }
        self.firebase = pyrebase.initialize_app(self.config)
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        
        
    def Create(self, email, password):
        print("Eroor where",email,password)
        self.auth.create_user_with_email_and_password(email,password)
        print("Erro1")
        
    def Login(self, email,password):
        self.auth.sign_in_with_email_and_password(email,password)
        print('Aybo')





if __name__ == "__main__":
    # This code will only run if the file is executed directly,
    # not when imported as a module
    pass