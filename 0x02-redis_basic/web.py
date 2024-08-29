#!/usr/bin/env python3

import requests
import time
from functools import lru_cache

# Dictionary to store the count of URL accesses
url_access_count = {}

# Decorator to cache the result with an expiration time of 10 seconds
def cache_with_expiry(seconds):
    def decorator_cache_with_expiry(func):
        @lru_cache(maxsize=None)
        def wrapper_cache_with_expiry(url):
            result = func(url)
            time.sleep(seconds)  # Simulating a slow response
            return result
        return wrapper_cache_with_expiry
    return decorator_cache_with_expiry

# Function to get page content with caching and tracking access count
@cache_with_expiry(10)  # Set cache expiration time to 10 seconds
def get_page(url):
    global url_access_count
    if url in url_access_count:
        url_access_count[url] += 1
    else:
        url_access_count[url] = 1

    response = requests.get(url)
    return response.text

# Test the function with a sample URL
if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com'
    
    for i in range(3):
        content = get_page(url)
        print(f"Accessed URL: {url}")
        print(f"Content: {content}")
        print(f"Access Count for {url}: {url_access_count[url]}")
        time.sleep(2)
