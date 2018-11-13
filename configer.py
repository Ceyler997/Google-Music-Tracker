'''Class holder'''
import configparser


class AppSetup:
    '''Class for setup the tracker'''

    valid = False
    login = ''
    password = ''

    out_file_path = 'Library/lib.json'

    def __init__(self, setup_file_name):
        parser = configparser.ConfigParser()

        if not parser.read(setup_file_name):
            print("Can't open setup file", setup_file_name)
            return

        # Setup account data
        try:
            self.login = parser['Account data']['login']
            self.password = parser['Account data']['password']
        except KeyError as error:
            print("Can't setup the app", error)

        self.valid = True

        # Setup output file
        try:
            self.out_file_path = parser['Output']['file path']
        except KeyError:
            pass

    def __bool__(self):
        return self.valid

    def get_login_info(self):
        '''Returns [login, password] pair, if is valid, None otherwise'''
        if self.valid:
            return self.login, self.password
        return None

    def get_out_file(self):
        '''Returns path to the output file default or from config, if there is'''
        return self.out_file_path
