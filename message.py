class Message:
    def __init__(self, username, text):
        self.username = username
        self.text = text
    def change_text(self, text):
        self.text = text
        self.__log_change_text()
    def __log_change_text(self):
        print('succesfully change text')
class Emoji(Message):
    def smile(self):
        self.text += ':)'