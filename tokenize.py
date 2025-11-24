import nltk
nltk.download('punkt')

corpus = """Hello Welcome to Kirat Nlp Understanding tutorial,
please walk with me to the last! how are you"""

corpus = corpus.replace("\n", " ")

from nltk.tokenize import sent_tokenize

print(sent_tokenize(corpus))

## Tokenize
## parahgraph to word and the snetences into the words

from nltk.tokenize import word_tokenize
print(word_tokenize(corpus))

from nltk.tokenize import wordpunct_tokenize
print(wordpunct_tokenize(corpus))

from nltk.tokenize import TreebankWordTokenizer
TOKENIZER=TreebankWordTokenizer()
print(TOKENIZER.tokenize(corpus))
## with the TreeBAnk '.' in between th etext not cinsider as other word but it is in last it consider '.' as other word

## STEMMING
## reduce the word to its word stem affixes ,
# to suffices and prefixes or the roots of words known as a lemma

## classification problem
### comments of product is a positive review or the negative review
## having only the one word from all the similar kind of the word

words=["eating","eats","eaten","writing","writes","programming","programs"]

## porterstemmer
from nltk.stem import PorterStemmer
stemming=PorterStemmer()

for word in words:
    print(word+"--->"+stemming.stem(word))

##stemming.stem('congratulations')

##REGEXpSTEMMER CLASS

from nltk.stem import RegexpStemmer
reg_stemmer=RegexpStemmer('ing$|s$|e$|able$',min=4)
print(reg_stemmer.stem("eating"))


### SNOWBALL STEMMER
## perofrm better than the proter stemmer as it give better accutracy as the better form iof the word
from nltk.stem import SnowballStemmer
sb_stemmer=SnowballStemmer('english')

for word in words:
    print(word+"--->"+sb_stemmer.stem(word))


print(stemming.stem("fairly"))
print(stemming.stem("Sportingly"))

print(sb_stemmer.stem("fairly"))
print(sb_stemmer.stem("Sportingly"))

## snowball stemmer give the best part of the stemming as it give the stem to all od tge word good rethar than the stemming
## LEMMATIZATION

## it is like stemming output we will get after the lemmatization is called as the lemma
## rather than the roof stem the output of teh stemming after the lemmatization we will be getting a valid word that means the same tthing

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("goes",pos='a'))

## POS-n noun
## verv v
## adjective a
#adverb r
words=["eating","eats","eaten","writing","writes","programming","programs"]
for word in word:
    print(word+"--->"+lemmatizer.lemmatize(word,pos='v'))
