from src import dict_tools
from src.player_mention_processor import PlayerMentionProcessor
from src.players_database import connection_manager


class Controller:
  """The Controller in the Model, View Controller architecture. This class contains
  business code and manages interactions between the Model and the View."""

  def __init__(self, model, view):
    self.model = model
    self.view = view

  def get_unread_mention(self):
    return self.view.get_unread_mention()

  def get_player_mentions(self, redditor):
    """
    Returns dictionary of all chess players the redditor has ever mentioned in comments 
    and submissions and how many times those players have been mentioned.
    """
    comments = redditor.get_comments()
    submissions = redditor.get_submissions()

    player_names = self.model.get_first_last_names()

    mention_processor = PlayerMentionProcessor(player_names)
    cmnt_mentions = mention_processor.process_comments(comments)
    sub_mentions = mention_processor.process_submissions(submissions)

    return dict_tools.combine_and_sum_dicts([cmnt_mentions, sub_mentions])


  def reply_to_msg(self, original_message, player_mentions):
    """Replies to original comment with list of top 10 most mentioned chess players and
    how many times the commenter has mentioned each of them"""

    # Dictionaries, such as player_mentions, have an arbitrary order by default.
    # Here, I convert mentions_dict to a list of keys sorted in descending order based on the values
    # which accompanied those keys in the original dictionary.

    # Then I iterate through the list of keys to get their accompanying values. This whole process essentially
    # lets me order the player_mentions dictionary.

    # More info here:
    # https://stackoverflow.com/questions/20577840/python-dictionary-sorting-in-descending-order-based-on-values
    # https://docs.python.org/3/howto/sorting.html

    reply = f"{original_message.author}'s 10 most mentioned chess players:\n\n"

    players_sorted_by_mentions = sorted(player_mentions, key=player_mentions.get, reverse=True)

    index = 1
    for player_name in players_sorted_by_mentions:
      num_mentions = player_mentions[player_name]
      reply += f"{index}. {player_name} ({num_mentions} times)\n"

      if index >= 10:
        break

      index += 1

    print(reply)

    self.view.reply(original_message, reply)
