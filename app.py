from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

app = Flask(__name__)

def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        driver = download_selenium()
        driver.get("https://google.com")
        title = driver.title
        data = {"some_text": title}
        driver.quit()  # Cerrar el WebDriver después de su uso
        return data

if __name__ == "__main__":
	app.run(debug=True, port=3000)