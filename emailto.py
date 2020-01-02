msg="""To: user1@company1.com, John Doe <user2@example.com>, "Public, John Q." <user3@example.com>
From: anotheruser@user.com
Subject: This is a subject

This is the message.
"""

import email
'''
msg822 = email.message_from_string(msg)
for to in email.utils.getaddresses(msg822.get_all("To", [])):
    print("To:",to)
'''
msg = email.message_from_string(msg)  
print(msg)