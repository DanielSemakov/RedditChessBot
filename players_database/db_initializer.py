#Deals with creating the initial tables in the database and inserting values into
#those tables
from players_database import db_tables
from players_database.connection_manager import SessionManager
from players_database.connection_manager import engine

import xml.etree.ElementTree as ET

from sqlalchemy import create_engine, inspect

from players_database.db_tables import ChessPlayer


#Maybe have separate classes to initialize chess_players DB and nicknames DB
class DbInitializer(SessionManager):

  def __init__(self):
    super().__init__()
    self.create_tables()
    self.insert_titled_players()

  #Maybe unnecessary to have this in a function
  def create_tables(self):
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()

    if 'chess_players' not in existing_tables:  # Example table name
      db_tables.Base.metadata.create_all(bind=engine)

  def insert_titled_players(self):
    """
    Scan XML file of FIDE players, find all titled players, and add their info to the
    chess_players table. Assumptions are made to separate between a player's first,
    middle, and last name. If the table already contains player names, the function
    terminates.
    """
    num_players_in_db = self.session.query(ChessPlayer).count()
    if num_players_in_db > 0:
      return

    tree = ET.parse("players_database/fide_players_list.xml")
    root = tree.getroot()

    player_id = 0

    titled_players = []

    for player in root:
      if player.findall("title")[0].text != None:

        first_name = None
        middle_name = None
        last_name = None

        #If full name in XML file has no commas, I presume this name format: [fname] [mname] [lname]
        #where the middle and last name are optional. This is a very inexact heuristic that doesn't take into account
        #the differences between naming conventions in different cultures, but it's an easy way to work with names.
        full_name = player.findall("name")[0].text

        if "," not in full_name:
          full_name_delimited = full_name.split()
          first_name = full_name_delimited[0]

          if len(full_name_delimited) == 2:
            last_name = full_name_delimited[1]
          elif len(full_name_delimited) > 2:
            last_name = full_name_delimited[len(full_name_delimited) - 1]

            #I assume the middle name is made up of all names between the first and last name
            full_name_delimited.pop(0)
            full_name_delimited.pop(len(full_name_delimited) - 1)

            middle_name = " ".join(full_name_delimited)

        #If full name in XML file has commas, I presume this name format: [lname], [fname] [mname]
        #(where any one of these names is optional) with some exceptions due to probably
        #erroneous formatting, including:
        #[lname], , [fname] [mname]
        #[lname], [fname] [mname],
        #[lname],[fname] [mname]
        else:
          # If full name has at least one comma but does not end in a comma
          # I assume all the names before the first comma make up the last name
          # e.g. with "Abreu Mijares, Elias Eduardo," I assume "Abreu Mijares" is the last name
          names_delimited_comma = full_name.split(',')

          # Deals with situations such as this: "[last name] , [first name]"
          # with unnecessary space after (and possibly before) last name
          last_name = names_delimited_comma[0].rstrip().lstrip()

          # Deals with situation (probably a format error) where full name in
          # XML file ends with a comma
          # E.g. "Harutyunyan, Narek A,"
          if full_name[len(full_name) - 1] == ",":
            names_delimited_comma.pop(len(names_delimited_comma) - 1)

          if len(names_delimited_comma) > 1:
            # Get first name. I assume the first name after the comma is the "first name."
            # E.g. with "Abreu Mijares, Elias Eduardo," I assume the first name is "Elias"

            # If there's no names following the comma, the first and middle names are None by default.
            # If there are any names following the comma, I assume the first name after the comma is
            # the "first name."
            # E.g. with "Abreu Mijares, Elias Eduardo," I assume the first name is "Elias"

            # Deals with format errors such as this: [last name], , [first name]
            # E.g. "Petrov, , Ivailo g"
            last_comma_delimited_str = names_delimited_comma[
                len(names_delimited_comma) - 1].lstrip()
            first_name = last_comma_delimited_str.split()[0]

            # If there exists more than one name after the comma, I assume all the names after the
            # first name make up the middle name.
            # E.g. with "Abreu Mijares, Elias Eduardo," I assume the middle name is "Eduardo"
            # E.g. with "A Aziz, Mohd Azizi Jamil," I assume the middle name is "Azizi Jamil"
            possible_middle_names = last_comma_delimited_str.split()
            possible_middle_names.pop(0)

            if len(possible_middle_names) > 0:
              middle_name = " ".join(possible_middle_names)

        player = db_tables.ChessPlayer(player_id,
                             first_name,
                             middle_name,
                             last_name,
                             titled_flag=True)
        titled_players.append(player)

        player_id += 1

    self.session.bulk_save_objects(titled_players)
    self.session.commit()

  def insert_influencer_players(self):
    pass

  def insert_historical_players(self):
    pass
