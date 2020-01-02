import talon
from talon.signature.bruteforce import extract_signature
import warnings
import email
import re   
import json



warnings.filterwarnings("ignore" , category=DeprecationWarning)

message = """"
---------- Forwarded message ---------
From: Vasudha Sutar <vasudha@mollatech.com>
Date: Thu, Jan 2, 2020 at 11:40 AM
Subject: Re: Features Required in Mail
To: Radha kavade <radha@mollatech.com>
Cc: sayli bagwade <sayli@mollatech.com>, shubham d <dshubham@mollatech.com>


Test mail for email parser
On Thu, Jan 2, 2020 at 10:48 AM Radha kavade <radha@mollatech.com> wrote:


---------- Forwarded message ---------
From: Bharat Swaroop <bharat@mollatech.com>
Date: Thu, Jan 2, 2020 at 10:18 AM
Subject: Features Required in Mail
To: Radha kavade <radha@mollatech.com>




--




Radha Kavade


UX/UI Designer & Visualizer

M: + 91 777 587 8331

S: a71894c1b73259ad

E: radha@mollatech.com | www.blue-bricks.com

Office No : 308, Amanora chambers, Hadapsar | 

411028, Pune

"""

text, signature = extract_signature(message)
#print(signature)
li = signature.split("\n")
#print(li)
p = []
for i in li:
    if(i == "--" or i == ""):
        continue
    else:
        p.append(i)
print("\n---------------------------------------------------------------\n")
print(p)
print("\n---------------------------------------------------------------\n")


lst = re.findall('\S+@\S+', signature)   




urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', signature)
#print(urls)

regex= "\w{3} \w{3} \w{4}"

phone = re.findall(regex, signature) 

#print(phone)


#print(lst)

Dict = {}
Dict.update( {'Name' : p[0]})
Dict.update({'Position' : p[1]})
#d = ['Name' , 'Position' , 'Mobile' , 'Skype' , 'Email' , 'company' , 'Address']
msg = email.message_from_string(signature)  
Dict.update({'email' : lst})
Dict.update({'company' : urls})
Dict.update({'phone' : phone})
#Dict.update('Phone no')
#print(Dict) 

json = json.dumps(Dict)
print(json)


