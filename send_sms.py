# import the necessary libraries
import csv
import pymongo
from twilio.rest import Client
from datetime import datetime, timedelta

# set up the Twilio client
account_sid = 'AC95df735283415d65a03509a194f01997'
auth_token = 'b742da9359da9ee4376f4b2f692d5714'
client = Client(account_sid, auth_token)

# set up the MongoDB client
client_mongo = pymongo.MongoClient('mongodb://localhost:27017/')
db = client_mongo['medicine']
collection = db['patients']

now = datetime.now()
# read the CSV file and insert each patient's data into the MongoDB collection
with open('PatientData.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        patient = {
            'name': row[0],
            'phone_number': row[1],
            'medicine': row[2],
            'dosage': row[3],
            'days': row[4]
        }
        collection.insert_one(patient)

# query the MongoDB collection for when patients need to take certain medicines and send a reminder SMS
for patient in collection.find():
    # Check if today is one of the days the patient needs to take the medicine
    for day in patient['days']:
        if day == 'M' and now.weekday() == 0:
            message = f"Remember to take {patient['dosage']} of {patient['medicine']} today, {patient['name']}!"
            client.messages.create(
                to=patient['phone_number'], from_='+15673131536', body=message)
        elif day == 'T' and now.weekday() == 1:
            message = f"Remember to take {patient['dosage']} of {patient['medicine']} today, {patient['name']}!"
            client.messages.create(
                to=patient['phone_number'], from_='+15673131536', body=message)
        elif day == 'W' and now.weekday() == 2:
            message = f"Remember to take {patient['dosage']} of {patient['medicine']} today, {patient['name']}!"
            client.messages.create(
                to=patient['phone_number'], from_='+15673131536', body=message)
        elif day == 'Th' and now.weekday() == 3:
            message = f"Remember to take {patient['dosage']} of {patient['medicine']} today, {patient['name']}!"
            client.messages.create(
                to=patient['phone_number'], from_='+15673131536', body=message)
        elif day == 'F' and now.weekday() == 4:
            message = f"Remember to take {patient['dosage']} of {patient['medicine']} today, {patient['name']}!"
            client.messages.create(
                to=patient['phone_number'], from_='+15673131536', body=message)
