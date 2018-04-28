#Lab 4
#Takes typed phrase and removes punctuation

punctuation=['(',')','?',':',';',',','.','!','/','"',"'"]

sentence=input("Type in a line of text >")
alist=list(sentence)
print(alist)

for string in sentence:
    if string in punctuation:
        alist.remove(string)

newsentence=''.join(alist)
print(newsentence)