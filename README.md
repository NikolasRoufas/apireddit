# Reddit API Fetcher for Syrian Conflict Data

This Python script fetches posts and comments from the subreddit `/r/syrianconflict` using the Reddit API. It was developed specifically for this project to collect data for sentiment analysis, topic modeling, and other data science tasks related to online discourse on the Syrian conflict.

## Features
- **Targeted Data Collection**: Fetches data from `/r/syrianconflict` with customizable filters (keywords, date ranges, etc.).
- **Efficient Data Storage**: Organizes collected posts and comments into a structured format for easy analysis.
- **Purpose-Built**: Created solely for the purpose of this project to analyze public discussions about the Syrian conflict.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/reddit-api-fetcher.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Reddit API credentials:
    - Create a Reddit app [here](https://www.reddit.com/prefs/apps).
    - Add your `client_id`, `client_secret`, and `user_agent` to the script.

## Usage

Run the script to fetch posts and comments from `/r/syrianconflict`:

```bash
python reddit_fetcher.py
