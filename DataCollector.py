import praw



def search(sub,word,n_posts):
    
    
    subreddit = reddit.subreddit(sub)
    
    comment_count = 0
    found_count = 0
    

    print(f"\nConnecting to {sub} \nGathering submissions...")    

    
    for submission in subreddit.hot(limit = n_posts):
        
        submission.comments.replace_more(limit = None)
        
        for comment in submission.comments.list():
            
            comment_count += 1
            
            if hasattr(comment, "body") and word in comment.body.lower():
 
                found_count += 1
                               
    percentage = found_count / comment_count * 100  
    
    print(f"\nThere was a match {found_count} " \
          f"times in {percentage:.02f}% of the comments " \
              f"scanned in r/{subreddit}. {comment_count} comments scanned.")
    
    return (found_count,comment_count,percentage)
    
    

if __name__ == "__main__":
    
    
    reddit = praw.Reddit(client_id = "l-Vl3xBi9VMQow",
                     client_secret = "vynw2ab-WTBxUE0mlc6qBerm5nExig",
                     user_agent = "scraper_api")
    

    
    sub_list = ['pics','politics','funny']
    
    
    for subreddit in sub_list:
        search(subreddit,'why',1)
     
