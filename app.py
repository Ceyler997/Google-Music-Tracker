from gmusicapi import Mobileclient
from time_acc import TimeAcc
import configparser

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
for song in library:
    acc.add(int(song['durationMillis']) * song['playCount'])

print('You listened to music for:')
print(acc)
