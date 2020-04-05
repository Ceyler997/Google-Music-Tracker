'''Class holder'''
import configparser
import logging
from os import path


class AppSetup:
    '''Class for setup the tracker'''

    def __init__(self, setup_file_name):
        self.id_file_path = "Auth/id"
        self.out_dir_path = "Library/"

        parser = configparser.ConfigParser()

        if parser.read(setup_file_name):
            # Setup account data
            try:
                self.id_file_path = parser['Login']['id file']
            except KeyError:
                logging.warning("ID file path is missing, default path will be used instead")

            # Setup output file
            try:
                self.out_dir_path = parser['Output']['file path']
            except KeyError:
                logging.error("Out file path is missing, default path will be used instead")
        else:
            logging.warning("Can't open setup file %s, default setup will be used", setup_file_name)

        #todo: make sure that directories exists

        self.valid = True

    def __bool__(self):
        return path.isfile(self.id_file_path) and path.getsize(self.id_file_path) > 0
