from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException


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
    try:
        driver = get_driver()
        driver.get("https://google.com")
        title = driver.title
        return {"title": title}
    except WebDriverException as e:
        # Manejo de errores específicos de Selenium
        return {"error": f"Error al usar el WebDriver: {str(e)}"}
    except Exception as e:
        # Manejo de errores genéricos
        return {"error": f"Error inesperado: {str(e)}"}
    finally:
        # Asegurarse de cerrar el driver si fue inicializado
        try:
            driver.quit()
        except NameError:
            pass

@app.get("/")
async def read_root():
    return {"message": "Hello, Render!"}