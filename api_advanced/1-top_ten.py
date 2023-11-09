#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def  top_ten(subreddit):
    """prints the titles of the top ten hot posts for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)        






