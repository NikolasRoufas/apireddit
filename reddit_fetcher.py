import praw
import pandas as pd
import csv

# Reddit API credentials
CLIENT_ID = ""
CLIENT_SECRET = ""
USER_AGENT = ""

# Initialize Reddit API connection
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Target subreddit
SUBREDDIT_NAME = ""

# CSV file to save comments
OUTPUT_FILE = ""

# Fetch comments from Reddit
def fetch_reddit_comments(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    comments_data = []

    print(f"Fetching comments from r/{subreddit_name}...")

    # Iterate over the top posts (can also use .new, .hot, etc.)
    for post in subreddit.top(limit=limit):
        print(f"Post Title: {post.title} - Fetching comments...")
        post.comments.replace_more(limit=None)  # Load all comments
        for comment in post.comments.list():
            comments_data.append({
                "post_id": post.id,
                "post_title": post.title,
                "comment_id": comment.id,
                "comment_body": comment.body,
                "comment_score": comment.score,
                "created_utc": comment.created_utc,
            })
    
    print(f"Fetched {len(comments_data)} comments.")
    return comments_data

# Save data to a CSV file
def save_to_csv(comments_data, output_file):
    df = pd.DataFrame(comments_data)
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Comments saved to {output_file}")

# Main function
if __name__ == "__main__":
    # Fetch comments
    comments = fetch_reddit_comments(SUBREDDIT_NAME, limit=10)  # Fetch top 10 posts
    # Save to CSV
    save_to_csv(comments, OUTPUT_FILE)

# This Script Was Created From Nikolaos Roufas For The Use Of Creating A CSV File For A juoyter Notebook