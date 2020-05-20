import numpy as np 

#load data set
trump=open('C:/Users/Jean/trump-speeches-master/speeches.txt',encoding='utf8').read()


#split data set into words
corpus=trump.split()
#print(corpus)

#create pairs to keys
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i],corpus[i+1])

pairs=make_pairs(corpus)

#dictionnary of pairs
word_dict={}
for word_1,word_2 in pairs:
    if word_1 in word_dict.keys():         
         word_dict[word_1].append(word_2)
    else:
        word_dict[word_1]=[word_2]


#build the markov model
first_word=np.random.choice(corpus)

while first_word.islower():
    first_word=np.random.choice(corpus)

chain=[first_word]
n_words=200
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

#predicted text
while(True):
    if chain[-1][-1]!='.':
        chain.pop(-1)
    else:
        break    
print(' '.join(chain))
