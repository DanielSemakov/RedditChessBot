from src.player_mention_processor import PlayerMentionProcessor

def test_process_comments_when_no_players(mocker):
    """Inputting an empty list of chess players should return an empty dictionary."""
    #Arrange
    mock_comment1 = mocker.MagicMock()
    mock_comment2 = mocker.MagicMock()
    mock_comment3 = mocker.MagicMock()

    mock_comment1.body = "I love Fabiano Caruana! He's my favorite. Same with Vladimir Kramnik."
    mock_comment2.body = "Wow, VLADimir kramNICK is a legendary player"
    mock_comment3.body = "Great play from MagnUS CARlsEn today."

    comments = [mock_comment1, mock_comment2, mock_comment3]

    players = []
    processor = PlayerMentionProcessor(players)

    #Act
    player_mentions = processor.process_comments(comments)

    #Assert
    assert player_mentions == {}

def test_process_comments_when_no_comments():
    """Inputting a collection with no comments should return a dictionary with all players
    as keys and all values equal to 0."""
    #Arrange
    players = ["Magnus Carlsen", "Anish Giri", "Wesley So"]
    comments = []

    processor = PlayerMentionProcessor(players)

    #Act
    player_mentions = processor.process_comments(comments)

    #Assert
    assert player_mentions == {"Magnus Carlsen": 0, "Anish Giri": 0, "Wesley So": 0}

def test_process_comments_when_multiple_players_and_comments(mocker):
    """Inputting 2+ players and 2+ comments should return a dictionary with all players
    as keys and values reflecting the number of mentions."""
    #Arrange
    players = ["Max Warmerdam", "Gukesh D", "Hikaru Nakamura", "Alexandra Botez"]

    mock_comment1 = mocker.MagicMock()
    mock_comment2 = mocker.MagicMock()
    mock_comment3 = mocker.MagicMock()
    mock_comment4 = mocker.MagicMock()

    mock_comment1.body = "I love Hikaru Nakamura! He's my favorite. Same with Gukesh D."
    mock_comment2.body = "Wow,Gukesh D is a legendary player. I love Gukesh D."
    mock_comment3.body = "Great play from Max Warmerdam today. Good job to MaX warMERdam."
    mock_comment4.body = "I don't like any of the players..."

    comments = [mock_comment1, mock_comment2, mock_comment3, mock_comment4]

    processor = PlayerMentionProcessor(players)

    #Act
    player_mentions = processor.process_comments(comments)

    #Assert
    assert player_mentions == {"Max Warmerdam": 2, "Gukesh D": 3, "Hikaru Nakamura": 1,
                               "Alexandra Botez": 0}

def test_process_submissions_when_no_players(mocker):
    """Inputting an empty list of chess players should return an empty dictionary."""
    # Arrange
    mock_submission = mocker.MagicMock()

    mock_submission.title = "I love Fabiano CARUANA! He's my favorite. Same with Vladimir Kramnik."
    mock_submission.selftext = "Wow, VLADimir kramNICK is a legendary player"

    submissions = [mock_submission]

    players = []
    processor = PlayerMentionProcessor(players)

    # Act
    player_mentions = processor.process_submissions(submissions)

    # Assert
    assert player_mentions == {}

def test_process_submissions_when_no_submissions(mocker):
    """Inputting a list with no submissions should return a dictionary with all players
    as keys and all values equal to 0."""
    # Arrange
    submissions = []

    players = ["Magnus Carlsen", "Anish Giri", "Wesley So"]
    processor = PlayerMentionProcessor(players)

    # Act
    player_mentions = processor.process_submissions(submissions)

    # Assert
    assert player_mentions == {"Magnus Carlsen": 0, "Anish Giri": 0, "Wesley So": 0}

