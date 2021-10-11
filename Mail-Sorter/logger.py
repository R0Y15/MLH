import pprint
import datetime
import os

# Log levels: if True, print
LOGINFO = True
LOGDEBUG = False
LOGERROR = True

# Level definitions
INFO = 0
DEBUG = 1
ERROR = 2
MOVE = 3

def singlet(cls):
    instan = {}

    def __init__(auto, logfile):
        return

    def getinstance(auto, logfile):
        if cls not in instan:
            instan[cls] = cls(auto, logfile)
        return instan[cls]
    return getinstance

@singlet
class Logger:
    p = pprint.PrettyPrinter(indent=4, width=80)
    pp = p.pprint

    def __init__(self, auto, logfile):
        self.auto = auto
        self.logfile = os.path.expanduser(logfile)

        try:
            self.file = open(logfile, 'a+')
        except FileNotFoundError:
            directory = os.path.split(logfile)[0]
            if not os.path.exists(directory):
                os.makedirs(directory)
            self.file = open(logfile, 'a+')

        self.log(DEBUG, "Initialized Logger")

    def writ_log(self, statement):
        dt = datetime.datetime.today()
        if self.auto is True:
            self.file.write("[{}] {}\n".format(dt, statement))
        else:
            self.pp("[{}] {}".format(dt, statement))

    def log(self, level, logtext):
        if LOGINFO and level == INFO:
            # self.pp("INFO: {}".format(logtext))
            self.writ_log("INFO: {}".format(logtext))
            return
        if LOGDEBUG and level == DEBUG:
            # self.pp("DEBUG: {}".format(logtext))
            self.writ_log("DEBUG: {}".format(logtext))
            return
        if LOGERROR and level == ERROR:
            # self.pp("ERROR: {}".format(logtext))
            self.writ_log("ERROR: {}".format(logtext))
            return
        if level == MOVE:
            # self.pp("MOVE: {}".format(logtext))
            self.writ_log("MOVE: {}".format(logtext))
            return
        #self.pp("OTHER: {}".format(logtext))
        #self.write_log("OTHER: {}".format(logtext))
    
    def quit(self):
        self.writ_log("Closing program on user exit")
        if self.auto is True:
            self.file.close()