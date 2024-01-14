import os
import pytube
import requests
import youtube_dl


def mkdir(path_to_dowbload):
    if not os.path.exists(path_to_dowbload):
        os.makedirs(path_to_dowbload)

def youtube_download(url, path_to_dowbload):
    mkdir(path_to_dowbload)
    video_with_highest_resolution = pytube.YouTube(url).streams.get_highest_resolution()
    video_with_highest_resolution.download(f"./{path_to_dowbload}")


def reddit_download(url, path_to_dowbload):
    response = requests.get(url + ".json")
    data = response.json()
    for video in data["data"]["children"]:
        if "secure_media" in video["data"] and video["data"]["secure_media"] is not None:
            if "reddit_video" in video["data"]["secure_media"]:
                video_url = video["data"]["secure_media"]["reddit_video"]["fallback_url"]
                mkdir(path_to_dowbload)
                ydl_opts = {
                    "outtmpl": os.path.join(path_to_dowbload, "%(title)s.%(ext)s"),
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])


def process(urls):
    for url in urls:
        if "youtube.com" in url:
            youtube_download(url, "youtube_download")
        elif "reddit.com" in url:
            reddit_download(url, "reddit_download")


if __name__ == "__main__":
    URLS = [
        "https://www.youtube.com/watch?v=pArgZVW4408",
        "https://www.reddit.com/r/Damnthatsinteresting/"
    ]
    process(URLS)
