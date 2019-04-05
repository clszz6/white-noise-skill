from mycroft import MycroftSkill, intent_file_handler


class WhiteNoise(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('noise.white.intent')
    def handle_noise_white(self, message):
        self.speak_dialog('noise.white')


def create_skill():
    return WhiteNoise()

