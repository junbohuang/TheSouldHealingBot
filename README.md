# Tensorflow Seq2seq Chatbot 0.1
### Requirement
- tf 1.4
- tf.nightly
- tf.nmt
- data below

## what is here
- model directly folked from tensorflow/nmt
- add split_data.py integrating data from https://github.com/Marsan-Ma/twitter_scraper in the model


## how to run
### run bash files in terminal for opencc/twitter dataset, or inference
### first acquire and split data
'''bash
python split_data.py
'''
### then run bash
'''bash
bash opencc.sh
bash twitter.sh'''
### inference can be done once the model has checkpoint available 
'''bash
bash infer.sh'''
