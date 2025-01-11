from fastapi import FastAPI, Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from fastapi.responses import JSONResponse

app = FastAPI()

def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

@app.get('/data')
def home():
    driver = download_selenium()
    driver.get("https://google.com")
    title = driver.title
    data = {"some_text": title}
    driver.quit()  # Cerrar el WebDriver después de su uso
    return data

@app.get("/")
async def read_root():
    return {"message": "Hello, Render!"}

@app.post("/items/")
async def create_item(name: str):
    return {"name": name, "status": "Item created"}


@app.on_event("startup")
def startup_event():
    print("Starting up FastAPI application")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)