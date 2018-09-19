import pytube
import yt_email

links = yt_email.get_video_links()

for link in links:
    print(link)
    pytube.YouTube(link).streams.first().download('.')
    
