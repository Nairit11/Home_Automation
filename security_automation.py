import time
import serial
import smtplib
import email.utils
 
TO = 'RECEIVER MAIL_ID'
GMAIL_USER = 'SENDER MAIL_ID'
GMAIL_PASS = 'SENDER PASSWORD'
 
SUBJECT = 'Someone is there at your doorstep'
TEXT = 'Doorstep Detection-Someone is there at your doorstep. Get the live CCTV footage at: http://IP_ADDRESS_OF_YOUR IP_WEBCAM' 
  
ser = serial.Serial('COM3', 9600) 
 
def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print(header)
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()
    
while True:
    message = ser.readline()
    print(message)
    
    if message[0:4] == 'Door':
        send_email()
    time.sleep(1)
