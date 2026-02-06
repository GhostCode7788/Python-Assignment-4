write=input("Enter text to write to the file:")
with open('output.txt','wt') as f:
    f.write(write + '\n')
    print("Date succesfully written to output.txt")
append=input("Enter the text to append to the file:")
with open('output.txt','at') as f:
    f.write(append)
    print("Data successfully appended.")
print("Final content of output.txt")
with open('output.txt','rt') as f:
    read=f.read()
    print(read)
