#Model in Model View Controller
from sqlalchemy import text
from players_database.connection_manager import engine
from players_database.connection_manager import SessionManager



#Maybe rename the class to PlayersManager/PlayerManager
#Maybe have a separate module/class for querying the nicknames table.
class PlayersModel(SessionManager):
  
  def get_full_names(self):
    sql_query = text("SELECT CONCAT(first_name, ' ', last_name) FROM chess_players")

    print(type(sql_query))

    with engine.connect() as connection:
      result = connection.execute(sql_query)

      #Convert CursorResult to
      return [i[0] for i in result.fetchall()]