def test_process_submissions_when_no_mentions_anywhere(mocker):
    """Inputting a list of submissions without full name mentions should return a
     dictionary of all players as keys and all values equal to 0. Submissions contain
     incomplete fragments of names."""
    #Arrange
    mock_submission1 = mocker.MagicMock()
    mock_submission2 = mocker.MagicMock()

    mock_submission1.title = "I don't like any of the players, like Wesley S"
    mock_submission1.selftext = "God, chess is so boring. I hate Anish Gir"
    mock_submission2.title = "Gosh, Magnus Carlos sucks."
    mock_submission2.selftext = "Not a fan of Magnus nor Anish"

    submissions = [mock_submission1, mock_submission2]

    players = ["Magnus Carlsen", "Anish Giri", "Wesley So"]
    processor = PlayerMentionProcessor(players)

    # Act
    player_mentions = processor.process_submissions(submissions)

    # Assert
    assert player_mentions == {"Magnus Carlsen": 0, "Anish Giri": 0, "Wesley So": 0}


def test_process_submissions_when_mentions_only_in_title(mocker):
    """Inputting a list of submissions with full name mentions only in the titles should return a
     dictionary of all players as keys and values indicating the number of mentions."""
    # Arrange
    mock_submission1 = mocker.MagicMock()
    mock_submission2 = mocker.MagicMock()

    mock_submission1.title = "I love Wesley So, WESLEY so! Magnus carlSEN is ok."
    mock_submission1.selftext = "God, chess is so boring. I hate Anish Gir"
    mock_submission2.title = "!WeslEy SO is so great!"
    mock_submission2.selftext = "Not a fan of Magnus nor Anish"

    submissions = [mock_submission1, mock_submission2]

    players = ["Magnus Carlsen", "Anish Giri", "Wesley So"]
    processor = PlayerMentionProcessor(players)

    # Act
    player_mentions = processor.process_submissions(submissions)

    # Assert
    assert player_mentions == {"Magnus Carlsen": 1, "Anish Giri": 0, "Wesley So": 3}

def test_process_submissions_when_mentions_only_in_selftext(mocker):
    """Inputting a list of submissions with full name mentions only in the selftext should return a
         dictionary of all players as keys and values indicating the number of mentions."""
    # Arrange
    mock_submission1 = mocker.MagicMock()
    mock_submission2 = mocker.MagicMock()

    mock_submission1.title = "God, chess is so boring. I hate Anish Gir"
    mock_submission1.selftext = "I love Wesley So, WESLEY so! Magnus carlSEN is ok."
    mock_submission2.title = "Not a fan of Magnus nor Anish"
    mock_submission2.selftext = "!WeslEy SO is so great!"

    submissions = [mock_submission1, mock_submission2]

    players = ["Magnus Carlsen", "Anish Giri", "Wesley So"]
    processor = PlayerMentionProcessor(players)

    # Act
    player_mentions = processor.process_submissions(submissions)

    # Assert
    assert player_mentions == {"Magnus Carlsen": 1, "Anish Giri": 0, "Wesley So": 3}

def test_process_submissions_when_mentions_in_title_and_selftext(mocker):
    """Inputting a list of submissions with full name mentions in titles and selftexts should
    return a dictionary of all players as keys and values indicating the number of mentions."""
    # Arrange
    mock_submission1 = mocker.MagicMock()
    mock_submission2 = mocker.MagicMock()

    mock_submission1.title = "Big ,Alexandra boTEZ fan!!!"
    mock_submission1.selftext = "I love Wesley So, WESLEY so! Magnus carlSEN is ok."
    mock_submission2.title = "...WESLey SOOOO!"
    mock_submission2.selftext = "!WeslEy SO is so great! Alexandra botez is okay"

    submissions = [mock_submission1, mock_submission2]

    players = ["Magnus Carlsen", "Anish Giri", "Wesley So", "Alexandra Botez"]
    processor = PlayerMentionProcessor(players)

    # Act
    player_mentions = processor.process_submissions(submissions)

    # Assert
    assert player_mentions == {"Magnus Carlsen": 1, "Anish Giri": 0, "Wesley So": 4,
                               "Alexandra Botez": 2}

