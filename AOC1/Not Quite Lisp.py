inpFile = '2input.txt'
with open(inpFile, 'r') as f:
    text = f.readlines()
 
 
count=0   
for i in text:
    if i=='(':
        count+=1
    if i==')':
        count-=1
print(count)