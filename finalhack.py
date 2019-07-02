from __future__ import unicode_literals
import json
import pygame

import pyglet 
from pygame import mixer, event, init


import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'outtmpl': 'C:\\Users\\ADMIN\\Desktop\\c4t\\Sesson2\\Sesson12\\finalhack\\%(title)s.%(ext)s',
    'default_search': 'ytsearch5',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
from youtube_dl import YoutubeDL


ydl = YoutubeDL(ydl_opts)

print("Welcome to music app!")

while True:
    with open('C:\\Users\\ADMIN\\Desktop\\c4t\\Sesson2\\Sesson12\\finalhack\\database.json') as json_files:
        current_database = json.load(json_files)
    def songlist():
        if len(current_database) == 0:
            print("You don't have any song!")    
        else:
            for i in range(len(current_database)):
                print(f"{i+1}. {current_database[i]['title']}")

    print("""Pick one of these options:
    1. Show all songs
    2. Show details of a song
    3. Play a song
    4. Search and download songs
    5. Exit:""")
    while True:
        selection = int(input(">>>"))
        if selection in [1,2,3,4,5]:
            break
        else:
            print('Invalid Command !!')

    if selection == 1 : 
        songlist()
            

    elif selection == 2:
        songlist()
        song = int(input("Enter the number of the song you want to see detail: "))
        while True:
            if song in range(1, len(current_database)+1):
                break
            else:
                print("Invalid song!")
        for k, v in current_database[song-1].items():
            print(f'{k}: {v}')
       
      

    elif selection == 3:
        
        songlist()
        song = int(input("Which song do you want to hear? >>> "))
            
        
      
        mixer.init()
        mixer.music.load(f"""{current_database[song-1]['title']}.mp3""".encode('utf8'))
        
        
        

        mixer.music.play()
        

        

        
        
        while True:
            choose = input("Play/ Pause/ Stop ? >> ")
            if choose.upper() == "PLAY":
                mixer.music.unpause()
            elif choose.upper() == "PAUSE":
                mixer.music.pause()
            elif choose.upper() == "STOP":
                mixer.music.stop()
                break 
        
            
        


    elif selection == 4:
        keyword = input('Enter the name of the song you want to search >>> ')
        search_result = ydl.extract_info(keyword, False)
        for i in range(5):
            print(f"""{i+1}. {search_result['entries'][i]["title"]}""")


        ask = input("Which song do you want to choose? (Enter a number or enter n to out the download!) ")
        while True:
            if ask.isdigit():
                if int(ask) in [1,2,3,4,5]:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([search_result['entries'][int(ask) - 1]['webpage_url']])
                    print("Your song have been downloaded")
                    new_data = {
                        'title': search_result['entries'][int(ask)-1]['title'],
                        'creator': search_result['entries'][int(ask)-1]['creator'],
                        'artist': search_result['entries'][int(ask)-1]['artist'],
                        'track': search_result['entries'][int(ask)-1]['track']
                    }
                    data = []
                    data.extend(current_database)
                    data.append(new_data)

                    with open('C:\\Users\\ADMIN\\Desktop\\c4t\\Sesson2\\Sesson12\\finalhack\\database.json', 'w') as outfile:
                        json.dump(data, outfile)
                    break
                else:
                    print("Invalid number! Enter the number again!")
            elif str(ask).upper() == "N":
                break
            else:
                print("")
                print("Invalid command !!!")
        

        

    elif selection == 5:
        print('See you later!!!')
        break
    