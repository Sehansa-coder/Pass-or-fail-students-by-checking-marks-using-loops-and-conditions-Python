file_path="C:/Users/user/Downloads/seha.txt"
files=open(file_path,"r")

content=files.read()
print(content)


oneline=files.readline() 
print(oneline)

# by using readline, only the first line will be printed

line2=files.readline()
print(line2)  
# the next line of the text file will be printed

looping=files.readlines()   # put 's' to iterate through line.if not it will loop through letters in each word
for line in looping:
    print(line)

logic=files.readlines()
for line in logic:
    if line.startswith("love yourself"): # only printing the needed line n the text
        print(line)

