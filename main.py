"""""
Fact Mailer
=====================
This program sends an appropriate fact to yur email for each day of the month.
Modify scheduler at the bottom to run this code in the bakground each day

"""""
import schedule
import time
import smtplib
import datetime as dt
from dataframe import fact_of_the_day, current_day, current_month
import json


def fact_mailer():

    try:
        #Get credentials from config file
        with open('config copy.json', 'r') as config_file:
            config = json.load(config_file)

        my_email = config['Email']['my_email']
        password = config['Email']['password']
        smtp_server = config['SMTP']['server']
        smtp_port = config['SMTP']['port']
        recipient_email = config['Email']['recipient_email']

        #Establish connnection to gmail 
        with smtplib.SMTP(smtp_server, smtp_port) as connection:

            #Add transport layer security
            connection.starttls()

            #Login to connection
            connection.login(user=my_email,password=password)

            #Send email 
            connection.sendmail(from_addr=my_email, 
                                to_addrs=recipient_email, 
                                msg=f'subject:Fact of the Day\n\n{fact_of_the_day}')
    except FileNotFoundError:
        print("Error: The specified config file does not exist.")
    except smtplib.SMTPException as e:
        print("Error occurred while connecting to the SMTP server:", e)
    except Exception as e:
        print("An error occurred, check your credentials are correct in the config file:", e)

# Schedule daily run
schedule.every().day.at("08:00").do(fact_mailer)  

#During time period you want facts, periodically check if scheduler has pending tasks 
while current_day < 14:
    schedule.run_pending()
    time.sleep(1)
