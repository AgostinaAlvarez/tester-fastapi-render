from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get-google-title")
async def get_google_title():
    # Configuración del WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Inicializar el WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://google.com")
        title = driver.title
        data = {"some_text": title}
    finally:
        driver.quit()  # Cerrar el WebDriver después de su uso

    return JSONResponse(content=data)



@app.get("/")
async def read_root():
    return {"message": "Hello, Render!"}