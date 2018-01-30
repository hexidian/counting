import time
ranges = {
    "0":[chr(i) for i in range(97,110)],#a-m
    "1":[chr(i) for i in range(110,123)]#n-z
}
def word_look(binary):
    length = len(binary)
    for word in words:
        if len(word)!=length:
            continue
        for i in range(len(word)):
            if word[i] not in ranges[binary[i]]:#if the letter is in the appropriate range
                continue
        return word
    return False
binary = raw_input("binary?\n>>>")
start = time.time()
if len(binary)!=7:
    f = open("common_words.txt","r")
    words = f.read().split()
    f.close()
    #print test_words("", len(binary), binary)
    print word_look(binary)
else:
    f = open("seven_letter_words.txt","r")
    words = f.read().split()
    f.close()
    #print test_words("", 7, binary)
    print word_look(binary)
print "completed in:",time.time()-start
