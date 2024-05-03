import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()


def instadownload(link):
    url = "https://instagram-downloader-download-photo-video-reels-igtv.p.rapidapi.com/data"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "0209cc463cmsh53405b09542842ep1e2f69jsn82b577fa4ca4",
        "X-RapidAPI-Host": "instagram-downloader-download-photo-video-reels-igtv.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    rest = response.json()['data']['result']['video_url']
    print('code: ', response.status_code)
    if response.status_code == 200:
        dict = {'video': rest}
        return dict
    else:
        return 'No'
