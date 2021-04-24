from fastapi import FastAPI,File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Any, Dict, AnyStr, List, Union
import uvicorn,os
import aiofiles


app=FastAPI(title="FileUpload")

@app.get("/")
async def main():
    content = """<html> <title>Teste UpLoad</title> <body> Teste UpLoad </body> </html> """
    return HTMLResponse(content=content)


@app.post("/sizefile/")
async def sizefile(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_uploadfiles(files: List[UploadFile] = File(...)):
    path='uploads/'
    if not os.path.isdir(path):
        os.mkdir(path)
        print('create',os.getcwd())
    for k in files:
        async with aiofiles.open(path+k.filename, 'wb') as out_file:
            while content := await k.read(1024):
                await out_file.write(content)
    return {"filenames": [file.filename for file in files]}


@app.post("/uploadfile")
async def create_uploadfile(input_data: UploadFile = File(...)):
    path='upload/'
    if not os.path.isdir(path):
        os.mkdir(path)
        print('create',os.getcwd())
    async with aiofiles.open(path+input_data.filename, 'wb') as out_file:
        while content := await input_data.read(1024):
            await out_file.write(content)
    return {"filename": input_data.filename}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
