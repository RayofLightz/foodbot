# Foodbot
# An automated recipe planner written
# in python 
# Written by Tristan Messner
import requests
import smtplib
import json
from email.message import EmailMessage 
import os

####################
# Global variables #
####################

url = "https://www.reddit.com/r/recipes"
user_agent = {"user-agent":"cookbot"}

def get_config():
    # Gets the configs located under
    # $HOME/.config/foodbot.json
    home = os.getenv("HOME")
    default_config = home + "/.config/foodbot.json"
    config = open(default_config,"r")
    j = json.loads(config.read())
    config.close()
    return j
    
     

def get_recipies():
    # Get 5 recepies from reddit
    rurl = url + "/hot.json"
    r = requests.get(rurl,params={"limit":5},headers=user_agent)
    json_stuff = r.json()
    # Formats them into a string for an email
    a = "Your weekly meal plan from /r/recipes\n"
    for i in range(5):
        a += json_stuff["data"]["children"][i]["data"]["title"]
        a += " url "
        a += "https://www.reddit.com" + json_stuff["data"]["children"][i]["data"]["permalink"]
        a += "\n"
    # gets config
    cfg = get_config()
    send_email(a,cfg["bot_email"],cfg["bot_password"],cfg["to_email"])



def send_email(content,bot_addr,bot_passwd,to_addr):
    # Connects to gmail with the bots creads and sends
    # the recipes and links to the user
    s = smtplib.SMTP_SSL("imap.gmail.com")
    s.login(bot_addr,bot_passwd)
    msg = EmailMessage()
    msg.set_payload(content)
    msg["From"] = bot_addr 
    msg["Subject"] = "You weekly recipie list"
    msg["To"] = to_addr 
    s.send_message(msg)

get_recipies()
