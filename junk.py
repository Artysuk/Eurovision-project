def file_reading_return_array(file):
    with open(file,'r',encoding = 'utf-8') as f:return list(word.rstrip('\n').split(':') for word in file)


print(file_reading_return_array('eurovision.txt'))