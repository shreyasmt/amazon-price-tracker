from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'PS4'
CURRENCY = '$'
MIN_PRICE = '275'
MAX_PRICE = '650'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = 'http://www.amazon.com.au/'

def get_chome_webdriver(options):
    return webdriver.Chrome('./chromedriver.exe',chrome_options=options)

def get_webdriver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')