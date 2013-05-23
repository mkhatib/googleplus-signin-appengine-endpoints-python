from protorpc import messages


class Greeting(messages.Message):
    msg = messages.StringField(1)
