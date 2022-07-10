#!/usr/bin/env python
import youtube_dl
def main():
    print("[RT] Redtube Simple Downloader | github.com/im-bb") #XD
    print("[!] Auto Loop Script, Use Control + C to Stop")
    directory = input("[*] Folder Directory for Saving : ")
    while True:
        url = input("[*] Redtube Videos Url : ")
        dire = directory+'/rtdl/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'best',
            'outtmpl': dire,
            'nooverwrites': True,
            'no_warnings': False,
            'ignoreerrors': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


if __name__ == '__main__':
    main()
 
