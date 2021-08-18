import configparser
def readConfig(section,Key):
    config= configparser.ConfigParser()
    config.read("../ConfigFiles/Config.cfg")
    return (config.get(section,Key))

def fetchElement(section, Key):
    config= configparser.ConfigParser()
    config.read("../ConfigFiles/Elements.cfg")
    return (config.get(section,Key))

