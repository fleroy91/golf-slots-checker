import requests
import json
from datetime import date, timedelta

START_TIME = "06:00"
END_TIME = "10:00"
FRIDAY = True
SATURDAY = True
TROON = True
VIYA = True

def get_troon(date):
    if not TROON:
        return
    TROON_ENDPOINT= "https://apilive.back9solutions.com/api/assets"
    TROON_BEARER= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGlsaXZlLmJhY2s5c29sdXRpb25zLmNvbVwvYXBpXC9vdHBzXC92ZXJpZnkiLCJpYXQiOjE2Mzc2NDE3ODcsImV4cCI6MTY0MTI0MTc4NywibmJmIjoxNjM3NjQxNzg3LCJqdGkiOiJtdUIxdTc2RmplSVZDc0hTIiwic3ViIjoyNjE4OSwicHJ2IjoiNGFjMDVjMGY4YWMwOGYzNjRjYjRkMDNmYjhlMWY2MzFmZWMzMjJlOCJ9.pgj06jlqtSyDRcWbkziaq9fXKwUBWqB2kYGpx0ZbCDE"
    TROON_GOLFS = {
        "9": "Montgommerie",
        "11": "Arabian Ranches",
        "1": "Els",
        "49": "Dubai Hills"
        # "4": "Al Zorah"
        }
    # https://apilive.back9solutions.com/api/assets/9/slots/2021-12-17?page=1&start_time=00:00&available_spaces=1&include=rate,location,prices

    for course_id in TROON_GOLFS:
        course_name = TROON_GOLFS[course_id]
        url = "{}/{}/slots/{}".format(TROON_ENDPOINT, course_id, date)
        # print(url)
        headers = {
            "Host": "apilive.back9solutions.com",
            "Authorization": "Bearer {}".format(TROON_BEARER),
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            "X-Platform-Token": "troonkey"
        }
        params = {
            "page": 1,
            "start_time": START_TIME,
            "end_time": END_TIME,
            "available_spaces": 1,
            "include": "rate,location,prices"
        }
        # print(params)
        res = requests.get(url, params=params, headers=headers, timeout=30)
        result = res.json()
        # print(result)
        data = result["data"]
        first = True
        for nb_slots in range(4, 0, -1):
            for elem in data:
                if elem["available_spaces"] == nb_slots:
                    for price in elem["prices"]["data"]["channels"]["data"]:
                        if price["name"] == "TEC":
                            if first:
                                print("{}".format(course_name))
                                first = False
                            tee = elem["location"]["data"]["name"]
                            print("    {} - {} joueurs - dh{} - {}".format(elem["start_time"][11:16], elem["available_spaces"], price["prices"]["user"], tee[0:4]))
                            break
                    break

