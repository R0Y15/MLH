import socket
import argparse
import signal
import sys
import datetime

# Local imports
from logger import *
from config import Config
from server import Server
from sorter import Sorter

class Main():

    def __init__(self):

        signal.signal(signal.SIGINT, self.quit)


        parser = argparse.ArgumentParser(description='Parse flags such as -a --auto for autosort, -v --verbose for verbose logging, -s --sort for specific folder sort, -l --log to specify a log file')

        parser.add_argument('-a', '--auto',     type=int,  default=0,                                            help='1 = True, 0 = False. Automatically sort all emails without human intervention?')
        parser.add_argument('-v', '--verbose',  type=bool, default=False,                                            help='True|False Automatically sort all emails without human intervention?')
        parser.add_argument('-s', '--sort',     type=str,  default="all",                                            help='True|False Automatically sort all emails without human intervention?')
        parser.add_argument('-l', '--log',      type=str,  default="/home/valon/.config/MailSorter/MailSorter.log",  help='True|False Automatically sort all emails without human intervention?')
        args = parser.parse_args()
        
        args.auto = True if args.auto == 1 else False

        self.logger = Logger(args.auto, args.log)

        self.log(INFO, "Program starting. settiongs are {}".format(args))
        self.log(DEBUG, "func --> main")


        # --------------Pre-Connect Checks------------------------------------
        self.is_connected()
        self.config = Config()
        # --------------Connect and Authentication-----------------------
        self.server = Server(self.config.config['AUTHENTICATION']['server'], self.config.config['AUTHENTICATION']['user'], self.config.config['AUTHENTICATION']['pass'])
        # --------------Perform Mail Operations------------------------------
        self.labels = self.server.get_all_labels()
        self.sorter = Sorter(self.config, automove=args.auto)
        self.sorter.sort_mail(self.server)  # '"Social"'
        # --------------Close Connection----------------------------------------
        self.server.close()
        self.server.logout()
        self.log(INFO, "Program has concluded. Exiting.")


    def log(self, level, statement):
        self.logger.log(level, "main -- {}".format(statement))


    def is_connected(self):
        # Detect network connection
        REMOTE_SERVER = "www.google.com"
        self.log(DEBUG, "func --> is_connected")
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname(REMOTE_SERVER)
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            self.log(DEBUG, "INTERNET CONNECTION DETECTED")
            s.close()
            return True
        except:
            pass
        self.log(ERROR, "INTERNET CONNECTION NOT DETECTED")
        exit(1)
        return False

    def quit(self, posOne, posTwo):
        self.logger.quit()
        sys.exit(0)

if __name__ == "__main__":
    main = Main()
