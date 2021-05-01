# Packages needed
import smtplib
from csv import DictReader
from random import choice
from email.message import EmailMessage
from time import sleep

def store_csv(csv_path):
    """
    csv_path, string
    This function takes in a csv and returns a list of dictionaries for each row in the csv.
    """
    students = []
    with open(csv_path, "r") as readcsv:
        csv_dict_reader = DictReader(readcsv)
        for row in csv_dict_reader:
            # append 1 dictionary per row (each row = 1 student) to a list
            students.append(row)
    return students

def send_email(student, sender, sender_password, subject, content):
    """
    student, string 
    sender, string
    sender_password, string
    subject, string
    content, string
    This function receives a student email, a sender email, the password of the sender email in order to login in to the server, a subject and the content of the email. The function then sends the email accordingly.
    """
    # Write Email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = student
    msg.set_content(content)

    # Send Email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(sender, sender_password)
        server.send_message(msg)
        server.quit()
        print('Email sent successfully!')
    except:
        print('Error!\nEmail not sent.')

# Write the path to the specific csv and Email message
csv_path = r'C:\Users\Westbrook\Downloads\exam.csv'

# Store result of first function -> it returns a list with a dictionary for each student
students = store_csv(csv_path)

# Store the Email from the random student selected to present the book in class
book_student = choice(students)['Email']

# Ask for the senders email and password
prof_email = str(input())
prof_password = str(input())

# Set the email subject
subject = 'Live Project test results'

# Run a loop for each student and send in a personalized email
for student in students:
    # Set the email content
    email_content = 'Dear {0},\n Your score for the book assignment is broken down below by question number.\n\n1.{1}:{2}\n\n2.{3}:{4}\n\n3.{5}:{6}'.format(student['First Name'], student['Problem 1 score'], student['Problem 1 comments'], student['Problem 2 score'], student['Problem 2 comments'], student['Problem 3 score'], student['Problem 3 comments'])
    # Add another line if the student has to present the book
    if student['Email'] == book_student:
        email_content += '\n\nYou\'ve been randomly chosen to present a summary of the book in the next class. Looking forward to it!'

    # Send the email
    send_email(student['Email'], prof_email, prof_password, subject, email_content)

    # Wait 1 second between Emails
    sleep(1)