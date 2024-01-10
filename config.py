import os

API_ID = API_ID = 23621134

API_HASH = os.environ.get("API_HASH", "3e49039179441fb424d90680ecffe365")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6807522515:AAFxyC3rLNHJOQ2Qq5xlG0glCImrSTRS0b8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6981453498))

LOG = -1002069641023

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6960520819").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


3e49039179441fb424d90680ecffe365