def get_viya(date):
    if not VIYA:
        return
    VIYA_ENDPOINT= "https://wasl-api.reciproci.com/api/ns/customer/nonmember/v6/findAvailability"
    VIYA_BEARER="c4289c92-2dbd-4448-846c-5eb23f7ae81b"

    url = VIYA_ENDPOINT
    date_str = "{}".format(date)
    # print(url)
    headers = {
        "Host": "wasl-api.reciproci.com",
        "Authorization": "Bearer {}".format(VIYA_BEARER),
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "LANGUAGE": "EN",
        "User-Agent": "Viya/1 CFNetwork/1312 Darwin/21.0.0",
        "DEVICE_ID": "B4634D93-6E01-4DFF-A660-A535DFF6111D"
    }
    data = {
    "bookings":[
        {
            "pax":1,
            "courseID":"97101-201-0000000002",
            "incShotGunTimes":True,
            "mType":"744,745,746,782,784,1004,1032,1016,1113,1143,1144,1145,1063,1013",
            "clubID":2,
            "holes":18,
            "bookingTime":START_TIME,
            "bookingDate":date_str
        },
        {
            "incShotGunTimes":False,
            "mType":"744,745,746,782,784,1004,1016,1143,1144,1145,1063,1113",
            "pax":1,
            "bookingTime":START_TIME,
            "clubID":3,
            "holes":18,
            "bookingDate":date_str,
            "courseID":"97101-201-0000000019"
        },
        {
            "holes":18,
            "courseID":"97101-201-0000000020",
            "pax":1,
            "bookingTime":START_TIME,
            "clubID":3,
            "bookingDate":date_str,
            "mType":"744,745,746,782,784,1004,1016,1143,1144,1145,1063,1113",
            "incShotGunTimes":True
        },
        {
            "clubID":1,
            "bookingDate":date_str,
            "holes":18,
            "incShotGunTimes":False,
            "courseID":"97101-201-0000000006",
            "pax":1,
            "mType":"744,745,746,782,784,1058,1004,1143,1144,1145,1063,1113",
            "bookingTime":START_TIME
        },
        {
            "clubID":3,
            "bookingDate":date_str,
            "incShotGunTimes":False,
            "mType":"744,1005,1016,1082",
            "holes":18,
            "pax":1,
            "courseID":"97101-201-0000000028",
            "bookingTime":START_TIME
        }
    ],
    "mTypeList":[
        {
            "isDynamic":False,
            "playerTypeID":744,
            "isDefault":True
        },
        {
            "isDynamic":False,
            "playerTypeID":745,
            "isDefault":False
        },
        {
            "isDefault":False,
            "isDynamic":False,
            "playerTypeID":746
        },
        {
            "playerTypeID":782,
            "isDefault":False,
            "isDynamic":False
        },
        {
            "isDefault":False,
            "playerTypeID":784,
            "isDynamic":False
        },
        {
            "isDefault":False,
            "isDynamic":True,
            "playerTypeID":1004
        },
        {
            "isDefault":False,
            "playerTypeID":1032,
            "isDynamic":True
        },
        {
            "isDefault":False,
            "isDynamic":True,
            "playerTypeID":1016
        },
        {
            "playerTypeID":1113,
            "isDynamic":True,
            "isDefault":False
        },
        {
            "playerTypeID":1143,
            "isDefault":False,
            "isDynamic":True
        },
        {
            "isDefault":False,
            "isDynamic":True,
            "playerTypeID":1144
        },
        {
            "playerTypeID":1145,
            "isDefault":False,
            "isDynamic":True
        },
        {
            "playerTypeID":1063,
            "isDefault":False,
            "isDynamic":True
        },
        {
            "isDefault":False,
            "isDynamic":False,
            "playerTypeID":1013
        },
        {
            "playerTypeID":1146,
            "isDefault":False,
            "isDynamic":True
        },
        {
            "playerTypeID":1058,
            "isDynamic":False,
            "isDefault":False
        },
        {
            "isDefault":False,
            "isDynamic":True,
            "playerTypeID":1005
        },
        {
            "isDefault":False,
            "playerTypeID":1082,
            "isDynamic":True
        }
    ]
    }
    res = requests.post(url, data=json.dumps(data), headers=headers, timeout=60)
    result = res.json()
    # print(result)
    data = result["availability"]
    for elem in data:
        first = True
        course_name = elem["courseName"]
        for nb_pax in range(4, 0, -1):
            for avail in elem["timesAvail"]:
                if avail["pax"] == nb_pax:
                    p = None
                    for price in avail["priceDetailsList"]:
                        if p is None or price["price"] < p:
                            p = price["price"]

                    if first:
                        print(course_name)
                        first = False
                    tee = "1st"
                    if avail["shotgunTime"]:
                        tee = "Shotgun"
                    print("    {} - {} joueurs - dh{} - {}".format(avail["bookingTime"], nb_pax, int(p), tee))
                    break

today = date.today()
friday = today + timedelta(days=(5 - today.weekday()) % 7 - 1)
saturday = today + timedelta(days=(6 - today.weekday()) % 7 - 1)

if FRIDAY:
    print("*{} {}*".format("Friday", friday))
    get_troon(friday)
    get_viya(friday)

if SATURDAY:
    print("")
    print("*{} {}*".format("Saturday", saturday))
    get_troon(saturday)
    get_viya(saturday)
