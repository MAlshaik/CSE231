import string
def build_wordlist(fp):
    lines = fp.readlines()
    words = []
    for i in lines:
        punc = string.punctuation
        w = i.strip().split(' ')
        for x in w:
            new_x = x.translate(str.maketrans('', '', string.punctuation))
            words.append(new_x)
    return words

def find_unique(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x

def main():
    infile = open("test.txt", 'r') 
    word_list = build_wordlist(infile)    
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

if __name__ == "__main__":
    main()