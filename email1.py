
import email
import json
import re
from email.iterators import typed_subpart_iterator

def get_charset(message, default="ascii"):
    """Get the message charset"""

    if message.get_content_charset():
        return message.get_content_charset()

    if message.get_charset():
        return message.get_charset()

    return default

def find_body(message):
    """Get the body of the email message"""

    if message.is_multipart():
        #get the plain text version only
        text_parts = [part for part in typed_subpart_iterator(message,'text','plain')]
        body = []
        for part in text_parts:
            charset = get_charset(part, get_charset(message))
            body.append(str(part.get_payload(decode=True),charset,"replace"))
            
#     else: # if it is not multipart, the payload will be a string
#           # representing the message body
#         body = unicode(message.get_payload(decode=True),get_charset(message),"replace")
#         return body.splitlines()

        body=u''.join(body).splitlines()
        
        bodyy=[]
        for i in body:
            if i is not '':
                bodyy.append(i)
        return bodyy


def find_recev(message):
    try:
        return message['Delivered-To']
    except:
        return 'error'

def find_from(message):
    try:
#       return message['From']
        return(re.findall('\S+@\S+', message['From'])) 
    except:
        return 'error'

def find_cc(message):
    try:
#         return message['Cc']
        return(re.findall('\S+@\S+', message['Cc']))
    except:
        return 'error'


def find_bcc(message):
    try:
#         return message['Cc']
        return(re.findall('\S+@\S+', message['Cc']))
    except:
        return 'error'

def find_day_date_time_zone(message):
    try:
        return message['Date']
    except:
        return 'error'
def find_subject(message):
    try:
        return message['Subject']
    except:
        return 'error'

def find_emails(message):
    try:
        listToStr = ' '.join(map(str, body)) 
        return(re.findall('\S+@\S+', listToStr))      
    except:
        return 'error'

def retjson(a):
    try:
        return(json.dumps(a, indent=4))
    except:
        return 'error'

if __name__ == "__main__":
    file1 = open("1.txt","r+")
    message = str(file1.read())
    #print(type(message))

    #contents = json.loads(message)
    #print(contents)

    
    parsed_json = (json.loads(message))
             # parsed_json.keys()
             # # dict_keys(['sender', 'receiver', 'receivedDate', 'subject', 'attachments', 'body', 'raw'])
           
    raw_email=parsed_json['raw']
    email_message=email.message_from_string(raw_email)
             
    fromm=find_from(email_message)
    to=find_recev(email_message)
    cc=find_cc(email_message)
    date=find_day_date_time_zone(email_message)
    sub=find_subject(email_message)
    body=find_body(email_message)
    mail=find_emails(body)
    dictt={'From':fromm,'To':to,'Cc':cc,'Date':date,'Subject':sub,'Body':body,'Attachment':parsed_json['attachments'],'List_of_Emails':mail}
    ans=retjson(dictt)
    print(ans)
    
