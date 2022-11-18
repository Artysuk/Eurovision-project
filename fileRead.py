class FileRead():

  def __init__(self, file):
    self.file = file

  def file_reading_return_array(self):
    with open(self.file) as f:
      return list(word.rstrip('\n').split(',') for word in f)

  def file_reading_just_return(self):
    with open(self.file) as f:
      return f

  def file_reading_return_set(self):

    general_dict = {}

    with open(self.file) as f:
      for i in f.readlines():
        general_dict[i.rstrip('\n')] = 0

    return general_dict
