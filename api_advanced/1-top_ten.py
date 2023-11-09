#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed
"""

import requests

def  top_ten(subreddit):
    """
    creating endpoint url
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    """ 
    user agent 
    """
    headers = {"User-Agent":"Mozilla/5.0"}
    """
    make get request
    """
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)        






