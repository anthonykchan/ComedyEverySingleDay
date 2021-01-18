import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
lastjoke = ""

def getjoke():
    jk1 = ("What do you call a hen that counts her eggs? \na mathmachicken.")
    jk2 = ("What do you call a story about a broken pencil? \nPOINTLESS.")
    jk3 = (
        "What's a pirate's favorite letter? \nYou'd think it was 'r' but tis the 'c' they love!'"
    )
    jk4 = ("What do you call a plastic noodle? \nan impasta!")
    jk5 = (
        "Patient: Doctor! Doctor! I think im loosing my memory! \nDoctor when did that happen?\nPatient: When did what happen?!"
    )
    jk6 = (
        "Why did the student eat his homework?\nThe teacher told him it has a piece of cake"
    )
    jk7 = ("How do you spell a mouse trap with only 3 letters? \nC-A-T!")
    jk8 = (
        "What did the dog say when his owner told him to stop chewing the newspaper?\nYou took the words out of my mouth!"
    )

    jk9 = ("Which cats are great at bowling?\nAlley cats!")

    jk10 = (
        "An exercise for people who are out of shape: Begin with a five-pound potato bag in each hand. Extend your arms straight out from your sides, hold them there for a full minute, and then relax. After a few weeks, move up to ten-pound potato bags. Then try 50-pound potato bags, and eventually try to get to where you can lift a 100-pound potato bag in each hand and hold your arms straight for more than a full minute. Once you feel confident at that level, put a potato in each bag."
    )

    jk11 = (
        "Did you hear about the cat that sucked a lemon?\nHe was a sour puss!")

    jk12 = ("What do you give a sick parrakeet?\nTweetment!")

    jk13 = ("Why was the pig covered in ink?\nBecause it lived in a pen!")

    jk14 = (
        "Why do pig make terrible drivers?\nBecause they are all road hogs!")

    jk15 = ("Where do you buy baby birds?\nAt the Chickout!")

    jk16 = (
        "My daughter received this e-mail from a prospective student prior to the start of the semester: “Dear Professor, I won’t be able to come to any of your classes or meet for any of the tests. Is this a problem?"
    )

    jk17 = (
        "With a patient in my medical exam room  Me: How old are your kids?  Patient: Forty-four and 39 from my wife who passed away, and from my second wife, 15 and 13.  Me: That’s quite the age difference!  Patient: Well, the older ones didn’t give me any grandkids, so I made my own"
    )

    jk18 = (
        " definition of a perfectionist: someone who wants to go from point A to point A+"
    )

    jk19 = (
        "Traveling through the Midwest, I stopped at an Ohio welcome center to pick up a state map. I found plenty of brochures but no maps. Then I spotted two employees and asked whether they had any. Sure, said the first guy. I’ll get you one. As he walked to the back, the second guy explained, We keep them in the storage room. If we leave them out on the counter, people just come in and take them."
    )

    jk20 = (
        "When my local barista handed me my change, one coin stood out. 'Look at that. You rarely get one of these old wheat pennies nowadays', I said, tapping the sheaf of-wheat design. I handed her the penny. Turning it over and over in her hand, she said,'You know, I always thought they were made of copper.'"
    )

    jk21 = (
        "One of my wife’s third graders was wearing a Fitbit watch, which prompted my wife to ask, 'Are you tracking your steps?'  'No,' said the little girl. 'I wear this for Mommy so she can show Daddy when he gets home'."
    )

    jk21 = (
        "During a job interview at the 99 Cents store, my son was asked, Where do you see yourself in five years? My son’s reply: At the Dollar Store. He got the job."
    )

    jklist = [
        jk1, jk2, jk3, jk4, jk5, jk6, jk7, jk8, jk9, jk10, jk11, jk12, jk13,
        jk14, jk15, jk16, jk17, jk18, jk19, jk20, jk21
    ]

    global lastjoke 
    if lastjoke in jklist:
      jklist.remove(lastjoke)
    
    randomjk = random.choice(jklist)
  
    lastjoke = randomjk

    return randomjk


def subscribe(name, email):

    #Email Account
    email_sender_account = "comedy.every.single.day@gmail.com"
    email_sender_username = "comedy.every.single.day"
    email_sender_password = "Xugfy9-pavsak-xegbyw"
    email_smtp_server = "smtp.gmail.com"
    email_smtp_port = 587

    #Email Content
    email_subject = "ComedyEverySingleDay Subscription"
    email_body = "<html><body>Hi " + name + ",<p>Looks like you subscribed to ComedyEverySingleDay! Here's a joke to start you off:</p>" + getjoke() + "<p>Whenever you want another joke to brighten your day, just say yes on our program and you will recieve a joke. We hope you have fun with our program and thanks for subscribing!</p></body></html>"
    
    #login to email server
    server = smtplib.SMTP(email_smtp_server, email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)
    #sending emails to all email recipients
    print("Sending email to {}".format(email))
    message = MIMEMultipart('alternative')
    message['From'] = email_sender_account
    message['To'] = email
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'html'))
    text = message.as_string()
    server.sendmail(email_sender_account, email, text)

    server.quit()


def send_email(name, email):

    #Email Account
    email_sender_account = "comedy.every.single.day@gmail.com"
    email_sender_username = "comedy.every.single.day"
    email_sender_password = "Xugfy9-pavsak-xegbyw"
    email_smtp_server = "smtp.gmail.com"
    email_smtp_port = 587

    #Email Content
    email_subject = "ComedyEverySingleDay Subscription"
    email_body = "<html><body>Hi " + name + ",<p>Here's another joke:</p>" + getjoke() + "<p>Whenever you want another joke, just say yes on our program again and you will recieve a new joke. We hope you continue to have fun with our program and thanks for subscribing!</p></body></html>"

    #login to email server
    server = smtplib.SMTP(email_smtp_server, email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)

    #For loop, sending emails to all email recipients
    print("Sending email to {}".format(email))
    message = MIMEMultipart('alternative')
    message['From'] = email_sender_account
    message['To'] = email
    message['Subject'] = email_subject
    message.attach(MIMEText(email_body, 'html'))
    text = message.as_string()
    server.sendmail(email_sender_account, email, text)

    server.quit()
    print("You should have gotten an email.")


status = input("Hi👋, Welcome to ComedyEveryDay!\n Have you subscribed , yes or no? ")

if status.lower() == "no":
    print("To subscribe, please fill out the following.")
    name = input("What's your name? ")
    print("Hi " + name + "!")
    email = input("What is your email? ")
    subscribe(name, email)
    should_continue = True
    while should_continue:
        response = input("Would you like another joke, yes or no? ")
        if response.lower() == "yes":
            print("You should get an email🤟.")
            send_email(name, email)
        elif response.lower() == "no":
            print("Okay, see you next time😁 !")
            should_continue = False
        else:
            print("Sorry I don't understand🧐")
else:
    print("Welcome back!")
    name = input("What's your name? ")
    print("Hi " + name + "!")
    email = input("What is your email? ")
    subscribe(name, email)
    should_continue = True
    while should_continue:
        response = input("Would you like another joke, yes or no? ")
        if response.lower() == "yes":
            print("You should get an email🤟.")
            send_email(name, email)
        elif response.lower() == "no":
            print("Okay, see you next time😁 !")
            should_continue = False
        else:
            print("Sorry I don't understand🧐")

