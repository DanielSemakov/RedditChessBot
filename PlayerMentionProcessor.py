class PlayerMentionProcessor:

    def __init__(self, player_names):
        self.player_names = player_names

    def process_comments(self, comments):
        player_mentions = dict.fromkeys(self.player_names, 0)

        for comment in comments:
            for player_name in self.player_names:
                player_mentions[player_name] += comment.body.lower().count(player_name.lower())

        return player_mentions

    def process_submissions(self, submissions):
        player_mentions = dict.fromkeys(self.player_names, 0)

        for submission in submissions:
            for player_name in self.player_names:
                player_mentions[player_name] += submission.title.lower().count(player_name.lower())
                player_mentions[player_name] += submission.selftext.lower().count(player_name.lower())

        return player_mentions
