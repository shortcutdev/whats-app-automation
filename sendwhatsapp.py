import datetime
import json
import requests
import time
import os

os.environ["TZ"] = "Time zone"
time.tzset()


# API setup
def APIsetup(number, msg):
    url = "https://whatsapp-api5.p.rapidapi.com/Sendtext"

    querystring = {"access_token":"a27e1f9ca234xxxxxxxxxxxxx","instance_id":"609ACF283XXXX","message":msg,"number":number}

    headers = {
	    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	    "X-RapidAPI-Host": "whatsapp-api5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# Reading from JSON
def read_from_json():
    jsondata = open('location of json file', 'r')
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

            if x.strftime("%x") == i["dob"] and x.strftime("%X") == "00:00:10":
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
