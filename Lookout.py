import imaplib
import email

class Lookout :
    def refresh_inbox(self) :
        self.get_inbox(self.inbox)

    def get_text(self, msg):
        if msg.is_multipart():
            return self.get_text(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)
        
    def get_inbox(self, inboxStr:str) :
        self.mail.select(inboxStr)
        self.typ, self.data = self.mail.search(None, 'ALL')

    def get_all_subjects(self, refresh=True) :
        if refresh :
            self.refresh_inbox()
        subjects = []
        for num in self.data[0].split():
            self.typ, data = self.mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            subject = email_message['Subject']
            subjects.append(subject)
        return subjects

    def get_all_content(self, refresh=True) :
        if refresh :
            self.refresh_inbox()
        contents = []
        for num in self.data[0].split():
            self.typ, data = self.mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            content = self.get_text(email_message)
            contents.append(content)
        return contents
    
    def get_all_content_by_subject(self, subject:str, refresh=True) :
        if refresh :
            self.refresh_inbox()
        contents = []
        for num in self.data[0].split():
            self.typ, data = self.mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            if (email_message['Subject'] == subject) :
                content = self.get_text(email_message)
                contents.append(content)
        return contents
    
    def get_all_content_by_sender_partial(self, sender:str, refresh=True) :
        if refresh :
            self.refresh_inbox()
        contents = []
        for num in self.data[0].split():
            self.typ, data = self.mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)
            if (not email_message['From'].find(sender.lower()) == -1) :
                content = self.get_text(email_message)
                contents.append(content)
        return contents


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
        self.mail.login(username, password)
        self.inbox = 'inbox'
        self.get_inbox(self.inbox)

    def close(self) :
        self.mail.close()
        self.mail.logout()
