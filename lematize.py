## stop words
## later we convert teh words in to the vector
import nltk
from scipy.sparse import save_npz

from nlp import lemmatizer

paragraph="""My dear young friends, today I want to share a simple message.
 Dream big. Dreams transform into thoughts, and thoughts lead to action. When you have a great aim in life, you must work hard with dedication and persistence. 
 Difficulties will come, but do not give up. Every challenge teaches you something new and strengthens your spirit.
The future of our nation depends on the creativity and courage of its youth. You must develop knowledge, build good character, and always stay optimistic. 
If you contribute even a small effort with honesty and sincerity, you can make a big difference for society.
Remember, success is not measured by money or fame. Success comes from doing your duty, helping others, and improving yourself every day.
Let us work together for a developed and peaceful India. The power to shape your future is within you. So dream, work, and achieve."""

## with thhelp of the stopwords we should remove the extra words inshort
## apply stopwords and stemming

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
print(stopwords.words('english'))
## remove the stopwords then
## apply stemming
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
sentences=nltk.sent_tokenize(paragraph)
type(sentences)

## apply stopwords and filter then applying stemming
for i in range(len(sentences)): ## iterating through the sentence
    words=nltk.word_tokenize(sentences[i])## word tokenize
    word1=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(word1) ## converting all list of word in sentences

print(sentences)

from nltk.stem import SnowballStemmer
snowballstemmer=SnowballStemmer('english')

for i in range(len(sentences)): ## iterating through the sentence
    words=nltk.word_tokenize(sentences[i])## word tokenize
    word1=[snowballstemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(word1) ## converting all list of word in sentences
print(sentences)

## snowball make all letter become small

from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

for i in range(len(sentences)): ## iterating through the sentence
    words=nltk.word_tokenize(sentences[i])## word tokenize
    word1=[lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(word1) ## converting all list of word in sentences
print(sentences)
