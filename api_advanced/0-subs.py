#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import resquests


def number_of_subscribers(subreddit):

    ## endpoint url
    end_pointurl = f"https://www.reddit.com/r/{subreddit}/about.json"

    ## Set a custom User-Agent header to avoid Too Many Requests error

    headers = {'User-Agent': 'Custom User-Agent'}

    ## Make a GET request to the Reddit API

    response = resquests.get(end_pointurl, headers=headers)

    ## check the status codes 

    if response.status_code  == 200:
        ## parse json response
        data = response.json()
        return data['data']['subscribers']
    else:
        ## if invalid return zero
        return 0
