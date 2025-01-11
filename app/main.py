from fastapi import FastAPI
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from fastapi.responses import JSONResponse

app = FastAPI()

def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Usar ChromeDriverManager para obtener el path del driver automáticamente
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    return driver

@app.get('/data')
def home():
    try:
        print("Iniciando Selenium...")
        driver = download_selenium()
        print("Selenium iniciado.")
        driver.get("https://google.com")
        print(f"Título de la página: {driver.title}")
        title = driver.title
        data = {"some_text": title}
        driver.quit()  # Cerrar el WebDriver después de su uso
        print("Selenium cerrado correctamente.")
        return data
    except Exception as e:
        print(f"Error en la ruta /data: {e}")
        return {"error": str(e)}

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
