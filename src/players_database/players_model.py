from sqlalchemy import text
from src.players_database.connection_manager import engine
from src.players_database.connection_manager import SessionManager
from src.players_database.db_tables import TitledChessPlayer

class PlayersModel(SessionManager):
  """The Model in the Model, View, Controller architecture, allowing the user
  to access info in the titled_chess_players table."""
  
  def get_first_last_names(self):
    """Returns a list of the first and last names of all players in the table."""
    sql_query = text("SELECT CONCAT(first_name, ' ', last_name) FROM titled_chess_players")

    with engine.connect() as connection:
      result = connection.execute(sql_query)

      #Convert CursorResult to
      return [i[0] for i in result.fetchall()]

  def get_names_ratings(self):
    """Returns a list of tuples containing name and rating info of all players. Each tuple
    has the following format: (first_name, middle_name, last_name, rating)"""
    return self.session.query(TitledChessPlayer.first_name, TitledChessPlayer.middle_name, TitledChessPlayer.last_name, TitledChessPlayer.rating).all()

