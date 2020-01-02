from email.utils import parsedate_to_datetime
from datetime import datetime, date

msg="""To: user1@company1.com, John Doe <user2@example.com>, "Public, John Q." <user3@example.com>
From: anotheruser@user.com
Subject: This is a subject
Mon, 16 Nov 2009 13:32:02 +0100
This is the message.
"""

msg  = parsedate_to_datetime("Mon, 16 Nov 2009 13:32:02 +0100")
print(msg)