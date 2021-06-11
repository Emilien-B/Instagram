# Import the module
from instadm import InstaDM

# Login
insta = InstaDM(username="notes_et_reglages", password='Emilien2007', headless=False, waiting=True)

# Retrieve unread messages
Messages = insta.NewMsg()
print(Messages)

# Retrieve messages with "kevin"
MessagesFromInstagramCreator = insta.NewMsg(exp="kevin")
print(MessagesFromInstagramCreator)

# Send a message to "kevin"
insta.sendMessage(user="kevin", message="Hello !")

# Send a message to "kevin" and "mikeyk"
insta.sendGroupMessage(users=['kevin', 'mikeyk'], message='Hello everyone !')