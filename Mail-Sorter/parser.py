import email
from email.parser import Parser as MailParser

# Local imports
from logger import *

class Parser():

    def __init__(self):
        self.logger = Logger(False, False)

    def log(self, level, statement):
        self.logger.log(level, "parser -- {}".format(statement))


    def get_first_text_block(self, email_message):
        self.log(INFO, "func --> get_first_text_block")
        maintype = email_message.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
                elif maintype == 'text':
                    return email_message.get_payload()


    def parse_email(self, raw_email, raw_body):
        self.log(INFO, "func --> parse_email")
        email_contents = {"header": {"from": "", "to": "", "cc": "", "date": "", "subject": ""}, "message": ""}
        email_contents["message"] = email.message_from_string(raw_email)
        email_contents["header"]["from"] = email_contents["message"]["From"]
        email_contents["header"]["to"] = email_contents["message"]["to"]
        email_contents["header"]["cc"] = email_contents["message"]["cc"]
        email_contents["header"]["date"] = email_contents["message"]["date"]
        email_contents["header"]["subject"] = email_contents["message"]["subject"]
        # pp("=======================================")
        self.log(INFO, "=======================================")

        emailText = raw_body
        mailparser = MailParser()
        emailThing = mailparser.parsestr(emailText)

        if emailThing.is_multipart():
            # pp("EMAIL MESSAGE IS MULTIPART: {}".format(emailThing.is_multipart()))
            self.log(DEBUG, "EMAIL MESSAGE IS MULTIPART: {}".format(emailThing.is_multipart()))
            for part in emailThing.get_payload():
                part = part.get_payload()
        else:
            # pp("EMAIL MESSAGE IS MULTIPART: {}".format(emailThing.is_multipart()))
            self.log(DEBUG, "EMAIL MESSAGE IS MULTIPART: {}".format(emailThing.is_multipart()))
        email_contents["message"] = emailThing.get_payload()
        # pp(email.message_from_string(raw_email).get_payload(decode=True))
        return email_contents
