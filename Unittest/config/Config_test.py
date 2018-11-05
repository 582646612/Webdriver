import os
import ConfigParser
dir = os.path.dirname(os.path.abspath('.'))
config = ConfigParser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
config.read(file_path)
browser = config.get("browserType", "browserName")
url = config.get("testServer", "URL")
print browser
print url