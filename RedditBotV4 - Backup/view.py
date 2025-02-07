import time

import praw


#View in Model View Controller
class View:

  def __init__(self, reddit_bot):
    self.reddit_bot = reddit_bot

  def get_unread_mention(self):
    """Returns oldest unread message and marks it as read"""

    subreddit = self.reddit_bot.subreddit('testingground4bots')

    for comment in subreddit.stream.comments(skip_existing=True):  # stream to continuously get new comments
      if "!top10chessplayers" in comment.body.lower():
        return comment
      time.sleep(5)
    return None


    #unread_messages = list(self.reddit_bot.inbox.unread())  # Get all unread messages
    #unread_count = len(unread_messages)  # Count the number of unread messages
    #print(f"You have {unread_count} unread messages.")

    # for message in self.reddit_bot.inbox.unread():
    #   time.sleep(3)
    #   print("New unread inbox message")
    #   message.mark_read()
    #
    #   if "u/AngryLobotomy377" in message.body:
    #     print("Bot has been tagged.")
    #
    #     return message

    #for mention in self.reddit_bot.inbox.mentions(limit=25):
    #  return mention

    # subreddit = self.reddit_bot.subreddit('testingground4bots')
    #
    # for comment in subreddit.stream.comments(skip_existing=True):  # stream to continuously get new comments
    #   if "!chessplayers" in comment.body:
    #     return comment
    # return None


  def reply(self, original_message, reply_message):
    original_message.reply(reply_message)
