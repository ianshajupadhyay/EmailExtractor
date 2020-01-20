from textblob import TextBlob
import nltk
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
#         return message['Delivered-To']
        return(re.findall('\S+@\S+', message['Delivered-To'])) 
    except:
        return 'error'
    

    
def find_from(message):
    try:
#       return message['From']
        from_email=re.findall('\S+@\S+', message['From'])
        listToStr = ' '.join(map(str, from_email))
        listToStr.strip('<')
        listToStr.strip('>')
        print(listToStr)
        return(re.findall('\S+@\S+', listToStr))
    except:
        return 'error'
    
    
    
def find_cc(message):
    try:
#         return message['Cc']
        return(re.findall('\S+@\S+', message['Cc']))
        # return(find_emails(cc))
    except:
        return 'error'  


def find_day_date_time_zone(message):
    try:
        date=message['Date']
        return(date[0:16]) 
    except:
        return 'error'
    
    
def find_subject(message):
    try:
        return message['Subject']
    except:
        return 'error'
    
    
def find_boundart(message):
    try:
        email_message.set_boundary("Blue_Boundary")
        return(email_message.get_boundary())
    except:
        return 'error'
    
    
def find_emails(message):
    try:
        listToStr = ' '.join(map(str, body)) 
        return(re.findall('\S+@\S+', listToStr))      
    except:
        return 'error'



def find_Phone(string):
    try:
        phone = ''
        phoneRegEx = re.compile('\"tel\:[\(\)\-0-9\ ]{1,}\"')
#          phoneRegEx=   re.compile('r'^(\d{3})-(\d{3})-(\d{4}))
        listToStr = ' '.join(map(str, body)) 
        m = phoneRegEx.search(listToStr)
        if m:
            phone = m.group(0)[5:-1]
        if not phone:
            return 'No_Contact_FOUND'
        return phone
    except:
        return 'error'
    
    
    
def find_Url(string):
    try:
        listToStr = ' '.join(map(str, body)) 
        url = re.search("(?P<url>https?://[^\s]+)", listToStr).group("url")
        if url == 'https://www':
            return 'No_URL_FOUND'
        return url
    except:
        return 'error'
    
    

def find_domain(signature):
    domain=url.split('//')[-1].split('/')[0]
    return (domain)


def find_Signature(s):
    
    ans=''
    s_body = ' '.join(map(str, body))
    result = s_body.find('-- ') 
    
    if(result!= -1 ):
        status = 1  # signature is present with the delimeter
    else :
        status = 0 # signature is  not present with the delimeter
    
    if(result):
        for i in s_body[result:-1]:
            if(i != '\n'):
                ans=ans+i    
            else:
                ans=ans+'--------'

    
    Dict={}
    sg='-- '

    deli=s.index(sg)
    
    name=s[deli+1]
    
    design = s[deli+2]
    phn = s[deli+3]
    from pandas import read_excel
    file_name = "desig.xlsx"
    df = read_excel(file_name)
    flag=  1
    x = design
    desig = "None"
    for i in df['OCC_TITLE']:
        if(i.find(x)):
            print(x)
            desig = x
            break
        else:
            continue

	#print(dict['designation'])
    email = find_emails(ans)
    domain=find_domain(ans)
    signDict = {}

    signDict= {"name":name, "designation":design,"phone":phn,"email":email,"domain":domain , "designation" : desig}
    print(signDict)
    return signDict
   
    

    
    
def find_sign_url(s):
    ans=''
    s_body = ' '.join(map(str, body))
    result = s_body.find('--') 
    
    if(result):
        for i in s_body[result:-1]:
            if(i != '\n'):
                ans=ans+i    
            else:
                ans=ans+'--------'
    return find_Url(ans)  





def find_name(message):
    try:
#       return message['From']
        message = message['from']
        name=""
        for i in message:
            if i != '<':
                name=name+i
            else:
                break
        return(name) 
    except:
        return 'error'
    
    


def find_tone(body):
    mess = ""
    for i in body:
        if i != '-- ':
            mess = mess + i
        else:
            break;
            
    obj = TextBlob(mess)
    sentiment = obj.sentiment.polarity
    if sentiment == 0:
        tone = "Neutral"
    elif sentiment > 0:
        tone = "Positive"
    elif sentiment < 0:
        tone = "Negative"
    return tone    


def retjson(a):
	try :
		return (json.dumps(a , indent = 4))
	except:
		return "error"


if __name__ == "__main__":
    file1 = open("1.txt","r+")
    message = file1.read()
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
    #urls_in_body = findall_urlsinbody(body)
    mail=find_emails(body)
    phone=find_Phone(body)
    url=find_Url(body)
    url_signature=find_sign_url(body)
    seeg=find_Signature(body)
    name = find_name(email_message)
    tone=find_tone(body)
#     print(type(body))
    dictt={'From':fromm,'To':to,'Cc':cc,'Date':date,'Subject':sub,'Body':body,'Attachment':parsed_json['attachments'],'List_of_Emails':mail}
    
    #print(seeg)
    print("urls adnashkdbaskdsab a isdas-     -------------------------------------------------------------- ")
    print(urls_in_body)
    newdictt = { 
                "emailDetails": 
                    { 
                     "senderEmail": fromm , 
                     "receivedOn" : date , 
                     "subject" : sub , 
                     "putsIn":cc , 
                     "recievers" : 
                             { 
                                "to": to ,
                                "cc":cc,
                             },
                     "extractedEmails":mail ,
                     "extractedContacts":phone,
                        "url":url_signature
                    },
                "senderDetails":   #signature
                    {
                        "email": fromm,
                        "name" : name,      #done
                        "imageURL": url,
                        "contact": seeg["phone"],
                        "occupation": seeg["designation"],      #Spacy se train
                        "companyName": "none",             #Spacy se train 
                        "tone": tone,            #donerabbit
                        "relatedURLs":
                        {
                         
                           "domains":seeg["domain"]              #done
                        },
                       	"designation" : seeg['designation']
                    }
                }
    ans=retjson(newdictt)
    
   
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
