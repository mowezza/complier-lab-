import nltk
print(nltk.__version__)
nltk.download()
sentence = """ At eight o'clock on thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print(tokens)

# code to demonestrate the para tokenizer
from nltk.tokenize import sent_tokenize 
para="""Cake is a form of sweet food made from flour,
sugar, and other ingredients, that is usually baked.
In their oldest forms, cakes were modifications of bread,
but cakes now cover a wide range of preparations that
can be simple or elaborate, and that share features 
with other desserts such as pastries, meringues, custards, and pies.
The most commonly used cake ingredients include flour, sugar, eggs, butter or oil or margarine,
a liquid, and leavening agents, such as baking soda or baking powder."""
tokenized_para= sent_tokenize(para)
print(tokenized_para)
print(type(tokenized_para))

# code to demonestrate the punctuation
from nltk.tokenize import RegexpTokenizer

tokenizer= RegexpTokenizer(r'\w+')
result = tokenizer.tokenize("Wow! I am excited to learn Compiler Designing")
print(result)

#Stop words removal from para
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

to_be_removed= set (stopwords.words ('english'))

para="""Cake is a form of sweet food made from

flour, sugar, and other ingredients, that is

usually baked.

In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of

preparations that can be simple or elaborate, and that share

features with other desserts such as pastries,

meringues, custards,

and pies."""

tokenized_para=word_tokenize(para)

print (tokenized_para)

modified_token_list=[word for word in tokenized_para if not word in to_be_removed]
print(modified_token_list)

# stemming 
from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

content="""Cake is a form of sweet food made from

flour, sugar, and other ingredients, that is usually baked. In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations

that can be simple or elaborate, and that share features with other desserts such as pastries,

meringues, custards, and pies."""

tk_content=word_tokenize(content)

stemmed_words = [stemmer.stem(i) for i  in tk_content]

print(stemmed_words)


