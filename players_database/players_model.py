#Model in Model View Controller
from sqlalchemy import text
from players_database.connection_manager import engine
from players_database.connection_manager import SessionManager
from players_database.db_tables import TitledChessPlayer


#Maybe rename the class to PlayersManager/PlayerManager
#Maybe have a separate module/class for querying the nicknames table.



class PlayersModel(SessionManager):
  
  def get_first_last_names(self):
    sql_query = text("SELECT CONCAT(first_name, ' ', last_name) FROM titled_chess_players")

    print(type(sql_query))

    with engine.connect() as connection:
      result = connection.execute(sql_query)

      #Convert CursorResult to
      return [i[0] for i in result.fetchall()]

  def get_names_ratings(self):
    """Returns a list of tuples containing name and rating info of all players. Each tuple
    has the following format: (first_name, middle_name, last_name, rating)"""
    return self.session.query(TitledChessPlayer.first_name, TitledChessPlayer.middle_name, TitledChessPlayer.last_name, TitledChessPlayer.rating).all()

