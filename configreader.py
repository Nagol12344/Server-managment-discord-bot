import json

## TODO: make a class system

def get_bot_token():
    File_object = open(r"configs/login.json", "r")
    token = json.loads(File_object.read())
    return token["bot_token"]

def check_access(id):
    File_object = open(r"configs/login.json", "r")
    json_data = json.loads(File_object.read())
    if str(id) in json_data["allowed_users"]: return True
    else: return False
