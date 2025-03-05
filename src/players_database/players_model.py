from sqlalchemy import text, func
from src.players_database.connection_manager import engine
from src.players_database.connection_manager import SessionManager
from src.players_database.db_tables import TitledChessPlayer

class PlayersModel(SessionManager):
  """The Model in the Model, View, Controller architecture, allowing the user
  to access info in the titled_chess_players table."""
  
  def get_first_last_names(self):
    """Returns a list of the first and last names of all players in the table."""
    query = self.session.query(
      func.concat(TitledChessPlayer.first_name, ' ', TitledChessPlayer.last_name)
    )

    result = query.all()

    return [name[0] for name in result]

  def get_names_ratings(self):
    """Returns a list of tuples containing name and rating info of all players. Each tuple
    has the following format: (first_name, middle_name, last_name, rating)"""
    return self.session.query(TitledChessPlayer.first_name, TitledChessPlayer.middle_name, TitledChessPlayer.last_name, TitledChessPlayer.rating).all()

