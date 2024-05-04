# Opening files

infile = open("example_text.txt")

print(infile) # prints <_io.TextIOWrapper name='example_text.txt' mode='r' encoding='UTF-8'>

print(infile.read()) # Prints out the text in the infile
print(infile.read()) # Prints nothing as the read cursor is at the end of the file

# At the end of the first read, the cursor is still at the end, thus the other two reads do nothing
# How to get fix this?

infile.seek(0) # 0 is the start of the file

print(infile.read()) 

infile.seek(0)

print(infile.readline()) # prints the first line in the text file

print(infile.readlines()) # Will print out a list of all the lines

infile.seek(0)

# Have to close the file when you open it

infile.close()

