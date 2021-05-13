import requests
import warnings
warnings.filterwarnings('ignore')
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import re
import numpy as np
from datetime import datetime
from datetime import timedelta
# import datefinder
from re import sub
from decimal import Decimal
from collections import defaultdict
from lxml import etree
import lxml.html
from pprint import pprint
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



pd.set_option("display.max_rows", None, "display.max_columns", None)

# headers = requests.utils.default_headers()
# headers.update({
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
# })

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_partnum():
    url = 'https://www.arrow.com/en/categories/power-management/regulators-and-controllers/linear-regulators?page=1'
    # driver = webdriver.PhantomJS(("C://phantomjs.exe"))

    # options = Options()
    # options.headless = True
    # driver = webdriver.Chrome("chromedriver.exe",chrome_options=options)
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(url)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_partnum()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
