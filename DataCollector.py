import praw

reddit = praw.Reddit(client_id = "",
 client_secret = "",
 user_agent = "DataCollector")

word = input("Enter word to be searched: ")

def Pics():
    print("Connecting to subreddit...")
    subreddit = reddit.subreddit("pics")
    global pics_x
    pics_x = 0
    global pics_y
    pics_y = 0
    post = 0
    print("\n" + "Gathering submissions...")
    for submission in subreddit.top(limit = 50):
        post += 1 
        print("\n" + f"Gathering comments in post #{post}...")        
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            pics_x += 1
            print("\n" + f"Checking comment #{pics_x}...")
            body_lower = comment.body.lower()
            if hasattr(comment, "body"):
                print("\n" + "Checking for matches...")
                if word in body_lower:
                    pics_y += 1
                    print("\n" + f"Match found. Comment: {comment.body}")
                else:
                    print("\n" + "Match not found.")
    global pics_percentage
    pics_percentage = pics_y / pics_x * 100            

def Funny():
    print("Connecting to subreddit...")
    subreddit = reddit.subreddit("funny")
    global funny_x
    funny_x = 0
    global funny_y
    funny_y = 0
    post = 0
    print("\n" + "Gathering submissions...")
    for submission in subreddit.top(limit = 50):
        post += 1 
        print("\n" + f"Gathering comments in post #{post}...")        
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            funny_x += 1
            print("\n" + f"Checking comment #{funny_x}...")
            body_lower = comment.body.lower()
            if hasattr(comment, "body"):
                print("\n" + "Checking for matches...")
                if word in body_lower:
                    funny_y += 1
                    print("\n" + f"Match found. Comment: {comment.body}")
                else:
                    print("\n" + "Match not found.")
    global funny_percentage
    funny_percentage = funny_y / funny_x * 100

def Politics():
    print("Connecting to subreddit...")
    subreddit = reddit.subreddit("politics")
    global politics_x
    politics_x = 0
    global politics_y
    politics_y = 0
    post = 0
    print("\n" + "Gathering submissions...")
    for submission in subreddit.top(limit = 50):
        post += 1 
        print("\n" + f"Gathering comments in post #{post}...")        
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            politics_x += 1
            print("\n" + f"Checking comment #{politics_x}...")
            body_lower = comment.body.lower()
            if hasattr(comment, "body"):
                print("\n" + "Checking for matches...")
                if word in body_lower:
                    politics_y += 1
                    print("\n" + f"Match found. Comment: {comment.body}")
                else:
                    print("\n" + "Match not found.")
    global politics_percentage
    politics_percentage = politics_y / politics_x * 100

def Gaming():
    print("Connecting to subreddit...")
    subreddit = reddit.subreddit("gaming")
    global gaming_x
    gaming_x = 0
    global gaming_y
    gaming_y = 0
    post = 0
    print("\n" + "Gathering submissions...")
    for submission in subreddit.top(limit = 50):
        post += 1 
        print("\n" + f"Gathering comments in post #{post}...")        
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            gaming_x += 1
            print("\n" + f"Checking comment #{gaming_x}...")
            body_lower = comment.body.lower()
            if hasattr(comment, "body"):
                print("\n" + "Checking for matches...")
                if word in body_lower:
                    gaming_y += 1
                    print("\n" + f"Match found. Comment: {comment.body}")
                else:
                    print("\n" + "Match not found.")
    global gaming_percentage
    gaming_percentage = gaming_y / gaming_x * 100

def AskReddit():
    print("Connecting to subreddit...")
    subreddit = reddit.subreddit("askreddit")
    global ask_reddit_x
    ask_reddit_x = 0
    global ask_reddit_y
    ask_reddit_y = 0
    post = 0
    print("\n" + "Gathering submissions...")
    for submission in subreddit.top(limit = 50):
        post += 1 
        print("\n" + f"Gathering comments in post #{post}...")        
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            ask_reddit_x += 1
            print("\n" + f"Checking comment #{ask_reddit_x}...")
            body_lower = comment.body.lower()
            if hasattr(comment, "body"):
                print("\n" + "Checking for matches...")
                if word in body_lower:
                    ask_reddit_y += 1
                    print("\n" + f"Match found. Comment: {comment.body}")
                else:
                    print("\n" + "Match not found.")
    global ask_reddit_percentage
    ask_reddit_percentage = ask_reddit_y / ask_reddit_x * 100
Pics()
Funny()
Politics()
Gaming()
AskReddit()
print("\n" + f"There was a match {pics_y} times in {pics_percentage}% of the data in r/Pics. {pics_x} comments scanned.")  
print(f"There was a match {funny_y} times in {funny_percentage}% of the data in r/Funny. {funny_x} comments scanned.") 
print(f"There was a match {politics_y} times in {politics_percentage}% of the data in r/Politics. {politics_x} comments scanned.")  
print(f"There was a match {gaming_y} times in {gaming_percentage}% of the data in r/Gaming. {gaming_x} comments scanned.")
print(f"There was a match {ask_reddit_y} times in {ask_reddit_percentage}% of the data in r/AskReddit. {ask_reddit_x} comments scanned.")
input("Press enter to close: ")  