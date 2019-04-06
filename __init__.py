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
from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.context import *


class WhiteNoiseAudio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        
        # Register list of white noise titles that are held in a padatious entity
        self.register_entity_file("title.entity")
        self.process = None
        
        # Build white noise list
        self.play_list = {
            'blender one': join(abspath(dirname(__file__)), 'stories', 'blender-1.mp3'),
            'blender two': join(abspath(dirname(__file__)), 'stories', 'blender-2.mp3'),
            'dryer one': join(abspath(dirname(__file__)), 'stories', 'dryer-1.mp3'),
            'dryer two': join(abspath(dirname(__file__)), 'stories', 'dryer-2.mp3'),
            'fan one': join(abspath(dirname(__file__)), 'stories', 'fan-1.mp3'),
            'fan two': join(abspath(dirname(__file__)), 'stories', 'fan-2.mp3'),
            'heater one': join(abspath(dirname(__file__)), 'stories', 'heater-1.mp3'),
            'heater 2': join(abspath(dirname(__file__)), 'stories', 'heater-2.mp3'),
            'motor': join(abspath(dirname(__file__)), 'stories', 'motor.mp3'),
            'ocean one': join(abspath(dirname(__file__)), 'stories', 'ocean-1.mp3'),
            'ocean two': join(abspath(dirname(__file__)), 'stories', 'ocean-2.mp3'),
            'ocean three': join(abspath(dirname(__file__)), 'stories', 'ocean-3.mp3'),
            'ocean four': join(abspath(dirname(__file__)), 'stories', 'ocean-4.mp3'),
            'pink noise': join(abspath(dirname(__file__)), 'stories', 'pink-noise.mp3'),
            'rain one': join(abspath(dirname(__file__)), 'stories', 'rain-1.mp3'),
            'rain two': join(abspath(dirname(__file__)), 'stories', 'rain-2.mp3'),
            'rain three': join(abspath(dirname(__file__)), 'stories', 'rain-3.mp3'),
            'rain four': join(abspath(dirname(__file__)), 'stories', 'rain-4.mp3'),
            'refrigerator': join(abspath(dirname(__file__)), 'stories', 'refrigerator.mp3'),
            'shower': join(abspath(dirname(__file__)), 'stories', 'shower.mp3'),
            'storm': join(abspath(dirname(__file__)), 'stories', 'storm.mp3'),
            'stream one': join(abspath(dirname(__file__)), 'stories', 'stream-1.mp3'),
            'stream two': join(abspath(dirname(__file__)), 'stories', 'stream-2.mp3'),
            'train one': join(abspath(dirname(__file__)), 'stories', 'train-1.mp3'),
            'train two': join(abspath(dirname(__file__)), 'stories', 'train-2.mp3'),
            'underwater one': join(abspath(dirname(__file__)), 'stories', 'underwater-1.mp3'),
            'underwater two': join(abspath(dirname(__file__)), 'stories', 'underwater-2.mp3'),
            'vacuum': join(abspath(dirname(__file__)), 'stories', 'vaccuum.mp3'),
            'water': join(abspath(dirname(__file__)), 'stories', 'water.mp3'),
            'water boiling one': join(abspath(dirname(__file__)), 'stories', 'water-boiling-1.mp3'),
            'water boiling two': join(abspath(dirname(__file__)), 'stories', 'water-boiling-2.mp3'),
            'water fall': join(abspath(dirname(__file__)), 'stories', 'waterfall.mp3'),
            'waves one': join(abspath(dirname(__file__)), 'stories', 'waves-1.mp3'),
            'waves two': join(abspath(dirname(__file__)), 'stories', 'waves-2.mp3'),
            'white noise one': join(abspath(dirname(__file__)), 'stories', 'white-noise-1.mp3'),
            'white noise two': join(abspath(dirname(__file__)), 'stories', 'white-noise-2.mp3'),
            'white noise three': join(abspath(dirname(__file__)), 'stories', 'white-noise-3.mp3'),
            'white noise four': join(abspath(dirname(__file__)), 'stories', 'white-noise-4.mp3'),
            'white noise five': join(abspath(dirname(__file__)), 'stories', 'white-noise-5.mp3'),
            'white noise six': join(abspath(dirname(__file__)), 'stories', 'white-noise-6.mp3'),

        }

    #Play random white noise from list
    @intent_file_handler('white-noise.relax.intent')
    def white_noise_relax(self, message):
        wait_while_speaking()
        self.speak_dialog('white-noise.relax')
        white_noise_file = list(self.play_list.values())
        white_noise_file = random.choice(white_noise_file)
        print(white_noise_file)
        # if os.path.isfile(white_noise_file):
        wait_while_speaking()
        self.process = play_mp3(white_noise_file)

    #Pick white noise by title
    @intent_file_handler('pick.white-noise.intent')
    def handle_pick_white_noise(self, message):
        self.speak_dialog('pick.white-noise')
        wait_while_speaking()
        title = message.data.get('title')
        score = match_one(title, self.play_list)
        print(score)
        if score[1] > 0.5:
            self.process = play_mp3(score[0])
        else:
            return None
            self.speak('Sorry I could not find that white noise in my library')

    #List stories in library
    @intent_file_handler('list.white-noise.intent')
    def handle_list_stories(self, message):
        wait_while_speaking()
        white_noise_list = list(self.play_list.keys())
        print(white_noise_list)
        self.speak_dialog('list.white-noise', data=dict(stories=white_noise_list))
    
    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

def create_skill():
    return WhiteNoiseAudio()
