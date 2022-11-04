import datetime
import json
import requests
import time
import os

os.environ["TZ"] = "Asia/Calcutta"
time.tzset()


# API setup
def APIsetup(number, msg):
    url = "https://whatsapp-api5.p.rapidapi.com/Sendtext"

    querystring = {"access_token": "7cedc5331900d7bdab8716fc021da98e", "instance_id": "63601AE81D57E", "message": msg,
                   "number": number}

    headers = {
        "X-RapidAPI-Key": "f5a4b6901amsh7c47b8aad7fa8b0p15b34ajsne8376d64239d",
        "X-RapidAPI-Host": "whatsapp-api5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)


# Reading from JSON
def read_from_json():
    jsondata = open('/home/19bcn7074/whatsapp/data.json', 'r')
    js = jsondata.read()
    obj = json.loads(js)
    return list(obj)


# schedule
def schedule():
    obj = read_from_json()
    # print("read")
    flag = False
    while True:
        x = datetime.datetime.now()

        for i in obj:

            if x.strftime("%x") == i["dob"] and x.strftime("%X") == "00:04:50":
                num = i['number']
                msg = i['msg']
                # print(msg)
                APIsetup(num, msg)
                # print("success")
                flag = True
                time.sleep(60.0)

        if flag:
            break


schedule()
