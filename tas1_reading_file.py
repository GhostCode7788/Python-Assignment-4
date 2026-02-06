try:
    with open('Sample.txt','rt') as f:
        line1=f.readline()
        line2=f.readline()
except FileNotFoundError as ferror:
    print("Error: The file 'Sample.txt' was not found.")
    print(ferror)
else:
    print(f'Line 1:{line1}')
    print(f'Line 2:{line2}')