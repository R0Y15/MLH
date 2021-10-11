import imaplib
import pprint
import email
import time
import configparser as cp
import logging
import subprocess
import socket
import re
from email.parser import Parser
from os.path import isfile
from datetime import datetime
from dateutil import tz

# Local imports
from logger import *
from server import Server
from message import Message

class Sorter():

    AUTOMOVE = True

    def __init__(self, config, automove=True):
        self.logger = Logger(False, False)
        self.AUTOMOVE = automove
        self.config = config


    def log(self, level, statement):
        self.logger.log(level, "sorter -- {}".format(statement))


    def sort(self, box, message, regexes):
        self.log(DEBUG, "func --> sort")
        self.log(DEBUG, "The regex for the box {}, is SUBJECT:{} & CONTENT: {}....".format(box, self.config.config[box]['subject_regex'], self.config.config[box]['content_regex']))
        self.log(INFO, "EMAIL -- FROM: {}, SUBJECT: {}".format(message.from_address, message.subject))
        if self.sort_sender(box, message, regexes[0]) is False:
            if self.sort_subject(box, message, regexes[1]) is False:
                if self.sort_content(box, message, regexes[2]) is False and message.body is not None:
                    self.log(INFO, "Email Failed to match filter {} for sender, subject, or content...".format(box))


    def sort_subject(self, box, message, regex):
        self.log(DEBUG, "func --> sort_subject({})".format(regex))
        self.log(DEBUG, "Email Subject: {}".format(message.subject))
        match = None
        try:
            match = regex.search(message.subject)
        except TypeError:
            self.log(ERROR, "TypeError: Subject is [{}]".format(message.subject))
        self.log(INFO, "Subject Match: {}".format(match))
        match = False if match is None else True

        if match:
            self.log(INFO, "SUBJECT MATCH FOUND!!!")
            if self.choose_move(message, box):
                message.move_message(box)
            return True
        return False

    def choose_move(self, message, destination):
        options = {'Y': True, 'N': False, 'n': False}
        if self.AUTOMOVE is False:
            choice = input("Would you like to move this email [UID[{}] to {}? ".format(message.uid, destination))
        else:
            choice = 'Y'
        try:
            if options[choice]:
                self.log(INFO, "MOVING  MESSAGE UID[{}]".format(message.uid))
                return True
            else:
                return False
        except KeyError:
            self.log(INFO, 'Item {} not found'.format(choice))
            return False


    def sort_sender(self, box, message, regex):
        self.log(DEBUG, "func --> sort_subject({})".format(regex))

        match = None

        try:
            self.log(INFO, "Email Sender: {}".format(message.from_address))
            self.log(DEBUG,"TESTING SENDER INPUT - TypeError: expected string or bytes-like object: {}".format(message.from_address))
            match = regex.search(message.from_address) 
            self.log(INFO, "Sender Match: {}".format(match))
        except TypeError:
            self.log(ERROR, "TypeError: sender is [{}]".format(message.from_address))

        match = False if match is None else True

        if match:
            self.log(DEBUG, "SENDER MATCH FOUND!!!")
            message.move_message(box)
            return True
        return False


    def sort_content(self, box, message, regex):
        self.log(DEBUG, "func --> sort_content({})".format(regex))

        match = regex.search(message.body)
        self.log(INFO, "Content Match: {}".format(match))
        match = False if match is None else True

        if match:
            message.move_message(box)
            return True
        return False


    def sort_mail(self, server):
        self.log(DEBUG, "func --> sort_mail")
        inbox = '"inbox"'
        server.select_box(inbox)
        message_uids = server.get_mailbox_contents(inbox)
        sections = self.config.get_sections()
        if self.AUTOMOVE is True:
            self.log(INFO, "Automove is set to true, sorting for all lables.")
            choice = 'all'
        else:
            choice = input("Options: all or one of the following [{}]? ".format(sections))
            self.log(DEBUG, choice)
            self.log(DEBUG, sections)

        if "\"{}\"".format(choice) in sections:
                choice = "\"{}\"".format(choice)
                self.log(INFO, "SORTING MAIL FOR LABEL: {}".format(choice))
                for i in range(10):
                    print('.', end="")
                    time.sleep(1)
                print('')
                regexes = config.get_regexes(choice)
                for email_uid in message_uids:
                    email_contents = server.retrieve_message(email_uid)
                    sort(choice, email_uid, email_contents, regexes)
        elif choice == "all":
            self.log(INFO, "SORTING MAIL FOR ALL FILTERS!!!")
            for label in sections:
                self.log(INFO, "SORTING MAIL FOR LABEL: {}".format(label).center(120, "="))
                for i in range(10):
                    print('.', end="")
                    time.sleep(1)
                print('')
                regexes = self.config.get_regexes(label)
                for email_uid in message_uids:
                    self.log(INFO, "========================================")
                    message = server.retrieve_message(email_uid)
                    self.sort(label, message, regexes)
                    # #pp(email_contents)
                # email_contents = retrieve_message(message_uids[-1])
                # #pp(email_contents)
                # #pp("========================================")
        else:
            self.log(ERROR, "selection {} is not one of the provided options!!!".format(choice))