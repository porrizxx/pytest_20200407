import os

BROWSER_NAME = 'CHROME'

# local path
LOCAL_PATH = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

# 浏览器驱动
CHROME_DRIVER_PATH = LOCAL_PATH + '/tools/chromedriver.exe'

LOG_PATH = LOCAL_PATH + '/logs/'

DOWNLOAD_FILE_DIRECTORY = LOCAL_PATH + '/download'
