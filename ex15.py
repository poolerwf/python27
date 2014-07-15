# import argv
from sys import argv

# prepar vars for arguments
script, filename = argv

# open filename passed
txt = open(filename)

# present filename and contents
print "Here's  your file %r:" % filename
print txt.read()

# close file
txt.close()

# request user to reenter filename
print "Type the filename again:"
file_again = raw_input("> ")

# open file again
txt_again = open(file_again)

# print file contents again
print txt_again.read()

# close file
txt_again.close()