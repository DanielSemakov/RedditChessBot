class RedditorModel:
  """Represents a Reddit account, which can be scanned for comments and submissions."""
  
  def __init__(self, redditor):
    self.redditor = redditor

  def get_comments(self):
    return self.redditor.comments.new(limit = None)
    
  def get_submissions(self):
    return self.redditor.submissions.new(limit = None)
  