#!/usr/bin/env python3
from pytube import YouTube

# ! regex ile playlist mi değil mi kontrol ediliğ ona göre methodlara gönderilecek


def downloadVideo(Stream) -> None:
    try:
        print("Downloading started...")
        Stream.download()
        print("Downloading ended...")
        return True
    except:
        print("Lütfen Linki kontrol ediniz..")


def main():
    link = input("Enter the link: ")
    yt = YouTube(link)
    print("Author: ", yt.author)
    # print("Description: ",yt.description)
    print("Length: ", yt.length)
    print("Views: ", yt.views)
    print("Caption Tracks: ", yt.caption_tracks)
    print("Captions: ", yt.captions)
    print("Descramble: ", yt.descramble)
    # print("Initialize stream objects: ",yt.initialize_stream_objects)
    print("Prefetch: ", yt.prefetch)
    print("Rating: ", yt.rating)
    # print("Register on complete callback: ",yt.register_on_complete_callback)
    # print("Register on progress callback: ",yt.register_on_progress_callback)
    # print("Streams: ",yt.streams)
    print("Thumbmail URL: ", yt.thumbnail_url)
    print("Title: ", yt.title)
    print("Video ID: ", yt.video_id)
    print("Watch URL: ", yt.watch_url)
    print("Age restricted: ", yt.age_restricted)
    # print("Age restricted: ",yt.streams.filter(only_video=True))
    # print("Age restricted: ",yt.streams.filter(progressive=True))

    ys = yt.streams.get_highest_resolution()
    downloadVideo(ys)


if __name__ == "__main__":
    main()
