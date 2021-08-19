import os

test_file = open('test.txt', 'wb')

print(test_file.mode)

print(test_file.name)

test_file.write(bytes('write me to the file\n', 'UTF-8'))

test_file.close()

test_file = open('test.txt', 'r+')
#open for reading and writing

text_in_file = test_file.read()
print(text_in_file)
#reads info in file

#os.remove('test.txt') comented out for causing errors
#deletes file
