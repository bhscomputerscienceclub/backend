from typing import Optional

from fastapi import FastAPI, File, UploadFile 
import multihash
import config
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/upload" )
async def create_upload_file(file: UploadFile = File(...)):
    # max length check TODO
    mh = multihash.decode(file.filename.encode(), 'hex')
    assert mh.func is multihash.Func.sha2_256 # tmp ensure sha256 decide on smth later
    if not mh.verify(await file.read()):
        return False
    #security checks TODO
    with open(config.DATA_DIR+"/"+mh.encode('hex').decode(), 'wb') as f:
        await file.seek(0)
        f.write(await file.read())
    return {"filename": file.filename}
