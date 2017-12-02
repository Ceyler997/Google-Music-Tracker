import configparser
from gmusicapi import Mobileclient
from time_acc import TimeAcc

print('Start')
parser = configparser.ConfigParser()

if not parser.read('config.ini'):
    print("Can't read 'config.ini' file")
    exit(-1)

if 'Account data' not in parser:
    print("Can't find 'Account data' section in config file")
    exit(-1)

login = 'login'
password = 'ps'
try:
    login = parser['Account data']['login']
    password = parser['Account data']['password']
except KeyError:
    print("There is no 'login' or 'password' options in config file")
    exit(-1)

api = Mobileclient()
login_result = api.login(login, password, Mobileclient.FROM_MAC_ADDRESS)

if not login_result:
    print("Can't sign you in. Please, use app specific password in case 2-factor authentication")
    exit(-1)

print('Signed in successfully')

library = api.get_all_songs()
acc = TimeAcc()
genreStatistic = dict();
genreStatistic['No genre'] = 0

for song in library:
    acc.add(int(song['durationMillis']) * song['playCount'])
    if 'genre' in song and song['genre'] is not '':
        if song['genre'] in genreStatistic:
            genreStatistic[song['genre']] += 1
        else:
            genreStatistic[song['genre']] = 1
    else:
        genreStatistic['No genre'] += 1

print('You listened to music for:')
print(acc)

sGenreStatistic = [(genre, genreStatistic[genre]) for genre in sorted(genreStatistic, key=genreStatistic.get, reverse=True)]

print('Genre statistic:')
total = len(library)/100
for genre, num in sGenreStatistic:
    print(genre, ': ', num, ' songs, ', "%0.2f" % (num/total), '% from total amount', sep='',)
print()