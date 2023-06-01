# Scraping ideas from reddit and saving them in a file called ideas_mm-dd-hh-mm.txt
import praw
from praw.models import MoreComments
import pandas as pd
import datetime

reddit_read_only = praw.Reddit(client_id="pUkhaxesSfBrdpleL15zeQ",		 # your client id
							client_secret="ZtuLcKS9Tn3YDYolsVQo0DHYOt5Pqg",	 # your client secret
							user_agent="Dasantha Edirisinghe")	 # your user agent

url = input("Enter the url: ")

submission = reddit_read_only.submission(url=url)


today = datetime.datetime.now()
filename = open(f"Ideas/{today}.txt", "w")
count = 1

for comment in submission.comments:
    if type(comment) == MoreComments:
        continue
    # post_dict["ID"].append(comment.id)
    # post_dict["Comment"].append(comment.body)
    comment_body = comment.body
    filename.write(f"COMMENT{count}:\n{comment_body}\n\n")
    count += 1