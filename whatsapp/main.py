import pyautogui as pt
from time import *
import pyperclip
import os
import random

dirname = os.path.dirname(__file__)

position1 = pt.locateOnScreen(dirname + r"/smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

#Gets message



def get_messsage():
    global x, y
    position = pt.locateOnScreen(dirname + r"/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration = .5)
    pt.moveTo(x + 110, y - 45, duration =.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(15,-200)
    pt.click()
    # Retrieves copied message
    whatsapp_message = pyperclip.paste()

    print('Message Received: ' + whatsapp_message)
    return whatsapp_message

# Posts
def post_response(message):
    global x,y
    position = pt.locateOnScreen(dirname + r"/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 170, y + 20, duration = 0.01)
    pt.click()
    pt.typewrite
    pt.typewrite(message, interval=0.000001)
    pt.typewrite("\n", interval = 0.1)

# Processes response
def process_response(message):
    if "?" in str(message.lower()):
        return "Don't ask me any questions!"
    else:
        if "Monday" in message:
            return "There's no in-lab lesson today!"
        elif "Tuesday" in message:
            return "There's in-lab lesson today..."
        elif "Wednesday" in message:
            return "There's no in-lab lesson today!"
        elif "Thursday" in message:
            return "There's in-lab lesson today..."
        elif "Friday" in message:
            return "There's no in-lab lesson today!"
        else:
            return "Invalid input."



# Continuously checks for new messages
def check_for_new_messages():
    pt.moveTo(x+115, y-42, duration = .5)
    i = 0
    while i < 5:
        #Continuously checks for green dot and new messages
        try:
            position = pt.locateOnScreen(dirname + r"/green_circle.png", confidence=.9)

            if position is not None:
                print("Theres a new message (green)")
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                i += 1
        except(Exception):
            print("No new other users with messages located.")

        if pt.pixelMatchesColor(int(x+115), int(y-42), (255,255,255), tolerance=10):
            print("It's white")
            post_response(process_response(get_messsage()))
        else:
            print("No new messages yet...")
        sleep(5)


# get_messsage()

processed_message = process_response(get_messsage())
post_response("Hi! Welcome to Ayres's Whatsapp Bot.                                                                                                                          This is a demo bot that you can use to find out whether there's an in-lab lesson.                                             Here's what I can do for you:                                                                                                                                     1.Determine whether there's in-lab lessons.")
post_response("May I know what day it is? (ie. Monday)")
#Checks for a response before replying.
check_for_new_messages()
