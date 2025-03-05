from src.controller import Controller
from src.players_database.players_model import PlayersModel
import pytest
import shutil
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.redditor_model import RedditorModel

ACTUAL_DB_PATH = '../src/players_database/mydb.db'
TEST_DB_PATH = 'players_database/mydb.db'

@pytest.fixture(scope="function")
def db_session():
    """Create a test database before each test and delete it after each test to avoid modifying
    the actual database. The test database is an exact copy of the actual database."""

    #Copy the actual database to the test database path
    shutil.copy(ACTUAL_DB_PATH, TEST_DB_PATH)

    engine = create_engine(f"sqlite:///{TEST_DB_PATH}")

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    #Clean up: Close the session and remove the test database file
    session.close()
    engine.dispose() #Ensure engine connection is closed-- error occurs without this
    os.remove(TEST_DB_PATH)  #Delete the test database file after tests


def test_get_player_mentions_multiple_mentions_from_submissions_and_comments(mocker, db_session):
    """Integration test for typical use case of player_mentions. This also ends up testing
    the players_model and player_mention_processor modules. When passing in a redditor_model object
    that contains 2 comments and 2 submissions, get_player_mentions() should return a dictionary
    where the keys are the names of all chess players in the database and the values are the number
    of times those players are mentioned in the comments and submissions. Instances of 0, 1, and 2+
    mentions are tested.
    """
    #Arrange

    #Create test doubles for redditor.get_comments() and redditor.get_submissions() function
    #calls so that they return hard-coded values: 2 comments and 2 submissions with several
    #player mentions
    mock_comment1 = mocker.MagicMock()
    mock_comment2 = mocker.MagicMock()

    mock_comment1.body = "I love Fabiano Caruana! He's my favorite. Same with Anish gIRI."
    mock_comment2.body = "Wow, VLADimir kramNIK is a legendary player. Same with wesLEY SO!!!"

    comments = [mock_comment1, mock_comment2]

    mock_submission1 = mocker.MagicMock()
    mock_submission2 = mocker.MagicMock()

    mock_submission1.title = "God, chess is so boring. I hate Anish Giri"
    mock_submission1.selftext = "I love Wesley So, WESLEY so! Magnus carlSEN is ok."
    mock_submission2.title = "Not a fan of Magnus nor Anish. But I LOVE WESLEY so"
    mock_submission2.selftext = "!WeslEy SO is so great! "

    submissions = [mock_submission1, mock_submission2]

    mock_get_comments = mocker.patch("src.redditor_model.RedditorModel.get_comments")
    mock_get_submissions = mocker.patch("src.redditor_model.RedditorModel.get_submissions")

    mock_get_comments.return_value = comments
    mock_get_submissions.return_value = submissions

    #Create model and view dependencies. Using a real PlayersModel object since it's part
    #of the system under test.
    model = PlayersModel()

    #Override session connected to real database with session connected to test database
    model.session = db_session

    view = mocker.MagicMock()
    controller = Controller(model, view)

    #Pass in real redditor_model so that the get_comments and get_submissions calls are
    #recognized and overridden
    redditor = mocker.MagicMock()
    redditor_model = RedditorModel(redditor)

    #Act
    player_mentions = controller.get_player_mentions(redditor_model)

    #Assert
    assert player_mentions["Fabiano Caruana"] == 1
    assert player_mentions["Anish Giri"] == 2
    assert player_mentions["Vladimir Kramnik"] == 1
    assert player_mentions["Wesley So"] == 5
    assert player_mentions["Magnus Carlsen"] == 1
    assert player_mentions["Alexandra Botez"] == 0
    assert player_mentions["Hans Niemann"] == 0
    assert player_mentions["Ian Nepomniachtchi"] == 0





