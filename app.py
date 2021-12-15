import requests
from datetime import date, timedelta

TROON_ENDPOINT= "https://apilive.back9solutions.com/api/assets"
TROON_BEARER= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGlsaXZlLmJhY2s5c29sdXRpb25zLmNvbVwvYXBpXC9vdHBzXC92ZXJpZnkiLCJpYXQiOjE2Mzc2NDE3ODcsImV4cCI6MTY0MTI0MTc4NywibmJmIjoxNjM3NjQxNzg3LCJqdGkiOiJtdUIxdTc2RmplSVZDc0hTIiwic3ViIjoyNjE4OSwicHJ2IjoiNGFjMDVjMGY4YWMwOGYzNjRjYjRkMDNmYjhlMWY2MzFmZWMzMjJlOCJ9.pgj06jlqtSyDRcWbkziaq9fXKwUBWqB2kYGpx0ZbCDE"

def get_troon(course_id, date):
    # https://apilive.back9solutions.com/api/assets/9/slots/2021-12-17?page=1&start_time=00:00&available_spaces=1&include=rate,location,prices

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
        "start_time": "{} 06:00:00".format(date),
        "end_time": "{} 11:00:00".format(date),
        "available_spaces": 1,
        "include": "rate,location,prices"
    }
    res = requests.get(url, params=params, headers=headers, timeout=30)
    result = res.json()
    print(result)

today = date.today()
friday = today + timedelta(days=5 - today.weekday())
saturday = today + timedelta(days=6 - today.weekday())

get_troon(9, friday)
get_troon(9, saturday)