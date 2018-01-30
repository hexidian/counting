import time
f = open("common_words.txt","r")
words = f.read().split()
f.close()
ranges = {
    "0":[chr(i) for i in range(97,110)],#a-m
    "1":[chr(i) for i in range(110,123)]#n-z
}
def word_look(binary):
    length = len(binary)
    for word in words:
        works = True
        if len(word)!=length:
            continue
        for i in range(len(word)):
            if word[i] not in ranges[binary[i]]:#if the letter is in the appropriate range
                works = False
                break
        if works:
            return word
    return False
binary = raw_input("binary?\n>>>")
start = time.time()
print word_look(binary)
print "completed in:",time.time()-start
