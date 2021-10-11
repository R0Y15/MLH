# Local imports
from logger import *


class Message:
    to_address = ""
    from_address = ""
    subject = ""
    message = ""
    uid = 00
    labels = [None, None]

    def __init__(self, parsed_message, uid, server):
        self.logger = Logger(False, False)
        self.log(DEBUG, "Message Init")
        self.to_address = parsed_message['header']['to'] if 'to' in parsed_message['header'] else 'None'
        self.from_address = parsed_message['header']['from'] if 'from' in parsed_message['header'] else 'None'
        self.subject = parsed_message['header']['subject'] if 'subject' in parsed_message['header'] else 'None'
        self.sent_date = parsed_message['header']['date'] if 'date' in parsed_message['header'] else 'None'
        self.cc = parsed_message['header']['cc'] if 'cc' in parsed_message['header'] else 'None'
        self.body = parsed_message['message'] if 'message' in parsed_message else 'None'
        self.uid = uid
        self.labels = self.get_message_labels()
        self.server = server

    def logg(self, level, statement):
        self.logger.log(level, "message -- {}".format(statement))

    
    def get_message_labels(self):
        self.logg(INFO, "func --> get_message_labels")
        self.logg(INFO, '')  # Get from the bash script and the python script it calls.


    def remove_all_labels(self):
        self.logg(INFO, "func --> remove_all_labels")
        labels = self.get_message_labels()
        for label in labels:
            self.remove_label(label)


    def remove_label(self, label):
        self.logg(INFO, "func --> remove_label")
        self.logg(DEBUG, "LABEL: {}".format(label))
        if label == '"inbox"' or label == "inbox":
            # pp("+=============================================SKIPPING")
            self.log(DEBUG, "+=============================================SKIPPING")
            return
        options = {'Y': True, 'N': False, 'n': False}
        # pp(email_message)
        choice = input("Would you like to remove the label {} from this email [UID:{}]?".format(label, self.uid))
        try:
            if options[choice]:
                self.logg(INFO, 'LISTING LABELS FOR UID: {}'.format(self.uid))
                response = self.server.mail.uid('FETCH', self.uid, '(X-GM-LABELS)')
                self.logg(INFO, response)
                self.logg(INFO, 'REMOVE LABEL')
                response = self.server.mail.uid('STORE', self.uid, '-X-GM-LABELS', label)
                self.logg(INFO, response)
                self.logg(INFO, 'LISTING LABELS FOR UID: {}'.format(self.uid))
                response = self.server.mail.uid('FETCH', self.uid, '(X-GM-LABELS)')
                self.logg(INFO, response)
        except KeyError:
            self.logg(DEBUG, 'Item %s not found' % choice)


    def add_label(self, label):
        self.logg(INFO, "func --> add_label")
        options = {'Y': True, 'N': False, 'n': False}
        choice = input("Would you like to add the label {} to this email [UID:{}]: From: {} Subject:{}?".format(label, self.uid, self.from_address, self.subject))
        try:
            if options[choice]:
                self.logg(INFO, 'LISTING LABELS FOR UID: {}'.format(self.uid))
                response = self.server.mail.uid('FETCH', self.uid, '(X-GM-LABELS)')
                self.logg(INFO, response)
                self.logg(INFO, 'ADD LABEL')
                response = self.server.mail.uid('STORE', self.uid, '+X-GM-LABELS', label)
                self.logg(INFO, response)
                self.logg(INFO, 'LISTING LABELS FOR UID: {}'.format(self.uid))
                response = self.server.mail.uid('FETCH', self.uid, '(X-GM-LABELS)')
                self.logg(INFO, response)
        except KeyError:
            self.logg(INFO, 'Item %s not found' % choice)


    def copy_message(self, destination):   ############################################# Move the automove to sorter side. 
        self.logg(INFO, "func --> move_message")

        response = self.server.mail.uid('COPY', self.uid, destination)
        self.logg(INFO, response)
        if response[0] == 'OK':
            self.logg(INFO, self.server.mail.uid('STORE', self.uid, '+FLAGS', '(\\Deleted)'))
            self.logg(INFO, 'ORIGINAL DELETED')
            self.logg(INFO, self.server.mail.expunge())
            self.logg(INFO, "MAIL MOVED")
        else:
            self.logg(INFO, 'ERROR: FAILED TO MOVE MAIL')


    def move_message(self, destination):
        self.copy_message(destination)
        self.remove_label('"inbox"')



    def trash_message(self):
        self.logg(INFO, "func --> trash_message")
        self.remove_all_labels()
        self.move_message('Trash')
        self.delete_message()


    def delete_message(self):
        self.logg(INFO, "func --> delete_message")
        options = {'Y': True, 'N': False, 'n': False}
        choice = input("Would you like to delete this email [UID[{}]: From: {} Subject:{}] to {}? ".format(self.uid, self.from_address, self.subject))

        try:
            self.logg(INFO, options[choice])
            if options[choice]:
                self.logg(INFO, 'DELETE')
                self.logg(INFO, "DELETING  MESSAGE UID[{}]: From: {} Subject:{}".format(self.uid, self.from_address, self.subject))
                self.logg(INFO, self.server.mail.uid('STORE', self.uid, '+FLAGS', '(\\Deleted)'))
                self.logg(INFO, self.server.mail.expunge())
            else:
                self.logg(INFO, 'KEEP')
        except KeyError:
            self.logg(INFO, 'Item %s not found' % choice)


    def archive_message(self, uid, email_message):
        self.logg(INFO, "func --> archive_message")
        self.move_message('"[Gmail]/All Mail"')


    # NOTE: Use the 'XM-'
    def starred(self):
        self.logg(INFO, "func --> starred")
        starLabel = '"[Gmail]/Starred"'
        self.sort_mail(starLabel)
