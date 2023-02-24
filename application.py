import uvicorn
from googletrans import Translator

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

translator = Translator()

@app.post(path="/english_text")
async def extract_data_from_images(value=Form(...)):

    translation = translator.translate(value, dest='hi')

    return str(translation.text)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("application:app", log_level="info")