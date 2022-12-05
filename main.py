import json
from datetime import date
import boto3 

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Birthday')
    todays_date = date.today().strftime("%d/%m/%Y")
    data = table.scan()["Items"]
    for i in data:
        if i["Birthday"] == todays_date:
            print(f"Happy Birthday {i['Name']}!!!\nSend sms notification")
