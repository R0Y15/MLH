import imaplib
import datetime

# Local imports
from logger import *
from parser import Parser
from message import Message

class Server():

    # Record all dates in UTC as they don't observer DST
    runtime = datetime.datetime.utcnow()
    runtime = runtime

    mail = ''

    def __init__(self, server, user, password):
        self.logger = Logger(False, False)
        self.logg(DEBUG, "Server Init!!")
        self.connect(server)
        self.authenticate(user, password)

    def logg(self, level, statement):
        self.logger.log(level, "server -- {}".format(statement))


    def connect(self, server):
        self.logg(INFO, "func --> connect")
        self.logg(DEBUG, "Server: {}".format(server))
        # self.mail = imaplib.IMAP4_SSL(config.config['AUTHENTICATION']['server'])
        self.mail = imaplib.IMAP4_SSL(server)


    def authenticate(self, user, password):
        self.logg(INFO, "func --> authenticate")
        self.logg(DEBUG, "Login information: user:{} password:{}".format(user, password))
        self.mail.login(user, password)


    def get_all_labels(self):
        self.logg(INFO, "func --> get_all_labels")
        labels_tuple = self.mail.list()
        labels_list = []
        for item in labels_tuple[1]:
            # pp(item)
            item = item.decode("utf-8").split("\"")[3]
            if item != '[Gmail]':
                labels_list.append(item)
        # pp(labels_list)
        self.logg(DEBUG, labels_list)
        return labels_list


    def retrieve_message(self, email_uid):
        self.logg(INFO, "func --> retrieve_message")
        
        #Fetch the mail headers from GMAIL
        result, data_one = self.mail.uid("FETCH", email_uid, '(BODY[HEADER.FIELDS (MESSAGE-ID FROM TO CC DATE SUBJECT)])')
        if result == 'OK':
            self.logg(DEBUG, "GOT MESSAGE HEADERS[{}]".format(email_uid))
        else:
            self.logg(DEBUG, "FAILED TO GET MESSAGE HEADERS[{}]".format(email_uid))
            exit(1)

        #Fetch the body of the message(including the attachement)
        result, data_two = self.mail.uid("FETCH", email_uid, '(BODY[TEXT])')
        if result == 'OK':
            self.logg(DEBUG, "GOT MESSAGE BODY[{}]".format(email_uid))
        else:
            self.logg(DEBUG, "GOT MESSAGE BODY[{}]".format(email_uid))
            exit(1)
        self.logg(DEBUG, data_two)
        
        if data_one[0] is not None:
            raw_email = data_one[0][1].decode("utf-8")
        else:
            raw_email = "None"
        if data_two[0] is not None:
            raw_body = data_two[0][1].decode("ISO-8859-1")
        else:
            raw_body = "None"
        
        parser = Parser()
        parsed_message = parser.parse_email(raw_email, raw_body)

        return Message(parsed_message, email_uid, self)


    def get_mailbox_contents(self, label):
        self.logg(INFO, "func --> get_mailbox_contents")
        
        result, data = self.mail.uid('search', None, "ALL")  # search and return UIDs
        if result == 'OK':
            self.logg(INFO, "YOU'VE GOT MAIL!!!")
        else:
            self.log(INFO, "NO MAIL FOR YOU!!!")
            exit(1)
        return data[0].split()


    def get_old_uids(self, label):
        self.logg(INFO, "func --> get_old_uids")
        self.logg(INFO, "")


    def archive_all(self, uid_array):  # uid_array is defined as follows [[uid, email_message], [uid, email_message], etc...]
        self.logg(INFO, "func --> archive_all")
        for item in uid_array:
            archive_message(item[0], item[1])

    def clo(self):
        self.mail.close()

    def logout(self):
        self.mail.logout()

    def sele_box(self, box):
        self.mail.select(box)
