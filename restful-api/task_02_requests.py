#!/usr/bin/python3

'''Use requests to fetch posts from JSONPlaceholder'''


import requests
import json
import csv


def fetch_and_print_posts():
    '''fetches and prints posts'''
    fetch = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {fetch.status_code}")
    if fetch.ok:
        data = fetch.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    '''fetches and saves posts to csv'''
    post_list = []
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.ok:
        posts = response.json()
        for post in posts:
            post_dict = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            post_list.append(post_dict)

    if post_list:
        keys = post_list[0].keys()
        with open("posts.csv", mode='w', newline="", encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(post_list)
