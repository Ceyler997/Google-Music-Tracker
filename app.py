'''App for collecting statistig from Google Music'''
from gmusicapi import Mobileclient
from configer import AppSetup
from handler import LibraryHandler

print('Start')

SETUP = AppSetup('config.ini')
if not SETUP:
    exit(-1)

API = Mobileclient()
LOGIN, PASSWORD = SETUP.get_login_info()
LOGIN_RESULT = API.login(LOGIN, PASSWORD, Mobileclient.FROM_MAC_ADDRESS)

if not LOGIN_RESULT:
    print("Can't sign you in. Please, use app specific password in case \
          2-factor authentication")
    exit(-1)

print('Signed in successfully')

LIBRARY = API.get_all_songs()
if not LIBRARY:
    print("Library is empty")
    exit(0)

HANDLER = LibraryHandler(LIBRARY)

HANDLER.update_lib_file(SETUP.get_out_file())

print("You've listened to music for", HANDLER.get_playing_time())

print("Genre statistic:")
GENRE_SONG_STAT, TOTAL_SONGS = HANDLER.get_genre_songs_statistic()
for genre in GENRE_SONG_STAT:
    play_count = GENRE_SONG_STAT[genre]
    # convert to int to get rid of frac part and then convert to string
    percentage = play_count/TOTAL_SONGS * 100
    percentage = f"{percentage:2.2}%"
    print(genre, play_count, percentage, sep='\t')
