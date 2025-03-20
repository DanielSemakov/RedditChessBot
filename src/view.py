import time

class View:
  """The View in the Model, View, Controller architecture, representing the Reddit Bot."""

  def __init__(self, reddit_bot):
    self.reddit_bot = reddit_bot

  def get_unread_mention(self):
    """Returns oldest unread message and marks it as read"""

    subreddit = self.reddit_bot.subreddit('chess')

    for comment in subreddit.stream.comments(skip_existing=True):
      if "!top10mentions" in comment.body.lower():
        return comment
      time.sleep(5)
    return None

  def reply(self, original_message, reply_message):
    original_message.reply(reply_message)
