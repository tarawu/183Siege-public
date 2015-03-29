from getch import getch
from constants import *
import time, random
import select
import sys
import multiprocessing
from multiprocessing import Pipe
import threading
import time
random.seed()

################################################################################
# Toggle Student AI / Story Mode                                               #
################################################################################
USE_AI = False                                                                 #
STORY_MODE = True                                                              #
################################################################################

def combat_action(options):
    return 'x'

def movement_action(options):
    return 'x'

def item_action(options):   
    return '3'
            

#####################################################################################
# Game Driver for your AI. Don't modify this section.                               #
#####################################################################################
def _check_loop():                                                                  #
    raw_input()                                                                     #
    USE_AI = False                                                                  #
                                                                                    #
class User(object):                                                                 #
    def __init__(self):                                                             #
        self.input_check = None                                                     #
        self.set_ai(USE_AI)                                                         #
                                                                                    #
    def select(self, options):                                                      #
        if options['situation'] == 'COMBAT': return combat_action(options)          #
        elif options['situation'] == 'ITEM': return item_action(options)            #
        elif options['situation'] == 'MOVE': return movement_action(options)        #
        else: raise Exception("Bad move option: {0}".format(options['situation']))  #
                                                                                    #
    def set_ai(self, setting):                                                      #
        global USE_AI                                                               #
        if setting:                                                                 #
            # launch subprocess to handle input                                     #
            USE_AI = True                                                           #
            self.input_check = threading.Thread(target=_check_loop)                 #
            self.input_check.daemon = True                                          #
            self.input_check.start()                                                #
        else:                                                                       #
            # end the subprocess                                                    #
            if self.input_check and self.input_check.is_alive():                    #
                self.input_check.join(GAME_SPEED)                                   #
            USE_AI = False                                                          #
                                                                                    #
                                                                                    #
    def __move__(self, options):                                                    # 
        if not USE_AI:                                                              #
            usr = getch()                                                           #
            if ord(usr) == 13:                                                      #
                self.set_ai(True)                                                   #
                return self.select(options).lower()                                 #
            return usr.lower()                                                      #
                                                                                    #
        time.sleep(GAME_SPEED)                                                      #
        if self.input_check and not self.input_check.is_alive():                    #
            self.set_ai(False)                                                      #
            return getch().lower()                                                  #
        return self.select(options).lower()                                         #
                                                                                    #
                                                                                    #
#####################################################################################
