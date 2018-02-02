
# coding: utf-8

# In[8]:


import os
import sys, os, re, gzip, tarfile
import itertools
import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import random 
from urllib.request import urlretrieve



# In[9]:


def get_data(data, keep_rate):
    def gunzip_file(gz_path, txt_path):
        """Unzips from gz_path into new_path."""
        print("Unpacking %s to %s" % (gz_path, txt_path))
        with gzip.open(gz_path +"/"+ data + ".txt.gz", "r") as gz_file:
            full_data = gz_file.readlines()
            print("origianl size", len(full_data))
            length_all = len(full_data)
            length_subset = int(length_all * keep_rate/2) * 2
            with open(txt_path +"/"+ data + ".txt", "wb") as new_file:
                new_file.writelines(full_data[:length_subset])
                print("subsetted size", length_subset)
            
    def split_q_a():
        with open(txt_path +"/"+ data+ ".txt") as f, open(txt_path  + "/"+data +'.q', 'w') as q:
            for line in itertools.islice(f, 0, None, 2):
                q.write(line)

        with open(txt_path +"/"+ data+ ".txt") as f, open(txt_path  + "/"+data +'.a', 'w') as a:
            for line in itertools.islice(f, 1, None, 2):
                a.write(line)
    if __name__ == "__main__":
        gunzip_file(gz_path, txt_path)
        print("unzipped")
        split_q_a()
        print("splitted")
        


# In[10]:


def split_dataset(data, ratio):
    """
    train:float, [0,1]
    val:float, [0,1]
    test:float, [0,1]
    """
    x = open(txt_path  + "/" + data + ".q", "r").readlines()
    print("length of question",len(x))
    y = open(txt_path  + "/" + data + ".a", "r").readlines()
    print("length of answer",len(y))


    # number of examples
    data_len = len(x)
    lens = [ int(data_len*item) for item in ratio ]

    trainX, trainY = x[:lens[0]], y[:lens[0]]
    testX, testY = x[lens[0]:lens[0]+lens[1]], y[lens[0]:lens[0]+lens[1]]
    validX, validY = x[-lens[-1]:], y[-lens[-1]:]

    with open(txt_path + "/" + data + "/train.q", "w") as f:
        for line in trainX:
            f.write(line)

    with open(txt_path + "/" + data + "/train.a", "w") as f:
        for line in trainY:
            f.write(line)

    with open(txt_path + "/" + data + "/val.q", "w") as f:
        for line in validX:
            f.write(line)

    with open(txt_path + "/" + data + "/val.a", "w") as f:
        for line in validY:
            f.write(line)

    with open(txt_path + "/" + data + "/test.q", "w") as f:
        for line in testX:
            f.write(line)

    with open(txt_path + "/" + data + "/test.a", "w") as f:
        for line in testY:
            f.write(line)

#     return (trainX,trainY), (testX,testY), (validX,validY)
    print("Q & A splited")

    


# In[11]:


def get_vocab(vocal_size):
    with open(txt_path  + "/"+data +'.txt') as fd:
        book = fd.read()
        book = book.lower()
        tokenizer = RegexpTokenizer(r'\w+')
        book = tokenizer.tokenize(book)
    num_words = len(Counter(book))
    print("Unique words: " + str(num_words))
    vocab_size = vocal_size
    words_and_count = Counter(book).most_common(vocab_size)
    with open(txt_path +"/"+data + "/" +'vocab.q',"w") as vb:
        words = []
        known_count = 0
        all_count = sum(Counter(book).values())
        for word_count in words_and_count:
            words.append(word_count[0])
            known_count += word_count[1]
        for word in words:
            vb.write(word+'\n')
        print("vocab size", vocal_size )
        print("unknown rate:", (1 - (known_count/all_count))*100,"%")
        unk = Counter(book).most_common(vocab_size).sort()
        vb.close() 
    with open(txt_path +"/"+data + "/" +'vocab.a',"w") as vb:
        words = []
        for word_count in words_and_count:
            words.append(word_count[0])
        for word in words:
            vb.write(word+'\n')
        vb.close() 





# In[ ]:





# In[20]:


pwd = os.getcwd()
gz_path = pwd + '/tmp'
txt_path = pwd + "/tmp/nmt_data"
print(gz_path)
print(txt_path)


# In[23]:


if not os.path.exists(gz_path + '/open_subtitiles.txt.gz'):
    print("opencc dataset doesn't exist, downloading...")
    urlretrieve("https://github.com/Marsan-Ma/chat_corpus/raw/master/open_subtitles.txt.gz", gz_path + "/opencc.txt.gz")
else: print("opencc dataset exists")
if not os.path.exists(gz_path + '/twitter_en.txt.gz'):
    print("twitter dataset doesn't exist, downloading...")
    urlretrieve("https://github.com/Marsan-Ma/chat_corpus/raw/master/twitter_en.txt.gz", gz_path + "/twitter.txt.gz")
else: print("twitter dataset exists")


# In[27]:


datasets = ['opencc', 'twitter']
for data in datasets:
    if not os.path.exists(txt_path + "/" + data):
        print("data folders don't exsits, creating...")
        os.makedirs(txt_path + "/" + data)
    else: print("generating data:", data)
    get_data(data, keep_rate=0.1)
    split_dataset(data, ratio = [0.7,0.15,0.15])
    get_vocab(8000)


# In[ ]:




