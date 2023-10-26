import pytest
from selenium import webdriver
driver = None


@pytest.fixture
def setup(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)
    request.cls.driver.get("https://app.localstack.cloud/sign-up")
    yield
    request.cls.driver.quit()
