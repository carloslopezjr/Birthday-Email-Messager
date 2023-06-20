from datetime import datetime  # import the time library into the program

import time

import random

# 11am == 11:00
def storingNames(name, birthday, phone, birthdayToday = False):
    None

def currentTime():

    global currentDate
    global currentHour

    # displays current time with specific formatting
    currentHour = datetime.now().time().strftime("%H:%M")

    # get the current date in the / / / format
    currentDate = datetime.now().strftime("%m/%d")

    return currentHour, currentDate


def birthdayFinder():

    # we want to loop through the person info list
    x = 0
    while x < len(personInfo):

        if currentDate == personInfo[x]["birthday"]:

            # get the value of key "name"
            name = personInfo[x]["name"]
            # print out a specific statement including the name

            print(f"It's {name}'s birthday!")

            personInfo[x]["birthdayToday"] = True
            x += 1

        else:
            x += 1


def dailyChecker():

    timer = 0
    while timer == 0:

        currentTime()  # run function

        # if current time is 11:00
        if currentHour == "11:00":

            # check to see if it's someones birthday today
            birthdayFinder()  # run function
            timer += 1

        else:
            # no birthday detected
            print(f"No Birthday Detected {currentHour}")

            # pauses between each while interval
            time.sleep(60)


def personalizedMessage():

    # data of messages that will randomly be sent
    messages = ["Wishing you a fantastic birthday filled with joy and laughter!",
                "I hope you have a good day!",
                "Sending you heartfelt wishes on your special day.", "Cheers to another year of amazing friendship!", "Enjoy your special day to the fullest!", "Have an absolutely fantastic day!", "May this day mark the beginning of an extraordinary year for you.", "Sending you lots of love and happiness on your birthday.", "May this year be filled with exciting opportunities, great accomplishments, and endless happiness."


                ]

    x = 0
    while x < len(personInfo):
        if personInfo[x]["birthdayToday"] == True:

            # get the value of key "name"
            name = personInfo[x]["name"]

            randomIndex = random.randrange(len(messages))

            print(f"Happy Birthday {name}! {messages[randomIndex]}")
            x += 1


# data base of information
personInfo = [{
    "name": "Carlos",
    "birthday": "06/20",
    "phone": "210-419-0444",
    "birthdayToday": False
},

    {
        "name": "Kyra",
        "birthday": "04/11",
        "phone": "961-775-2092",
        "birthdayToday": False
}
]


# Outputs

'''dailyChecker()'''
currentTime()
birthdayFinder()
personalizedMessage()
