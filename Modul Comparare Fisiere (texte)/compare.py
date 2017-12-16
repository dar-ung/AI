from nltk.corpus import wordnet
from nltk.stem import SnowballStemmer
romana = SnowballStemmer("romanian")
#print(romana.stem("oasele"))

with open ('506text.txt', encoding="utf8") as f:
    content = f.readlines()

#content = [romana.stem(x.strip()) + '\n' for x in content]

for i in content:
    if (ord(i[0])>=65 and ord(i[0])<=90) or (ord(i[0])>=97 and ord(i[0])<=122):
        print (i[0:-1], " = ", romana.stem(i[0:-1]))
