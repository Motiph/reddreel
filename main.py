import praw
import settings
from utils.files import download, remove_special_chars


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
                file_url = submission.secure_media.get('reddit_video').get('fallback_url')
                url_without_format = file_url[:file_url.find('DASH') + 4]

                file_title = remove_special_chars(submission.title)

                video_path = download(name=file_title, ext=".mp4", url=submission.url)
                audio_path = download(name=file_title, ext=".mp3", url=f"{url_without_format}_audio.mp4")

if __name__ == "__main__":
    start_colecting(
        subreddit="VALORANT",
        hot=True,
        limit=6
    )