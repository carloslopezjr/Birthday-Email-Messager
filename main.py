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

        currentTime()

        if currentHour == "21:34":
            # print("It's time to check if anyone has a birthday today!")
            birthdayFinder()
            timer += 1

        else:
            print(f"No Birthday Detected {currentHour}")

        time.sleep(60)


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
},
    {
        "name": "Kyra",
        "birthday": "06/20",
        "phone": "961-775-2092",
        "birthdayToday": False
}
]



# Outputs
# dailyChecker()

currentTime()
birthdayFinder()

print(personInfo)
