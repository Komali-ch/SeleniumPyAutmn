# In python we have a package "configparser",need to import,inside config parser we have RawConfigParser
# needs to create an object for RawConfigParser class
# accessing read method from rawconfigparser to read data from ini file
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'webappUrl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
