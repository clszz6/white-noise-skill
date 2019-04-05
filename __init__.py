from mycroft import MycroftSkill, intent_file_handler

from os.path import join, abspath, dirname
import os.path
import random
from adapt.tools.text.tokenizer import EnglishTokenizer
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_mp3
from mycroft.util.parse import fuzzy_match
from mycroft.util.parse import match_one
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *

class WhiteNoise(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('noise.white.intent')
    def handle_noise_white(self, message):
        self.speak_dialog('noise.white')


def create_skill():
    return WhiteNoise()

