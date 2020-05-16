import pytube
import yt_email
import time 

def getvideos():
    links = yt_email.get_video_links()
    if links == []: 
        time.sleep(60)
        getvideos()

    for link in links:
        print(link)
        pytube.YouTube(link).streams.first().download('.')
        
if __name__ == '__main__':
    getvideos()
