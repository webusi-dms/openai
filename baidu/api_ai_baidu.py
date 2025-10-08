import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

destUrl = "https://chat.baidu.com/search?extParams=%7B%22enter_type%22%3A%22chat_url%22%7D&isShowHello=1"

def getOneData(text):
    waitId = "new-page"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36')
    service = Service(executable_path='/usr/local/bin/chromedriver')

    browser = webdriver.Chrome(service=service, options=chrome_options)

    try:
        browser.get(destUrl)
        wait = WebDriverWait(browser, 100)
        wait.until(EC.presence_of_element_located((By.ID, waitId)))

        chatInput = browser.find_element(By.ID, "chat-textarea")
        chatInput.click()
        time.sleep(0.2)
        chatInput.clear()
        chatInput.send_keys(text)

        submitBtn = None
        try:
            submitBtn = browser.find_element(By.CLASS_NAME, "chat-submit-button-ai-active")
        except:
            submitBtn = None

        if submitBtn is None:
            submitBtn = browser.find_element(By.CLASS_NAME, "cos-icon-arrow-up")
        submitBtn.click()

        waitClass = 'cos-icon-exchange'
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, waitClass)))

        time.sleep(3)

        resultDiv = browser.find_element(By.CLASS_NAME, "marklang")

        return resultDiv.text

    finally:
        browser.close()

