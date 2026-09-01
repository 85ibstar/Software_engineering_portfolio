import re

class RegEx_validation:

    def __init__(self, given_emailAddress: str, given_password: str, given_phone_number):
        # defined the attributes, the user inputs
        self.emailAddress = given_emailAddress
        self.password = given_password
        # passes in None for log-in
        if given_phone_number is not None :
            self.phone_number = str(given_phone_number)
        else:
            self.phone_number = given_phone_number


    def email_validation(self):
        # grouped in              (group 1)      (group 2)     (group 3)
        pattern = re.compile(r"([a-zA-z0-9]+)@([a-zA-Z-]+)\.(com|de|org)")
        # looks for in the set all alphabets and numbers 1 or more, -, @, any alphabets 1 or more, -, ".", either com or de or org

        # checks whether the string matches the pattern
        if bool(re.fullmatch(pattern,self.emailAddress)):
            return True
        else:
            return False


    def pass_entry_validation(self):

        pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
        # ensures the pattern is 8 or more characters long, and 1 or more: special characters, digits and letters

        if bool(re.fullmatch(pattern,self.password)):
            return True
        else:
            return False


    def phone_number_validation(self):

        pattern = re.compile(r"0\d{10}")
        # pattern starts with 0, followed by 10 other numbers

        if bool(re.fullmatch(pattern, self.phone_number)):
            return True
        else:
            return False


    def register_validation(self):
        if self.phone_number_validation() and self.pass_entry_validation() and self.email_validation():
            return True
        else:
            return False

    def login_validation(self):
        if self.email_validation() and self.pass_entry_validation():
            return True
        else:
            return False