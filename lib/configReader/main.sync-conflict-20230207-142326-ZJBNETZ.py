#inicaialize config file
def getConfig():
    config = configparser.ConfigParser()
    config.read('../config')
    return config
