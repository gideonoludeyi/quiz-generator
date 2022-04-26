import os

from fastapi import FastAPI, Request, Response, UploadFile, status
from fastapi.exceptions import HTTPException
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from quiz_generator.core.pool import QuestionPool
from quiz_generator.core.source import QuestionSource
from quiz_generator.generator import QuizGenerator

from app.text_file_source import TextFileQuestionSource
from app.unsupported_file_extension import UnsupportedFileExtension

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


@app.post('/generate')
def generate(file: UploadFile, filetype: str = 'txt', num_handouts: int = 1, num_questions_per_handout: int = 1):
    try:
        source = upload_file_to_source(file)
    except UnsupportedFileExtension as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Unsupported file extension: {e.extension}')

    pool = QuestionPool(source)
    generator = QuizGenerator(pool)
    handouts = generator.generate_handouts(
        num_handouts=num_handouts,
        num_questions_per_handout=num_questions_per_handout
    )
    return handouts


def upload_file_to_source(file: UploadFile) -> QuestionSource:
    *_, file_extension = os.path.splitext(file.filename)
    match file_extension:
        case '.txt' | '.text':
            return to_text_source(file)
        case _:
            raise UnsupportedFileExtension(extension=file_extension)


def to_text_source(file: UploadFile) -> TextFileQuestionSource:
    lines = (b.decode('utf-8').strip() for b in iter(file.file))
    return TextFileQuestionSource(lines)
