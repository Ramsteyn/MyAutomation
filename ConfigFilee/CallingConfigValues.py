from configparser import ConfigParser
# Create object of ConfigParser class
obj=ConfigParser()
# reading values in the config file
obj.read("../ConfigFilee/Config.cfg")
print(obj.get("MyConfig3","userName"))