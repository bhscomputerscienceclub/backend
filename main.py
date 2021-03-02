from typing import Optional, List

from fastapi import FastAPI, File, UploadFile
from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from fastapi_sqlalchemy import (
    db,
)  # an object to provide global access to a database session
from db import (
    Session,)
from db.trade import (
    Trade,
    TradeResp,
    TradeCreateReq,
)
import multihash
import time
import config

app = FastAPI()


@app.get("/users/{user_id}/trades", response_model=List[TradeResp])
def read_root(user_id: int):
    session = Session()
    ans = session.query(Trade).filter(Trade.uid == user_id).all()
    session.close()
    return [s.resp() for s in ans]


@app.post("/users/{user_id}/trades", response_model=TradeResp)
def read_item(trade: TradeCreateReq, user_id: int):
    t = int(time.time() * 1000)
    trade = Trade(title=trade.title, uid=user_id, user_trade_num=t)
    session = Session()
    session.add(trade)
    session.commit()
    session.close()
    return trade.resp() 


@app.post("/upload")
async def create_upload_file(file: UploadFile = File(...)):
    # max length check TODO
    mh = multihash.decode(file.filename.encode(), "hex")
    assert mh.func is multihash.Func.sha2_256  # tmp ensure sha256 decide on smth later
    if not mh.verify(await file.read()):
        return False
    # security checks TODO
    with open(config.DATA_DIR + "/" + mh.encode("hex").decode(), "wb") as f:
        await file.seek(0)
        f.write(await file.read())
    return {"filename": file.filename}
