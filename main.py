import praw
import settings


def start_colecting(subreddit: str, hot: bool = True, limit: int = 5):

    reddit = praw.Reddit(
        client_id=settings.CLIENT_ID,
        client_secret=settings.SECRET,
        user_agent=settings.USER_AGENT,
        redirect_uri=settings.REDIRECT_URI
    )

    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        if submission.is_video:
            video_duration = submission.secure_media.get('reddit_video').get('duration', '')

            if video_duration < 60:
                print("starting...")



if __name__ == "__main__":
    start_colecting(
        subreddit="VALORANT",
        hot=True,
        limit=6
    )