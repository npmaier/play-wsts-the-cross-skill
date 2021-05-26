from mycroft import MycroftSkill, intent_file_handler


class PlayWstsTheCross(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cross.the.wsts.play.intent')
    def handle_cross_the_wsts_play(self, message):
        self.speak_dialog('cross.the.wsts.play')


def create_skill():
    return PlayWstsTheCross()

