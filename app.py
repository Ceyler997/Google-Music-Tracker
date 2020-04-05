'''App for collecting statistig from Google Music'''
import sys
import logging
from gmusicapi import Musicmanager
from configer import AppSetup
from handler import LibHandler

logging.info('App start')

SETUP = AppSetup('config.ini')
API = Musicmanager()

if not SETUP:
    API.perform_oauth(SETUP.id_file_path, True)

LOGIN_RESULT = API.login(SETUP.id_file_path)

if not LOGIN_RESULT:
    logging.error("Login failed")
    sys.exit(-1)

logging.info('Signed in successfully')

UPLOADED_SONGS = API.get_uploaded_songs()
UPLOADED_HANDLER = LibHandler(UPLOADED_SONGS, SETUP.out_dir_path + 'uploaded')
UPLOADED_HANDLER.update_lib_file()

PURCHASED_SONGS = API.get_purchased_songs()
PURCHASED_HANDLER = LibHandler(PURCHASED_SONGS, SETUP.out_dir_path + 'purchased')
PURCHASED_HANDLER.update_lib_file()

API.logout()

# LIBRARY = API.get_all_songs()
# if not LIBRARY:
#     print("Library is empty")
#     sys.exit()

# HANDLER = LibraryHandler(LIBRARY)

# HANDLER.update_lib_file(SETUP.get_out_file())

# print("You've listened to music for", HANDLER.get_playing_time())

# print("Genre statistic:")
# GENRE_SONG_STAT, TOTAL_SONGS = HANDLER.get_genre_songs_statistic()
# for genre in GENRE_SONG_STAT:
#     play_count = GENRE_SONG_STAT[genre]
#     # convert to int to get rid of frac part and then convert to string
#     percentage = play_count/TOTAL_SONGS * 100
#     percentage = f"{percentage:2.2}%"
#     print(genre, play_count, percentage, sep='\t')
