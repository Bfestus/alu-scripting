## number_of_subscribers Function

### Description
This function queries the Reddit API and returns the number of subscribers (total subscribers, not active users) for a given subreddit. If the provided subreddit is invalid or does not exist, the function returns 0.

### Requirements
- **Prototype:** `def number_of_subscribers(subreddit)`
- **Return:** If the subreddit is valid, return the number of subscribers. If not a valid subreddit, return 0.

### Hint
No authentication is necessary for most features of the Reddit API. To avoid Too Many Requests errors, make sure to set a custom User-Agent header in your API request.

### Parameters
- `subreddit` (str): The name of the subreddit for which you want to retrieve the number of subscribers.

### Return Value
- `int`: The number of subscribers of the given subreddit. If the subreddit is invalid, return 0.

### Example Usage
```python
subscribers_count = number_of_subscribers("programming")
print("Number of subscribers in the 'programming' subreddit:", subscribers_count)

