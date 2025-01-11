from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

app = FastAPI()

# Variable global para el driver
driver = None

# Inicializar el driver al inicio de la aplicación

def init_chrome():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Especifica la ruta de Chromium, si se encuentra en un directorio específico
    options.binary_location = '/usr/bin/chromium'  # Ajusta según el entorno

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

@app.on_event("startup")
async def startup_event():
    global driver
    driver = init_chrome()


@app.on_event("shutdown")
async def shutdown_event():
    global driver
    if driver:
        driver.quit()


# Función principal para recopilar datos
def get_data():
    global driver
    driver.get("https://hypeauditor.com/top-instagram-health-medicine-united-states/")

    try:
        table = driver.find_element(By.CLASS_NAME, "table")
        rows = table.find_elements(By.CLASS_NAME, "row")
        data_list = []

        for row in rows[1:]:  # Ignora la cabecera
            data_row = row.find_element(By.CLASS_NAME, "row__top")
            contributor = data_row.find_element(By.CLASS_NAME, "contributor")
            contributor__name = contributor.find_element(By.CLASS_NAME, "contributor__name-content")
            contributor__title = contributor.find_element(By.CLASS_NAME, "contributor__title")
            subscribers = data_row.find_element(By.CLASS_NAME, "subscribers")
            authentic_engagement = data_row.find_element(By.CLASS_NAME, "authentic")
            average_engagement = data_row.find_element(By.CLASS_NAME, "engagement")

            categories_data = []
            category_container = data_row.find_element(By.CLASS_NAME, "category")
            categories = category_container.find_elements(By.CLASS_NAME, "tag__content")
            audience_country = data_row.find_element(By.CLASS_NAME, "audience")

            for category in categories:
                categories_data.append(category.text)

            data = {
                'username': contributor__name.text,
                'contributor__title': contributor__title.text,
                'subscribers': subscribers.text,
                'engagement_authentic': authentic_engagement.text,
                'average_engagement': average_engagement.text,
                'audience_country': audience_country.text,
                'categories_data': categories_data,
            }
            data_list.append(data)

        return data_list
    except Exception as e:
        print(f"Error al extraer datos: {e}")
        return {"error": "No se pudieron obtener los datos"}


# Ruta para obtener los datos
@app.get("/users")
async def get_users():
    data = get_data()
    return {"users": data}

@app.get("/")
async def read_root():
    return {"message": "Hello, Render!"}

@app.post("/items/")
async def create_item(name: str):
    return {"name": name, "status": "Item created"}
