def format_list(inpt):
    output = ""
    for i in inpt:
        output += str(i) + "\n"
    return output
f = open("common_words.txt","r")
words = f.read().split()
f.close()
sev_words = []
for i in words:
    if len(i)==7:
        sev_words.append(i)
f = open("seven_letter_words.txt","w")
f.write(format_list(sev_words))
f.close()
