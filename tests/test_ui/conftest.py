import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



@pytest.fixture(scope="class")
def test_setup():
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.maximize_window()
    chrome.get("http://0.0.0.0:5000/")
    yield chrome
    chrome.get("http://google.com")
    time.sleep(10)


@pytest.fixture(scope="function")
def test_begin():
    with open("./balabalaba.txt", "a") as fp:
        fp.write("strochka lubaya {}\n".format(time.time()))
