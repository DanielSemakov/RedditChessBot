import praw
from src.players_database.db_initializer import DbInitializer
from src.view import View
from src.players_database.players_model import PlayersModel
from src.redditor_model import RedditorModel
from src.controller import Controller
from dotenv import load_dotenv
import os

def main():
    db_initializer = DbInitializer()

    view = create_redditor_bot()
    players_model = PlayersModel()
    controller = Controller(players_model, view)

    while True:
        og_message = controller.get_unread_mention()

        if og_message is not None:
            redditor_model = RedditorModel(og_message.author)

            player_mentions = controller.get_player_mentions(redditor_model)
            controller.reply_to_msg(og_message, player_mentions)


def create_redditor_bot():
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

    username = os.getenv("REDDIT_USERNAME")
    password = os.getenv("REDDIT_PASSWORD")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    #Allows you to connect to Reddit via the account
    reddit_bot = praw.Reddit(
        username = username,
        password = password,
        client_id = client_id,
        client_secret = client_secret,
        user_agent = "reddit_bot"
    )

    return View(reddit_bot)

if __name__ == "__main__":
  main()

