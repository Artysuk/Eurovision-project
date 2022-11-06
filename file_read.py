#Not reading files rn

def file_reading_return_array(file):
    with open(file) as f:return list(word.rstrip('\n').split(':') for word in file)

def file_reading_just_return(file):
    with open(file) as f:return f

def file_reading_return_set(file):
    with open(file) as f:return dict(word.rstrip('\n').split(':') for word in file)