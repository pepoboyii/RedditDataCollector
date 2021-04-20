import praw
from matplotlib import pyplot as plt
   

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
    
    
    #The things here are reddit secret information, get these from the reddit website developer section
    reddit = praw.Reddit(client_id = "",
                     client_secret = "",
                     user_agent = "")
    
    #populate this list with the subreddits you want to search for
    sub_list = ['pics','politics','funny']
    
    #This is obvious
    word_to_search = 'why'
   
    nof_posts = 1
      
    D = {} #Dict for plotting
    
    #Plotting
    for subreddit in sub_list:
        D[subreddit] = search(subreddit,word_to_search,nof_posts)[2]
        
    plt.bar(range(len(D)), list(D.values()), align='center')
    plt.title(f'% comments \'{word_to_search}\' showed up in')
    plt.xticks(range(len(D)), list(D.keys()))
