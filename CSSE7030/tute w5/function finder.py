def find_functions(filename):
    with open (filename, 'r') as rfile:
        for line in rfile:
            if line[0:4] == 'def ':
            # OR can use if 'def' in line: OR if 'def ' == line[:4] ([:4] means first 4 characters)
                line = line.strip() # str.strip() is use for remove all the space, empty line before or after the string
                print(line)
    
def find_functions_ans(filename):
    with open (filename, 'r') as rfile,\
         open('functions.txt','w') as wfile:
        for line in rfile:
            if 'def' == line[:4]:
                wfile.write(line)
            
    
