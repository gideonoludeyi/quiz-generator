import os

from fastapi import FastAPI, Request, Response
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(debug=True)

templates = Jinja2Templates(directory='templates')

file_formats = dict(txt='Text', json='JSON')


@app.get('/', response_class=HTMLResponse)
def root(request: Request) -> Response:
    return templates.TemplateResponse('index.html.jinja2', dict(request=request, file_formats=file_formats))


@app.get('/download')
def download(filetype: str = 'txt') -> Response:
    path = f'assets/questions.{filetype}'
    if not os.path.isfile(path):
        raise HTTPException(400, detail='Unsupported filetype')
    return FileResponse(path)
