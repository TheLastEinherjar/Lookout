# Lookout
Python Lookout is a Python class that allows you to fetch emails from an IMAP server and extract their contents. It is useful for automating email-based workflows.

## Contributors

- *TheLastEinherjar - Prompter/Editor*
- *Phind.com - Developer*

## Dependencies

Python Email Lookout requires the following dependencies:

- *imaplib*
- *email*

## Example

```py
from Lookout import Lookout

# create an instance of the class
lookout = Lookout(username='your_username', password='your_password')

# get all subjects
subjects = lookout.get_all_subjects()

# get all content
contents = lookout.get_all_content()

# get content by subject
content = lookout.get_all_content_by_subject('subject')

# get content by sender
content = lookout.get_all_content_by_sender_partial('sender')

# close the connection
lookout.close()
```
# o7
