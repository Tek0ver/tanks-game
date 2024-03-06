class Log:

    def __init__(self):

        self.active = True
        self.level = 0

        # TODO : add message for self.active = False
        self.log('Log is activated')

    def log(self, message: str, cat: str = None, level: int = 0):
        # TODO : add categories for logs

        if self.active:
            print(message)


log = Log()