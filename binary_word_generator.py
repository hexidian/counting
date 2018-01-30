f = open("common_words.txt","r")
words = f.read().split()
f.close()
def test_words(prev_word, more, binary):
    this_binary = int(binary[-more])* -1 + 1
    if more==0:
        return prev_word if prev_word in words else False

    prev_word
    for i in range(13):
        test_word = prev_word + chr(97+i+ (13*this_binary) )
        test = test_words(test_word, more-1, binary)
        if test:
            return test

    return False

binary = raw_input("binart?\n>>>")
print test_words("", len(binary), binary)
