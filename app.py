'''App for collecting statistig from Google Music'''
import configparser
from gmusicapi import Mobileclient
from time_acc import TimeAcc

print('Start')
PARSER = configparser.ConfigParser()

if not PARSER.read('config.ini'):
    print("Can't read 'config.ini' file")
    exit(-1)

if 'Account data' not in PARSER:
    print("Can't find 'Account data' section in config file")
    exit(-1)

LOGIN = 'login'
PASSWORD = 'ps'
try:
    LOGIN = PARSER['Account data']['login']
    PASSWORD = PARSER['Account data']['password']
except KeyError:
    print("There is no 'login' or 'password' options in config file")
    exit(-1)

API = Mobileclient()
LOGIN_RESULT = API.login(LOGIN, PASSWORD, Mobileclient.FROM_MAC_ADDRESS)

if not LOGIN_RESULT:
    print("Can't sign you in. Please, use app specific password in case \
          2-factor authentication")
    exit(-1)

print('Signed in successfully')

LIBRARY = API.get_all_songs()

ACC = TimeAcc()
GENRE_STATISTIC = dict()
GENRE_STATISTIC['No genre'] = 0

for song in LIBRARY:
    if 'playCount' in song:
        ACC.add(int(song['durationMillis']) * song['playCount'])
    if 'genre' in song and song['genre']:
        if song['genre'] in GENRE_STATISTIC:
            GENRE_STATISTIC[song['genre']] += 1
        else:
            GENRE_STATISTIC[song['genre']] = 1
    else:
        GENRE_STATISTIC['No genre'] += 1

print('You listened to music for:')
print(ACC)
SORTED_GENRES = sorted(GENRE_STATISTIC, key=GENRE_STATISTIC.get,
                       reverse=True)

SORTED_GENRES = [(genre, GENRE_STATISTIC[genre]) for genre
                 in SORTED_GENRES]

print('Genre statistic:')
TOTAL = len(LIBRARY)/100
for genre, num in SORTED_GENRES:
    print(genre, ': ', num, ' songs, ', "%0.2f" % (num/TOTAL), '% from total \
    amount', sep='',)

print()
