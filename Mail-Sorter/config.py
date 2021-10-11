import configparser as cp
import re
from os.path import isfile

# Local imports
from logger import *


class Config():

    def __init__(self):
        self.config_file = 'sorter.conf'
        self.config = cp.ConfigParser()

        self.logger = Logger(False, False)
        self.sections = self.get_config()


    def logg(self, level, statement):
        self.logger.logg(level, "config -- {}".format(statement))

   
    def get_regexe(self, box):
        self.log(INFO, "func --> get_regexe")
        from_pattern = '{}'.format(self.config[box]['from_regex'])
        from_regex = re.compile(from_pattern)

        subject_pattern = '{}'.format(self.config[box]['subject_regex'])
        subject_regex = re.compile(subject_pattern)

        content_pattern = '{}'.format(self.config[box]['content_regex'])
        content_regex = re.compile(content_pattern)

        return [from_regex, subject_regex, content_regex]


   
    def get_sections(self):
        sections = self.config.sections()
        sections.remove("AUTHENTICATION")
        return sections


  
    def get_config(self):
        self.log(INFO, "func --> get_config")
        if isfile(self.config_file):
            self.config.read(self.config_file)
            self.config.sections()
        else:
            self.save_config(True)


  
    def save_config(self, default=False):
        self.log(INFO, "func --> save_config")
        if default:
            self.config['AUTHENTICATION'] = {
                'server': 'thing.google.com',
                'user': 'bonkers',
                'pass': 'piquel'
            }
            self.config['FOLDEREX'] = {
                'subject_regex': '(buy|suck)\ it',
                'content_regex': 'change\.org'
            }
        with open(config_file, 'w') as config_link:
            self.config.write(config_link)
