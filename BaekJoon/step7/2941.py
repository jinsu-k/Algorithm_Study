croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
test = ['c', '=', '-', 'd', 'z', 'l', 'n', 's', '']

word = input()

for i in croatian:
    word = word.replace(i, "_")
    
print(len(word))
#ljes=njak
#ddz=z=
#nljj
#c=c=
#dz=ak
