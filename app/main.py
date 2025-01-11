from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI()

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

@app.get("/scrape")
async def scrape_google():
    driver = get_driver()
    driver.get("https://google.com")
    title = driver.title
    driver.quit()
    return {"title": title}
