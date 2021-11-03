class User():
    def __init__(self, username: str, email: str, firstName: str, lastName: str, dateRegistered: str):
        self._username = username
        self._email = email
        self._firstName = firstName
        self._lastName = lastName
        self._dateRegistered = dateRegistered

    @property
    def firstName(self):
        return self._firstName

    @property
    def lastName(self):
        return self._lastName

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def dateRegistered(self):
        return self.dateRegistered

    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName
