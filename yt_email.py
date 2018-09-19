import imaplib
import email
import re
import HTMLParser

EMAIL = # Your e-mail here
PWD = # Your password here
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

links = []

def get_video_links():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(EMAIL,PWD)
        mail.select('inbox') 

        state, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        for id in id_list:
            state, data = mail.fetch(id, '(RFC822)')

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    msgstr = str(msg)
                    subject = msg['Subject']
                    if "uploaded" in subject:
                        vid_id = re.search('vi/(.*)/', msgstr)
                        if vid_id:
                            links.append('https://www.youtube.com/watch?v=' + vid_id.group(1))
                    else:
                        continue
        return links
    except Exception, e:
        print str(e)
