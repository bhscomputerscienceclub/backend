from fastapi_sqlalchemy import db
from pydantic import BaseModel
from . import Base

from sqlalchemy import (
    Column,
    Integer,
    String,
    PickleType,
    DateTime,
    create_engine,
    ForeignKey,
    UniqueConstraint,
)


class TradeCreateReq(BaseModel):
    title: str


class TradeResp(BaseModel):
    num: int
    uid : int
    title : str

class Trade(Base):
    __tablename__ = "trades"
    uid = Column(Integer, primary_key=True)
    user_trade_num = Column(Integer, primary_key=True)
    title = Column(String)
    
    def resp(self) -> TradeResp:
        return TradeResp(
                num = self.user_trade_num,
                uid = self.uid,
                title = self.title
                )

    def dict(self):
        return {
            "uid": uid,
            "trade_number": user_trade_num,
            "title": title,
        }
