from datetime import datetime  # import the time library into the program

import time

# 11am == 11:00


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

        currentTime() # run function

        # if current time is 11:00
        if currentHour == "11:00":

            # check to see if it's someones birthday today
            birthdayFinder() # run function
            timer += 1

        else:
            # no birthday detected
            print(f"No Birthday Detected {currentHour}")

            # pauses between each while interval
            time.sleep(60)
        

def personalizedMessage():

    x = 0
    while x < len(personInfo):
        if personInfo[x]["birthdayToday"] == True:
            
            # get the value of key "name"
            name = personInfo[x]["name"]
            
            print(f"Happy Birthday {name}! I hope you have a good day!")
            x += 1


# data base of information
personInfo = [{
    "name": "Carlos",
    "birthday": "06/19",
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

dailyChecker()
personalizedMessage()
