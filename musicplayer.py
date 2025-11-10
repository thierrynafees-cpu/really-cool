import tkinter as tk
import vlc
import time
import os
import random
clear = lambda: os.system('cls')

root = tk.Tk()
root.title("woo hoo")
root.geometry('500x500')



script = os.path.dirname(os.path.abspath(__file__))

playlist_path = os.path.join(script, "music")
playlist_songsEx = os.listdir(playlist_path)
playlist_songs = {}
playedSongs = []
playing = True
order = 'normal'

for i, song in enumerate(playlist_songsEx, start=1):
    playlist_songs.update({str(i): song})


def listSongs(playlist):
    clear()
    for i in playlist:
        print(i + ": " + playlist[i])

def playSongs(playlist):
    listSongs(playlist)
    print("R: gamble")
    song_number = input()
    if song_number == "r" or "R":
        playSong(str(random.randint(1, int(list(playlist_songs.keys())[-1])))) #now thats a lot of methods lol
    else:
        playSong(song_number)

def playSong(songNumber):
    if int(songNumber) > int(list(playlist_songs.keys())[-1]):
        song = playlist_songs.get("1")
        songNumber = 1
    else:
        song = playlist_songs.get(str(songNumber))
    print(playlist_songs)
    print(song)
    audio_path = os.path.join(playlist_path, song)
    song_playing = vlc.MediaPlayer(audio_path)
    song_playing.play()
    songPlaying(song, songNumber, song_playing, True)


def songPlaying(song, songNumber, player, playing):
    clear()
    global order
    
    if playing:
        print(song.rstrip(".mp3") + " is playing \n")
    else:
        print(song.rstrip(".mp3") + " is paused")
    print("order: normal")
    option = input("options: \n 1. pause/resume \n 2. next song \n 3. song before \n 4. switch order \n 5. back ")

    if option == "1":
        if player.is_playing():
            player.pause()
            playing = False
        else:
            player.play()
            playing = True

    elif option == "2":
        print(songNumber)
        player.stop()
        playSong(int(songNumber) + 1)

    elif option == "3":
        player.stop()
        if int(songNumber) - 1 < 1:
            songNumber = int(list(playlist_songs.keys())[-1])
        else:
            playSong(int(songNumber) - 1)
    
    elif option == "3":
        if order == "normal":
            order = "shuffle"
        else:
            order = "normal"

    songPlaying(song, songNumber, player, playing)
        
def home():
    clear()
    print("welcome to my music player! \n what will ye have?: \n 1. list meh le songs \n 2. just play the damn thing!")
    f = input("input nomor ")
    if f == "1":
        listSongs(playlist_songs)
    elif f == "2":
        playSongs(playlist_songs)


home()