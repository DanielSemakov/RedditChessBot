from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship

Base = declarative_base()

class TitledChessPlayer(Base):
  __tablename__ = "titled_chess_players"

  id = Column("id", Integer, primary_key=True, autoincrement = True)
  first_name = Column("first_name", String)
  middle_name = Column("middle_name", String)
  last_name = Column("last_name", String)
  rating = Column("rating", Integer)
  titled_flag = Column("titled_flag", Boolean)
  past_player_flag = Column("past_player_flag", Boolean)
  influencer_flag = Column("influencer_flag", Boolean)

  def __init__(self, id, first_name, middle_name, last_name, rating, *, titled_flag = False,
               past_player_flag = False, influencer_flag = False):
    self.id = id
    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.rating = rating
    self.titled_flag = titled_flag
    self.past_player_flag = past_player_flag
    self.influencer_flag = influencer_flag

  def __repr__(self):
    return (f"{self.id} {self.first_name} {self.middle_name} {self.last_name} {self.rating} "
            f"{self.titled_flag} {self.past_player_flag} {self.influencer_flag}")


class Nickname(Base):
  __tablename__ = "nicknames"

  nickname = Column("nickname", String, ForeignKey(TitledChessPlayer.id), primary_key = True)
  player_id = Column("player_id", Integer)

  def __init__(self, nickname, player_id):
      self.nickname = nickname
      self.player_id = player_id

  def __repr__(self):
      return (f"{self.nickname} {self.player_id}")



  