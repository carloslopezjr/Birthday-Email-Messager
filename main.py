from datetime import datetime  # import the time library into the program

import time 

import random

from email.message import EmailMessage

import ssl

import smtplib


# function that makes it easy to store names // not working yet
def storingNames(name, birthday, phone, birthdayToday=False):
    None

# gets current time
def currentTime():

    global currentDate
    global currentHour

    # displays current time with specific formatting
    currentHour = datetime.now().time().strftime("%H:%M")

    # get the current date in the / / / format
    currentDate = datetime.now().strftime("%m/%d")

    # print(currentDate, currentHour) // test 

    return currentHour, currentDate

# uses currentTime() to find if a birthday matches current date
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

# checks time, and finds who's birthday is today
def dailyChecker():

    global currentHour2

    timer = 0
    while timer == 0:

        currentTime()  # run function

        # if current time is 11:00
        if currentHour == "00:00":

            # check to see if it's someones birthday today
            birthdayFinder()  # run function
            timer += 1

        else:
            # no birthday 
            currentHour2 = datetime.now().time().strftime("%H:%M:%S")
            print(f"No Birthday Detected {currentHour2}")

            # pauses between each while interval
            time.sleep(60)

# drafts email message
def personalizedMessage():

    # data of messages that will randomly be sent
    messages = ["Wishing you a fantastic birthday filled with joy and laughter!",
                "I hope you have a good day!",
                "Sending you heartfelt wishes on your special day.", "Cheers to another year of amazing friendship!", "Enjoy your special day to the fullest!", "Have an absolutely fantastic day!", "May this day mark the beginning of an extraordinary year for you.", "Sending you lots of love and happiness on your birthday.", "May this year be filled with exciting opportunities, great accomplishments, and endless happiness."
                ]
    
    randomMessage = random.choice(messages)
    
    return randomMessage

# sends emails to people
def emailSender(email_reciever, body):
    email_sender = 'carlosssolrac1@gmail.com'
    email_password = ""

    subject = "Happy Birthday!"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

    currentHour3 = datetime.now().time().strftime("%H:%M:%S")
    print(f"Email sent exactly at {currentHour3}")

# starts the program
def start():

    dailyChecker()

    x = 0
    while x < len(personInfo):
        if personInfo[x]["birthdayToday"] == True:

            # find the email of the person's birthday
            email = personInfo[x]['email']
            message = personalizedMessage()  # draft the message for the person
            # send the message to designated persons or persons'
            emailSender(email, message)

            x += 1

# data base of information
personInfo = [{
    "name": "Carlos",
    "birthday": "06/19",
    "phone": "",
    "email": "",
    "birthdayToday": False
},

    {
        "name": "Kyra",
        "birthday": "04/11",
        "phone": "",
        "email": "",
        "birthdayToday": False
}
]

# starts the program exactly at 00 seconds
def preStart():

    x = 0
    while x == 0:

        time = datetime.now().time().strftime("%S")
        
        int_time = int(time)
        
        if int_time == 00:
            start()
            x = 1


# outputs
if __name__ == "__main__":
    print("Starting the program...")
    preStart()
