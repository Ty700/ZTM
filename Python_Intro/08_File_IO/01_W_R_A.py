# Write, Read, Append

# open default mode = 'r', 'w' = write, 'a' = append
# 'r+' = R/W
with open('example_text.txt', mode='a') as my_file: 
    # my_file.read() # can't do this if in write/append mode only
    my_file.write('\nMy name is Tyler\n') # Returns the amount of bytes writen

