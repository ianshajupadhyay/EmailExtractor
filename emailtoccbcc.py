from email.utils import getaddresses
import email

msg="""To: user1@company1.com, John Doe <user2@example.com>, "Public, John Q." <user3@example.com>
From: anotheruser@user.com
Subject: This is a subject

This is the message.
"""
msg = email.message_from_string(msg)   

tos = msg.get_all('to', [])
ccs = msg.get_all('cc', [])
resent_tos = msg.get_all('resent-to', [])
resent_ccs = msg.get_all('resent-cc', [])
all_recipients = getaddresses(tos + ccs + resent_tos + resent_ccs)



print("-----------------------------------------\n")
print(tos)
print("-----------------------------------------\n")
print(ccs)

print("-----------------------------------------\n")

