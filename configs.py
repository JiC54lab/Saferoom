# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Safe Room](https://t.me/{BOT_USERNAME})
📝 **Language:** [Python3](https://www.python.org)
📚 **Library:** [Pyrogram](https://docs.pyrogram.org)
📡 **Hosted on:** [Heroku](https://heroku.com)
🧑🏻‍💻 **Developer:** [JiC54](https://t.me/JiC54_SERIES_Bot)
👥 **Support:** [JiC54 Support](https://t.me/jic54supportbot)
📢 **Updates Channel:** [Click Here](https://t.me/JiC54)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **JiC54 CHANNELS**
[Movies and Series 2022](https://t.me/+H_6j47erCp44YjY0)
[Latest releases only](https://t.me/+uQBJ5JaaLpgyMWI0)
[Dax songs](https://t.me/+EHBqUrMHnglmZWY8)
[DC Series](https://t.me/+8eC2YwzHZtUwZDg0)
[Marvel Movies](https://t.me/+GvVfP9p-YAsyMTY0)
[Marvel Series](https://t.me/+_dW2BNOdk2hiODVk)
[African Movies](https://t.me/+6QrMOpOVtKAxOGQ0)
[WWE wrestling](https://t.me/+LhZuWiqE21NiYzY0)
[Netflix Series](https://t.me/+DOvLtPVH3wllNDZk)
[Dax Music Videos](https://t.me/+TRppGR3YPKA1Mzg8)
[Lyrics](https://t.me/+zQ_jwfFrInY4ZGQ0)
[Animations](https://t.me/+BeSwOyG7VsAyNzZk)

**⚠️Remember that Safe Room moderators will Delete Adult Contents from Database and ban the sender. So better don't Store Those Kind of Things.**
"""
	HOME_TEXT = """
Hi [{}](tg://user?id={}),\n\nThis is **Safe Room Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
