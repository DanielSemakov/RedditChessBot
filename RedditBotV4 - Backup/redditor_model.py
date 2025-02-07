#Maybe I should instead get the redditor's comments and posts via
#the View class. Aren't the comments/posts more like the UI than
#the DB?

#I think I've decided to keep this class separate. View interacts specifically
# with my Reddit bot account (inbox and replying). RedditorModel interacts with any
# Reddit account (view comments and submissions)

class RedditorModel: 
  
  def __init__(self, redditor):
    self.redditor = redditor

  def get_comments(self):
    return self.redditor.comments.new(limit = None)
    
  def get_submissions(self):
    return self.redditor.submissions.new(limit = None)
  